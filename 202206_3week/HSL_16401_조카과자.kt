import java.io.BufferedReader
import java.io.InputStreamReader
import java.lang.Math.abs
import java.lang.Math.floor
import java.util.*
import kotlin.collections.ArrayList

//16401번: 조카 과자 나눠주기
//https://www.acmicpc.net/problem/16401

fun main(args: Array<String>) {
    //region VARIABLES
    val br = BufferedReader(InputStreamReader(System.`in`))
    var st = StringTokenizer(br.readLine())
    var st2 = StringTokenizer(br.readLine())

    var memCnt   = st.nextToken().toInt()   //조카 수
    val cookieCnt = st.nextToken().toInt()  //쿠키수
    var cookieList = ArrayList<Long>(cookieCnt) // 각 강의의 길이(분 단위)
    for(idx in 0 until cookieCnt) cookieList.add(st2.nextToken().toLong())
    //endregion

    //이분탐색 조건 정의
    cookieList.sort()

    var left   = 1 //왼쪽 끝 값이 됨. 강의의 길이 중에서 가장 큰 값이 왼쪽 끝 값이 됨.(이유는 모든 강의가 최소한 하나의 블루레이에 담길 수 있어야 하므로)
    var right  = cookieList[cookieList.lastIndex] //하나의 블루레이에 모든 영상을 담는 경우가 최대 블루레이 크기이므로 right 값으로 강의 전체 sum을 right로 정의
    var middle = (left+right)/2

    var answer = 0

    while(true)
    {
        var cnt:Long = 0
        var availableList = cookieList.filter { it >= middle }.toList()

        for(idx in 0 until availableList.size)
        {
            cnt += availableList[idx]/middle
        }

        when
        {
            memCnt <= cnt -> {
            //조카 수보다, 실제 중간 값으로 나눈 값이 더 많으므로 우측 이동
                if(answer < middle) answer = middle.toInt()
                left = (middle +1).toInt()
            }
            memCnt > cnt -> {
            //블루레이 크기가 너무 크게 설정 되었으므로 좌측으로 이동                
                right = middle -1
            }
        }
        middle = (left+right)/2

        if(right < left) break
    }

    print(answer) //블루레이값(중간값)이 같은 것 중에서 최소의 값 return
}
