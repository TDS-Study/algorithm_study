import java.util.Scanner;

public class HJK_2748_피보나치2_브론즈1{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        sc.close();

        long prev1 = 0;
        long prev2 = 1;
        long x = 0;

        if (n <= 1) {
            x = n;
        } else {

            for (int i = 2; i <= n; i++) {
                x = prev1 + prev2;
                prev1 = prev2;
                prev2 = x;
            }
        }

        System.out.println(x);
    }
}