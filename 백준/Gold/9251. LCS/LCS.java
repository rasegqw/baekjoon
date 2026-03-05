import java.util.Arrays;
import java.util.Deque;
import java.util.Scanner;

public class Main {
    
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        char[] charArr1 = sc.nextLine().toCharArray();
        char[] charArr2 = sc.nextLine().toCharArray();
        int n1 = charArr1.length;
        int n2 = charArr2.length;
        int[][] dp = new int[n1 + 1][n2 + 1];

        for (int j = 1; j <= n2; j++) {
            for (int i = 1; i <= n1; i++) {

                if (charArr2[j - 1] == charArr1[i - 1]) {
                    dp[i][j] = Math.max(dp[i - 1][j - 1] + 1, dp[i - 1][j]);
                } else {
                    dp[i][j] = Math.max(dp[i][j - 1], dp[i - 1][j]);
                }
            }
        }

        System.out.println(dp[n1][n2]);
    }
}
