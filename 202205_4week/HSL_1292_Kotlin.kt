import javafx.util.converter.BigDecimalStringConverter
import java.math.BigDecimal
import java.util.*
import kotlin.math.*

//1292번: 선행학습
//(1 ≤ A ≤ B ≤ 1,000)

fun main() = with(Scanner(System.`in`)) {
    //region 입력단
    val sPos = nextInt() //시작 위치
    val ePos = nextInt() //종료 위치
    //endregion

    var arr = IntArray(1000, {0})
    var arrIdx = 0
    var value = 1

    while(arr.size > arrIdx)
    {
        repeat(value)
        {
            if (arrIdx < arr.size)
            {
                arr[arrIdx] = value
                arrIdx++
            }
        }
        value++
    }

    print(arr.copyOfRange(sPos-1,ePos).sum())
}
