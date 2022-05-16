import javafx.util.converter.BigDecimalStringConverter
import java.math.BigDecimal
import java.util.*
import kotlin.math.*

//1292번: 선행학습
//(1 ≤ A ≤ B ≤ 1,000)

fun main() = with(Scanner(System.`in`)) {
    val sPos = nextInt() //시작 위치
    val ePos = nextInt() //종료 위치

    var arr = IntArray(1000, {0})
    var arrIdx = 1
    var value = 1
    var returnValue = 0

    while(arr.size >= arrIdx)
    {
        if (ePos < arrIdx) break

        repeat(value)
        {
            if (sPos <= arrIdx  && arrIdx <= ePos){ returnValue +=value}
            arrIdx++
        }
        value++
    }

    //print(arr.copyOfRange(sPos-1,ePos).sum())
    print(returnValue)
}
