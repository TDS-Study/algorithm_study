import java.util.*
import kotlin.math.*

//17266번 : 어두운 굴다리
//https://www.acmicpc.net/problem/17266

fun main() = with(Scanner(System.`in`)) {
    val n = nextLine().toInt() // n: 굴다리의 길이
    val m = nextLine().toInt() // m: 가로등의 개수
    var x = nextLine().split(" ").map(String::toInt).toIntArray() // x: 가로등의 위치
    var maxDiff = 1

    for (idx in 0 until x.size-1)
    {
        val dif = x[idx+1]-x[idx]
        if(maxDiff < dif) maxDiff = dif
    }

    //좌우 시작과 끝의 각각의 거리
    var firstDiff = x[0]
    var lastDiff  = n - x[x.lastIndex]

    var resultArr = arrayListOf<Int>(ceil(maxDiff.toDouble()/2).toInt(), firstDiff, lastDiff)

    print(resultArr.maxOrNull())
}

