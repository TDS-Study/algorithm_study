import java.util.Arrays;
import java.util.Scanner;

public class HJK_3079{

    static int n;
    static long m;
    static long[] times;

    private static void getInput(){
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();
        m = sc.nextLong();
        times = new long[n];

        for(int i = 0; i < n; i++){
            times[i] = sc.nextLong();
        }

        sc.close();
    }

    public static void main(String[] args){
        getInput();

        long begin = 1;
        long end = Arrays.stream(times).max().getAsLong() * m;
        long middle = 0, minValue = 0;

        while(begin <= end){
            middle = (begin + end) / 2;

            if(check(middle)){
                end = middle - 1;
                minValue = middle;
            }
            else{
                begin = middle + 1;
            }
        }

        System.out.println(minValue);
    }

    static private boolean check(long middle){
        boolean r = false;
        long peopleCnt = m;

        for(long i : times){
            peopleCnt -= (middle / i);

            if(peopleCnt <= 0){
                r = true;
                break;
            }
        }

        return r;
    }
}