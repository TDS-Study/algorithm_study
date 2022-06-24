using System;
using System.Linq;
using System.Collections.Generic;

public class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        List<int> result = new List<int>();
        int curIdx = 0;
            
        while(curIdx < progresses.Length)
        {    
            //현재 기준 작업이 100% 도달 여부 검증
            if(progresses[curIdx] >=100)            
            {
                curIdx++;
                int releaseCnt = 1;                
                
                //뒤에 작업이 진도율이 100% 인지 확인
                for(int j = curIdx; j<progresses.Length; j++)
                {
                    if(progresses[j] >=100){
                        curIdx++;
                        releaseCnt++;
                    } 
                    else break;                
                }   
                result.Add(releaseCnt);
            }
            
            //개별 작업의 하루 작업량만큼 진도율 증가
             for(int k = curIdx; k<progresses.Length; k++)
             {
                progresses[k] += speeds[k];
             }     
        }        
        
        int[] answer = new int[] {};
        answer = result.ToArray();
        return answer;
    }
}
