import java.io.*;
import java.util.*;

public class Main {

    static int ans;
    static int types;
    static List<int[]> coins = new ArrayList<>();
    static int[] coinType;
    static int[] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        ans = Integer.parseInt(st.nextToken());
        types = Integer.parseInt(br.readLine());

        coinType = new int[types];
        dp = new int[ans+1];
        
        for (int i = 0; i < types; i++) {
            st = new StringTokenizer(br.readLine());
            int type = Integer.parseInt(st.nextToken());
            int cnt = Integer.parseInt(st.nextToken());

            coins.add(new int[]{type, cnt});
        }

        dp[0] = 1;

        for (int[] coin : coins) {
            int val = coin[0];
            int cnt = coin[1];

            for (int i = ans; i>=0; i--) {
                for (int j = 1; j<=cnt; j++) {
                    if ((i - val * j) >= 0) 
                        dp[i] += dp[i - (val*j)];
                    
                }
            }
        }
        // System.out.println(Arrays.toString(dp));
        System.out.println(dp[ans]);
    }

}