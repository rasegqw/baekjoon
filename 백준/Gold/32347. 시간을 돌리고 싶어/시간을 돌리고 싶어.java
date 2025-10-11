import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());

        List<Integer> days = new ArrayList<>();

        for (int i = 1; i<=N; i++) {
            int x = Integer.parseInt(st.nextToken());

            if (x == 1) days.add(i);
        }

        // System.out.println(Arrays.toString(days.toArray()));
        int minAns = Integer.MAX_VALUE;

        int left = 1;
        int right = N;
        
        while (left < right) {
            int mid = (left+right)/2;
            int cnt = 1;
            boolean flag = true;
    
            int prev = N;
            int cur = N - mid;
    
            while (cur > 1) {
                // System.out.println("cur, cnt : "+ cur+" "+cnt);
                int idx = Collections.binarySearch(days, cur);
                if (idx < 0) idx = -idx - 1;

                int target = days.get(idx);
                
                if (target == prev) {
                    flag = false;
                    break;
                }
                prev = target;
                cur = prev - mid;
                cnt++;
            }

            if (!flag) {
                left = mid + 1;
            } else {
                // System.out.println("here");
                if (cnt > K) {
                    left = mid + 1;
                } else {
                    if (minAns > mid) minAns = mid;
                    right = mid;
                }
            }
        }

        System.out.println(minAns);
    }
}