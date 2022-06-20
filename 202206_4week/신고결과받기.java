
import java.util.*;
import java.util.Map.Entry;

// https://programmers.co.kr/learn/courses/30/lessons/92334

public class 신고결과받기 {
    public static void main(String[] args) {
        String[] id_list = { "muzi", "frodo", "apeach", "neo" };

        String[] report = { "muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi" };
        int k = 2;

        Solution s = new Solution();

        s.solution(id_list, report, k);
    }
}

class Solution {
    public int[] solution(String[] id_list, String[] report, int k) {
        int[] answer = new int[id_list.length];
        // 신고받은사람 별 신고한사람 HashSet* 
        // *HashSet 으로 중복신고 제거
        HashMap<String, Set<String>> ds = new HashMap<String, Set<String>>();
        
        // 신고받은 사람 목록 초기화
        for(String user : id_list) {
            ds.put(user, new HashSet<String>());            
        }
        
        // 신고 목록을 돌며 신고받은 사람 별 신고자 목록(HashSet) 작성
        for(String str : report) {
            String[] a = str.split(" ");            
            ds.get(a[1]).add(a[0]);
        }
        
        // 신고 받은 사람 신고수가 k를 넘을 때 신고 한 사람 카운트 증가
        for(Entry<String, Set<String>> e : ds.entrySet()) {
            
            Set<String> s = (HashSet<String>)e.getValue();
            Iterator<String> it = s.iterator();
            
            if (s.size() >= k) {
                while(it.hasNext()) {
                    String str = it.next();

                    for(int j = 0; j < id_list.length; j++) {
                        if(id_list[j].equals(str))
                            answer[j]++;
                    }
                }
            }
        }        
        
        return answer;
    }
}