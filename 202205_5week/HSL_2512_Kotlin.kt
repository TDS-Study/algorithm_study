import java.util.*
import kotlin.math.*

//2512번 : 나라예산
//https://www.acmicpc.net/problem/2512

fun main() = with(Scanner(System.`in`)) {
    val n = nextLine().toInt() // n: 지방의 수
    val budgetList = nextLine().split(" ").map(String::toInt).toIntArray().sorted() // 각 지방의 요청한 예산 목록
    val totalBudget = nextLine().toInt() // 주어진 총 예산

    var returnValue = 0

    //이분탐색 범위 지정을 위한 변수
    var sRange = 1                 //시작
    var eRange = totalBudget       //끝
    var maxBudget = totalBudget/2  //중간값(상한액)
    
    while (true)
    {
        //이분탐색 중간 값
        var sumValue = 0 //해당 상한액으로 할 경우, 필요한 전체 예산

        //만약 각 지방의 요청한 예산의 합이, 편성된 예산보다 작은 경우, 요청한 예산중에 가장 큰 값을 return 하고 연산 종료.
        if(totalBudget >= budgetList.sum()) {
            returnValue = budgetList.maxOrNull()!!
            break
        }

        //상한액(중간값)을 기준으로 예산을 편성할 경우, 전체 얼마의 예산이 필요한지 계산.
        for(budget in budgetList)
        {
            if (budget >= maxBudget) sumValue += maxBudget
            else sumValue += budget
        }

        when{
            sumValue == totalBudget -> { returnValue = maxBudget; break }
            sumValue < totalBudget  -> { sRange = maxBudget
                                         maxBudget = sRange + (eRange - sRange)/2 }
            else ->{ eRange = maxBudget
                     maxBudget = sRange + (eRange-sRange)/2 }
        }
        returnValue = maxBudget //최대 편성 가능한 예산을 찾기 위함.

        if(sRange==maxBudget || eRange==maxBudget) break
    }

    print(returnValue)
}



