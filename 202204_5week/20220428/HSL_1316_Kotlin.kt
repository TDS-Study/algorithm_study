import java.util.*

//1316 : 그룹 단어 갯수 구하는 문제

fun main() = with(Scanner(System.`in`)) {
    //입력단
    val n = nextInt()
    val stringLineList = arrayListOf<String>()
    repeat(n) { stringLineList.add(next()) }

    //로직 시작
    var notGroupWordCnt = 0

    stringLineList.forEach{ // 입력 받은 string 배열 반복
        var isGroupWord:Boolean = true

        for (index in 0 until it.length) // 입력 받은 단어를 한글자씩 쪼개어 반복
        {
            var char = it.get(index) //단어의 한글자씩 가져오기.

            for(subIndex in index+1 until it.length) //가져온 글자의 다음 글자부터 for문으로 비교 하여 group여부 체크
            {
                var lastIndex = it.indexOf(char, subIndex-1) ////char변수 이후 글자 중에서  char변수와 같은 글자의 직전 index 반환
                var nextIndex = it.indexOf(char, subIndex) //char변수 이후 글자 중에서  char변수와 같은 글자의 index 반환

                if(nextIndex == -1) break //nextIndex가 없는 경우는 제외(맨 끝자리 도달함)

                if((nextIndex - lastIndex) >1) 
                {
                    isGroupWord = false
                    break
                }
            }
        }

        if (!isGroupWord) notGroupWordCnt++
    }
    print(stringLineList.size - notGroupWordCnt)
}
