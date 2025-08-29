import java.io.*;
import java.util.*;

public class Main {

    public static int minCutCost(int N, int[] cuts) {
        int k = cuts.length;
        int[] pos = new int[k + 2];
        pos[0] = 0;
        pos[k + 1] = N;
        for (int i = 0; i < k; i++) pos[i + 1] = cuts[i];
        Arrays.sort(pos);

        // dp[i][j] = 구간 (pos[i], pos[j])를 다 자르는 최소 비용
        int[][] dp = new int[k + 2][k + 2];

        // 구간 길이를 늘려가면서 채움
        for (int len = 2; len <= k + 1; len++) {
            for (int i = 0; i + len <= k + 1; i++) {
                int j = i + len;
                dp[i][j] = Integer.MAX_VALUE;
                for (int m = i + 1; m < j; m++) {
                    dp[i][j] = Math.min(dp[i][j],
                            dp[i][m] + dp[m][j] + (pos[j] - pos[i]));
                }
                if (dp[i][j] == Integer.MAX_VALUE) dp[i][j] = 0;
            }
        }

        return dp[0][k + 1];
    }

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int[] cuts = new int[M];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i<M; i++) {
            cuts[i] = Integer.parseInt(st.nextToken());
        }

        int result = minCutCost(N, cuts);
        System.out.println(result);
    }
}