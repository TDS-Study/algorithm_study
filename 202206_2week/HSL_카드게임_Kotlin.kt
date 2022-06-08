import java.io.BufferedReader
import java.io.InputStreamReader
import java.lang.Math.abs
import java.util.*
import kotlin.collections.ArrayList

//두명의 카드 플레이어의 카드가 잘 섞였는지 확인하는 문제.
//문제가 잇는 라운드가 몇개인지 return

fun main() {
    //cards1 플레이어1
    var cards1 = arrayOf(arrayOf(1,2,3,4,5), arrayOf(6,7,8,9,10))
    //cards2 플레이어2
    var cards2 = arrayOf(arrayOf(5,7,8,11,13), arrayOf(11,13,15,17,19))

    var answer = 0

    for(idx in 0 .. cards1.size-1)
    {
        var diff = 0
        //cards1, cards2 두 플레이어의 카드 중 겹치는 카드의 갯수 구하기
        diff += cards1[idx].intersect(cards2[idx].toList()).count()

        if(idx+1 < cards1.size)
        {
            diff += cards1[idx].intersect(cards1[idx + 1].toList()).count()
            diff += cards2[idx].intersect(cards2[idx + 1].toList()).count()
        }
        if (diff>0) answer++
    }

    print(answer)
}
