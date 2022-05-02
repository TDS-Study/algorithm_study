import com.sun.xml.internal.fastinfoset.util.StringArray
import java.util.*
import kotlin.math.roundToLong

//1895 : 이미지 필터
//첫째 줄에 필터링 된 이미지 J의 각 픽셀 값 중에서 T보다 크거나 같은 것의 개수를 출력

fun main() = with(Scanner(System.`in`)) {
    //region 입력 받은 값 처리
    val firstLine = nextLine()            // 입력 받은 첫 번째 row string
    var configList = firstLine.split(' ') // 첫 번째 입력 row string 공백 기준으로 배열화

    val rowCnt = configList[0].toInt()    // 행의 수
    val columnCnt = configList[1].toInt() // 열의 수

    //두번째 row 입력 string
    val lines = arrayListOf<String>()
    repeat(rowCnt) { lines.add(nextLine()) }

    val tCompareValue = nextLine().toInt() // 입력 받은 마지막 줄의 T값 (필터링된 이미지 결과와 최종 비교 할 값)    
    val inputArray = Array(rowCnt) { IntArray(columnCnt) } //2차원 배열 선언 (입력 받은 값을 2차원 배열화)

    for (index in 0 until lines.count()) {
        var rowArray = lines[index].split(' ').map(String::toInt).toIntArray()
        inputArray.set(index, rowArray)
    }
    //endregion

    var resultArray = ArrayList<Int>() // 필터링된 이미지 저장할 2차원 배열

    //이미지 필터링 로직
    //입력 받은 2차원 배열의 [0,0]부터 시작하여 이미지 필터링
    for (columnIdx in 0 until columnCnt) {
        if (columnIdx + 2 > columnCnt - 1) break; //이미지 필터링을 할 수 없는 범위

        for (rowIdx in 0 until rowCnt) {
            if (rowIdx + 2 > rowCnt - 1) break;   //이미지 필터링을 할 수 없는 범위

            var tempArray = ArrayList<Int>()

            // 이미지 필터링을 위한 9 X 9 범위로 값 가져오기.
            tempArray.add(inputArray[rowIdx][columnIdx].toInt())
            tempArray.add(inputArray[rowIdx][columnIdx + 1].toInt())
            tempArray.add(inputArray[rowIdx][columnIdx + 2].toInt())

            tempArray.add(inputArray[rowIdx + 1][columnIdx].toInt())
            tempArray.add(inputArray[rowIdx + 1][columnIdx + 1].toInt())
            tempArray.add(inputArray[rowIdx + 1][columnIdx + 2].toInt())

            tempArray.add(inputArray[rowIdx + 2][columnIdx].toInt())
            tempArray.add(inputArray[rowIdx + 2][columnIdx + 1].toInt())
            tempArray.add(inputArray[rowIdx + 2][columnIdx + 2].toInt())

            tempArray.sort()               // 중간 값을 가져오기 위한 정렬
            val middelValue = tempArray[4] // 정렬된 값 중에서 중간 값인 5번째 값 가져오기.
            resultArray.add(middelValue)   // 중간 값을 최종 배열에 추가.
        }
    }

    var result = resultArray.filter { it >=  tCompareValue}.count() //이미지 필터링된 최종 배열에서 T 값보다 큰 값의 COUNT RETURN.
    print(result)
}
