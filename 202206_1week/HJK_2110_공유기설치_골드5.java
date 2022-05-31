import java.util.Arrays;
import java.util.Scanner;

public class HJK_2110_공유기설치_골드5 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int nHouse = sc.nextInt();
        int nWifi = sc.nextInt();
        int[] aLoc = new int[nHouse];

        for (int i = 0; i < nHouse; i++) {
            aLoc[i] = sc.nextInt();
        }

        Arrays.sort(aLoc);
        // 최소 거리는 1이고, 최대 거리는 마지막 집 - 첫집 이다.
        int begin = 1, end = aLoc[aLoc.length - 1] - aLoc[0];
        int middle, answer = 1;

        // 찾고자 하는 최대거리를 이진탐색 해 가며 맞는 조건을 찾는다
        while (begin <= end) {
            middle = (end + begin) / 2;

            if (isPass(middle, nWifi, aLoc) == true) {
                // 통과 시 더 큰 값(최대)을 찾아본다
                begin = middle + 1;
                // 답을 일단 저장해둔다
                answer = middle;
            } else {
                // 더 작은 값을 찾아본다
                end = middle - 1;
            }
        }

        System.out.println(answer);
    }

    private static boolean isPass(int minDist, int nWifi, int[] aLoc) {
        int prevLoc = aLoc[0];
        int distance = 0;
        int cntWifi = nWifi - 1;
        boolean bResult = false;
        
        // 첫 집 부터 wifi 를 놓고 minDist 보다 큰 거리에 있는 집에 하나씩 놓아가며 
        // 전체 wifi 를 놓았을 때 주어진 minDist 가능한지를 확인한다
        for (int i = 1; i < aLoc.length; i++) {
            // 현재 집의 위치 - wifi 놓은 이전 집 거리가 minDist 를 만족하는지 체크
            distance = aLoc[i] - prevLoc;

            if (distance >= minDist) {
                prevLoc = aLoc[i];
                cntWifi--;
            }

            if (cntWifi == 0) {
                bResult = true;
                // 공유기를 성공적으로 다 놓았으면 minDist 가 가능하므로 나간다
                break;
            }
        }

        return bResult;
    }
}
