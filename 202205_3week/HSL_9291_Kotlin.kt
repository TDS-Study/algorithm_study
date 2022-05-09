import com.sun.xml.internal.fastinfoset.util.StringArray
import java.util.*
import kotlin.math.roundToLong

//9291 : 스도쿠 채점
//https://www.acmicpc.net/problem/9291

fun main() = with(Scanner(System.`in`)) {
    //region 입력 받은 값 처리
    val firstLine = nextLine()            // 입력 받은 첫 번째 row string
    val testCaseCnt= firstLine.toInt()    // 테스트 해야 될 case count
    val rowCnt = 9                        // 테스트 케이스의 row count
    val columnCnt = 9                     // 테스트 케이스의 column count

    //두번째 row 입력 string (TEST case)
    val lines = arrayListOf<String>()
    repeat((testCaseCnt*rowCnt)+testCaseCnt-1)
    {
        val lineString = nextLine()
        if(!lineString.isNullOrEmpty()) lines.add(lineString)
    }

    var lineIdx =0
    var returnString = ""

    for(testCaseIdx in 0 until testCaseCnt)
    {
        var isCorrect = true

        //region 입력 받은 테스트 케이스 string 2차원 배열화
        val testCaseArray = Array(rowCnt) { IntArray(columnCnt) }

        lineIdx = testCaseIdx*rowCnt
        for(idx in 0 until rowCnt)
        {
            var rowArray = lines[lineIdx].split(' ').map(String::toInt).toIntArray()
            testCaseArray.set(idx, rowArray)
            lineIdx++
        }

        if(isCorrect == true)
        {
            for(idx in 0 until rowCnt)
            {
                //행의 값의 합 체크
                var rowSum = testCaseArray[idx].sum()

                if (rowSum != 45)
                {
                    isCorrect = false
                    break
                }
            }
        }

        if(isCorrect == true)
        {
            for(idx in 0 until columnCnt)
            {
                val eachColumnSumList = List(columnCnt){ col -> testCaseArray.map{it[col]}.sum()}

                if (eachColumnSumList.filter { it != 45 }.count() > 0)
                {
                    isCorrect = false
                    break
                }
            }
        }

        //println(isCorrect)

        if(isCorrect == true)
        {
            for (columnIdx in 0 until columnCnt step 3) {
                if (columnIdx + 2 > columnCnt - 1) break; //이미지 필터링을 할 수 없는 범위

                for (rowIdx in 0 until rowCnt step 3) {
                    if (rowIdx + 2 > rowCnt - 1) break;   //이미지 필터링을 할 수 없는 범위

                    var tempArray = ArrayList<Int>()

                    // 이미지 필터링을 위한 3 X 3 범위로 값 가져오기.
                    tempArray.add(testCaseArray[rowIdx][columnIdx].toInt())
                    tempArray.add(testCaseArray[rowIdx][columnIdx + 1].toInt())
                    tempArray.add(testCaseArray[rowIdx][columnIdx + 2].toInt())

                    tempArray.add(testCaseArray[rowIdx + 1][columnIdx].toInt())
                    tempArray.add(testCaseArray[rowIdx + 1][columnIdx + 1].toInt())
                    tempArray.add(testCaseArray[rowIdx + 1][columnIdx + 2].toInt())

                    tempArray.add(testCaseArray[rowIdx + 2][columnIdx].toInt())
                    tempArray.add(testCaseArray[rowIdx + 2][columnIdx + 1].toInt())
                    tempArray.add(testCaseArray[rowIdx + 2][columnIdx + 2].toInt())

                    //println(tempArray)
                    //println(tempArray.sum())
                    if (tempArray.sum() != 45 )
                    {
                        isCorrect = false
                        break
                    }
                }
            }
        }

        if(returnString.isNotEmpty()) returnString+= "\n"

        returnString += "Case " + (testCaseIdx+1).toString() + ": "

        if (isCorrect == false) returnString += "INCORRECT"
        else returnString += "CORRECT"
    }

    print(returnString)
}
