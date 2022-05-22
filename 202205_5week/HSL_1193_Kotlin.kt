import java.util.*
import kotlin.math.*

//1193번 : 2차원 분수 배열
//https://www.acmicpc.net/problem/1193

fun main() = with(Scanner(System.`in`)) {
    var n = nextInt() // n번째 자리

    var rangeSPos = 1
    var rangeEPos = 1
    var numerator = 0   //출력 분자값
    var denominator = 0 //출력 분모값

    for(idx in 1..10000000)
    {
        if((rangeSPos < n && n< rangeEPos)
            || n == rangeSPos
            || n == rangeEPos)
        {
            var startPos = rangeSPos
            var isOdd = true
            if (idx % 2 == 0) isOdd = false

            if(isOdd){
                numerator = idx //분자
                denominator = 1 //분모
            }else
            {
                numerator = 1 //분자
                denominator =  idx //분모
            }

            while(n > startPos)
            {
                if(isOdd){
                    numerator-=1
                    denominator+=1
                }else
                {
                    numerator+=1
                    denominator-=1
                }

                startPos++
            }
            break
        }

        rangeSPos += idx
        rangeEPos += idx+1
    }

    print("$numerator/$denominator")
}

