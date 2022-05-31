import java.util.Arrays;
import java.util.Scanner;

public class HJK_2110_공유기설치_골드5 {
    private void print(String str){
        System.out.println(str);
    }
    public void run(){
        Scanner sc = new Scanner(System.in);

//        int nHouse = sc.nextInt();
//        int nWifi = sc.nextInt();
//        int[] aLoc = new int[nHouse];

//
//        for ( int i = 0; i<nHouse; i++){
//            aLoc[i] = sc.nextInt();
//        }

        int nHouse = 5;
        int nWifi = 3;
        int[] aLoc = { 1, 2, 4, 9, 8};

        Arrays.sort(aLoc);

        int begin = 1, end = aLoc[aLoc.length-1] - aLoc[0];
        int middle, answer = 1;

        while(begin <= end){
            middle = (end + begin) / 2;
//
//            print("middle:" + middle);

            if( isPass(middle, nWifi, aLoc) == true){
                // 통과 시 더 큰 값을 찾아본다
                begin = middle + 1;
                answer = middle;
            }
            else {
                // 더 작은 값을 찾아본다
                end = middle - 1;
            }
        }

        System.out.println(answer);
    }

    private boolean isPass(int minDist, int nWifi, int[] aLoc){
        int offset = aLoc[0];
        int distance = 0;
        int cntWifi = nWifi - 1;
        boolean bResult = false;

        for(int i = 1; i < aLoc.length; i++){

            distance = aLoc[i] - offset;


            if(distance >= minDist){
                offset = aLoc[i];
                cntWifi--;
            }

            if(cntWifi == 0) {
                bResult = true;
//                print("pass minDist:" + minDist);
                break;
            }
        }

        return bResult;
    }
}
