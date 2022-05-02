import com.sun.xml.internal.fastinfoset.util.StringArray
import java.util.*
import kotlin.math.roundToLong

//2865 : 나는 위대한 슈퍼스타K
//능력의 합이 최대가 되도록 참가자와 장르를 선택하는 프로그램 작성

fun main() = with(Scanner(System.`in`)) {
    //region 입력단
    //첫번째 row 입력 string
    val firstLine = nextLine()
    var configToken = firstLine.split(' ') // 첫번째 입력 row 공백 기준으로 분리

    val rowCnt = configToken[0].toInt() // 행의 수
    val columnCnt = configToken[1].toInt()     // 열의 수

    //두번째 row 입력 string
    val lines = arrayListOf<String>()
    repeat(rowCnt) { lines.add(nextLine()) }

    val tCompareValue = nextLine().toInt() //필터링된 결과와 비교 할 값.

    //2차원 배열 선언
    val inputArray = Array(rowCnt) { IntArray(columnCnt) }

    for (index in 0 until lines.count()) {
        var rowArray = lines[index].split(' ').map(String::toInt).toIntArray()
        inputArray.set(index, rowArray)
    }
    //endregion

    var resultArray = ArrayList<Int>()

    for (columnStartIdx in 0 until columnCnt) {
        if (columnStartIdx + 2 > columnCnt - 1) break;

        for (rowStartIdx in 0 until rowCnt) {
            if (rowStartIdx + 2 > rowCnt - 1) break;

            var tempArray = ArrayList<Int>()

            tempArray.add(inputArray[rowStartIdx][columnStartIdx].toInt())
            tempArray.add(inputArray[rowStartIdx][columnStartIdx + 1].toInt())
            tempArray.add(inputArray[rowStartIdx][columnStartIdx + 2].toInt())

            tempArray.add(inputArray[rowStartIdx + 1][columnStartIdx].toInt())
            tempArray.add(inputArray[rowStartIdx + 1][columnStartIdx + 1].toInt())
            tempArray.add(inputArray[rowStartIdx + 1][columnStartIdx + 2].toInt())

            tempArray.add(inputArray[rowStartIdx + 2][columnStartIdx].toInt())
            tempArray.add(inputArray[rowStartIdx + 2][columnStartIdx + 1].toInt())
            tempArray.add(inputArray[rowStartIdx + 2][columnStartIdx + 2].toInt())

            tempArray.sort()
            val middelValue = tempArray[4]
            resultArray.add(middelValue)
        }
    }

    var result = resultArray.filter { it >=  tCompareValue}.count()
    print(result)
}
