import java.util.*
import kotlin.math.*

//5585번 : 잔돈

fun main() = with(Scanner(System.`in`)) {
    var returnMoney = 1000 - nextLine().toInt() // 받아야 될 거스름 돈
    val changeMoneyList = arrayListOf<Int>(500,100,50,10,5,1) //가지고 있는 거스름돈 큰 순서로 정렬

    var answer = 0
    
    for(money in changeMoneyList)
    {//큰 돈부터 잔돈 지급.
        if(returnMoney == 0) break //거슬러 줄 돈이 0원일 때까지 반복
        answer += returnMoney/money
        returnMoney %= money
    }

    print(answer)
}



