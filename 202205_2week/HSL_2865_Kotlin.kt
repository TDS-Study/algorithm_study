import com.sun.xml.internal.fastinfoset.util.StringArray
import java.util.*
import kotlin.math.roundToLong

//2865 : 나는 위대한 슈퍼스타K
//능력의 합이 최대가 되도록 참가자와 장르를 선택하는 프로그램 작성

//Data Item선언
data class Audition(
    val no : Int
    ,var score: Double
)

fun main() = with(Scanner(System.`in`)) {
    //region 입력단
    //첫번째 row 입력 string
    val firstLine = nextLine()
    var configToken = firstLine.split(' ') // 첫번째 입력 row 공백 기준으로 분리

    val candidateCnt = configToken[0].toInt() // 지원자 수
    val genreCnt = configToken[1].toInt()     // 노래 장르수
    val finalCnt = configToken[2].toInt()     // 본선 참가자 수

    //두번째 row 입력 string
    val lines = arrayListOf<String>()
    repeat(genreCnt) { lines.add(nextLine()) }

    //2차원 배열 선언
    var inputArray = Array(genreCnt){ Array<Audition?>(candidateCnt){null}}

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
    3 2 2
    2 3.0 1 0.2 3 0.1
    3 1.0 2 0.5 1 0.2

    - 사용하기 쉽게 2차원 배열로 정리
    [지원자번호, 점수]

    [2, 3.0] [1, 0.2] [3, 0.1]
    [3, 1.0] [2, 0.5] [1, 0.2]

    지원자수 : 3
    노래 장르수 : 2
    본선 참가자 수: 2

    //결과 출력을 위한 빈 array 선언
    1. 각 지원자의 장르별 점수 중에서 가장 큰 점수를 가져온다.
    2. 그 중에서 점수별로 내림차순 정리한다.
    3. 본선 참가자 수 만큼 위에서 더한 결과를 return

    */

    var finalCandidate = ArrayList<Audition>()

    for(index in 0 .. candidateCnt-1)
    {
        for(genIndex in 0 .. genreCnt-1)
        {
            var number = inputArray[genIndex][index]!!.no
            var score = inputArray[genIndex][index]!!.score

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

    finalCandidate.sortByDescending { it.score }

    var result  = 0.0

    for(index in 0 until finalCnt)
    {
        result += finalCandidate[index].score
    }

    println(roundDigit(result,1))
}

fun roundDigit(number : Double, digits : Int): Double {
    return Math.round(number * Math.pow(10.0, digits.toDouble())) / Math.pow(10.0, digits.toDouble())
}
