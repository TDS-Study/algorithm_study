import com.sun.xml.internal.fastinfoset.util.StringArray
import java.util.*
import kotlin.math.roundToLong

//2865 : 나는 위대한 슈퍼스타K
//능력의 합이 최대가 되도록 참가자와 장르를 선택하는 프로그램 작성

//Data Item 선언 (참가자 번호, 점수)
data class Audition(
    val no : Int
    ,var score: Double
)

fun main() = with(Scanner(System.`in`)) {
    //region 입력단
    val firstLine = nextLine()                       // 첫번째 입력 row string
    var configToken = firstLine.split(' ') // 첫번째 입력 row string을 공백 기준으로 배열화

    val candidateCnt = configToken[0].toInt() // 지원자 수
    val genreCnt = configToken[1].toInt()     // 노래 장르수
    val finalCnt = configToken[2].toInt()     // 본선 참가자 수

    val lines = arrayListOf<String>()         //두번째 row 입력 string
    repeat(genreCnt) { lines.add(nextLine()) }

    var inputArray = Array(genreCnt){ Array<Audition?>(candidateCnt){null}} // 입력받은 지원자 장르별점수를 2차원 배열로 저장하기 위함.

    // 입력 받은 지원자들의 장르별 점수를 2차원 배열로 저장 (Audition 아이템에 저장)
    for(index in 0 until lines.count())
    {
        var candidateArray = Array<Audition?>(candidateCnt){null}
        var splitArray = lines[index].split(' ')  //2번째 입력 줄의 값을 공백단위로 split ... "4 5.0 2 4.0 3 2.0 1 1.0" -> [4] [5.0] [2] [4.0] [3] [2.0] [1] [1.0]

        var setIndex = 0
        for(subIndex in 0 until  splitArray.count() step 2)
        {
            var no = splitArray[subIndex].toInt()           //지원자 번호 추출
            var score = splitArray[subIndex+1].toDouble()   //지원자 점수 추출
            candidateArray.set(setIndex++, Audition(no = no, score = score) ) //array 추가
        }

        inputArray.set(index, candidateArray)
    }
    //endregion

    /* 로직 설명

    - 입력값
    4 4 3
    4 5.0 2 4.0 3 2.0 1 1.0
    2 2.0 3 1.0 1 0.5 4 0.3
    4 6.0 3 5.0 2 2.0 1 0.0
    1 4.0 2 3.0 4 0.6 3 0.3

    지원자수 : 4
    노래 장르수 : 4
    본선 참가자 수: 3

    - 사용하기 쉽게 2차원 배열로 정리 (Audition 아이템에 담아서 2차원 배열로 정리)
    [지원자번호, 점수]
    행: 장르 별 최고 점수를 좌측 부터 기입되어 있음.

    [4, 5.0] [2, 4.0] [3, 2.0] [1, 1.0]
    [2, 2.0] [3, 1.0] [1, 0.5] [4, 0.3]
    [4, 6.0] [3, 5.0] [2, 2.0] [1, 0.0]
    [1, 4.0] [2, 3.0] [4, 0.6] [3, 0.3]

    //결과 출력을 위한 빈 array 선언
    1. 첫 번째 열의 값이 각 장르의 최고 점수임..동일한 참가자가 2개 장르에서 1등인 경우..아래처럼 큰 값 3개를 저장.
         [4, 5.0] [2, 4.0] [3, 2.0] [1, 1.0]
        *[2, 2.0] [3, 1.0] [1, 0.5] [4, 0.3]
        *[4, 6.0] [3, 5.0] [2, 2.0] [1, 0.0]
        *[1, 4.0] [2, 3.0] [4, 0.6] [3, 0.3]

    2. 두 번째 열에서 첫번째 열에서 저장한 참가자 목록 중에서 더 큰 값이 있다면 더 큰 값으로 해당 값 교체.
       혹은 첫번째 열에서 없는 참가자 중에서 큰 값이 있다면 그 값을 취한다.
         [4, 5.0] *[2, 4.0] [3, 2.0] [1, 1.0]
         [2, 2.0]  [3, 1.0] [1, 0.5] [4, 0.3]
        *[4, 6.0] *[3, 5.0] [2, 2.0] [1, 0.0]
        *[1, 4.0]  [2, 3.0] [4, 0.6] [3, 0.3]
    3. 이렇게 마지막 열까지 각 참가자의 최고 점수 값을 취하게 한다.
    4. 마지막에 그렇게 취한 배열의 값들을 내림차순 정렬 한 후에, 최종 참가자 수만큼 자른 후에 sum

    */

    var finalCandidate = ArrayList<Audition>()

    for(columnIdx in 0 .. candidateCnt-1) 
    {//참가자 수 (열)
        for(rowIdx in 0 .. genreCnt-1)
        {//장르 수 (행)
            var number = inputArray[rowIdx][columnIdx]!!.no
            var score = inputArray[rowIdx][columnIdx]!!.score

            //최종 본선 참가자 목록의 동일 참가자 보다 점수가 큰 경우, 큰 점수로 교체
            var duplicateItem = finalCandidate.find { it?.no == number && it?.score < score }

            if (duplicateItem != null)
            {
                finalCandidate.remove(duplicateItem)
                finalCandidate.add(Audition(no = number, score = score))
            }
            else if(finalCandidate.filter { it.no == number }.isEmpty())
            {
                finalCandidate.add(Audition(no = number, score = score))
            }
        }
    }

    finalCandidate.sortByDescending { it.score }  //최종 참가자 N명 만큼 자르기 위한 오름차순 정렬

    var result  = 0.0

    for(index in 0 until finalCnt)
    {
        result += finalCandidate[index].score //최종 참가자 수 만큼 sum
    }

    println(roundDigit(result,1))
}

fun roundDigit(number : Double, digits : Int): Double {
    return Math.round(number * Math.pow(10.0, digits.toDouble())) / Math.pow(10.0, digits.toDouble())
}
