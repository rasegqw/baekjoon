import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        
        String[] targets = new String[N];
        int[] targetLen = new int[N];
        int[] targetNumSum = new int[N];

        for (int i = 0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            String x = st.nextToken().strip();

            targets[i] = x;
            int len = x.length();
            int sum = 0;

            targetLen[i] = len;
            char[] cArray = x.toCharArray();

            // '0' = 48, '9' = 57
            for (char c : cArray) {
                if (47 < c && 58 > c) {
                    sum += c-48;
                    // System.out.println(sum);
                }
            }
            targetNumSum[i] = sum;
        }
        
        List<Integer> ans = new ArrayList<>();

        for (int j = 0; j < targets.length; j++) {
            ans.add(j);
        }

        ans.sort((a, b) -> {
            if (targetLen[a] != targetLen[b]) {
                return Integer.compare(targetLen[a], targetLen[b]);
            } else {
                if (targetNumSum[a] != targetNumSum[b]) {
                    return Integer.compare(targetNumSum[a], targetNumSum[b]);
                } else {
                    for (int i = 0; i<targetLen[a]; i++) {
                        // System.out.println(i);
                        if (targets[a].charAt(i) != targets[b].charAt(i)) {
                            return Integer.compare(targets[a].charAt(i), targets[b].charAt(i));
                        }
                    }
                    return 0;
                }
            }
        });

        for (int j : ans) {
            // System.out.println(j);
            System.out.println(targets[j]);
        }
    }
}