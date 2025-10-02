import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        long[][] dp = new long[n][m];

        for (int i = 0; i<n; i++) {
            dp[i][0] = 1;
        }
        for (int i = 1; i<m; i++) {
            dp[0][i] = 1;
        }
        
        for (int i = 0; i<n-1; i++) {
            for (int j = 0; j<m-1; j++) {
                dp[i+1][j+1] = dp[i][j]%1000000007 
                                + dp[i+1][j]%1000000007 
                                + dp[i][j+1]%1000000007;
            }
        }

        long ans = (dp[n-1][m-1])%1000000007;

        System.out.println(ans);
    }
}