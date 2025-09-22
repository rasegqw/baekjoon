import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());

        Map<Integer, Integer> teams = new LinkedHashMap<>();

        st = new StringTokenizer(br.readLine());
        int[] nums = new int[N];
        
        for (int i = 0; i<N; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(nums);

        for (int i = 0; i<N; i++) {
            int x = nums[i];
            if (teams.containsKey(x)) {
                int target = teams.get(x);
                teams.put(x, target+1);
            } else {
                teams.put(x, 1);
            }
        }

        // System.out.println(teams.toString());
        int cnt = 0;
        int cur = 0;

        for (Map.Entry<Integer, Integer> e : teams.entrySet()) {
            int k = e.getKey();
            int v = e.getValue();

            cur += v;
            cnt += cur/k;

            if (cur <= 0) {
                continue;
            }
            
            if (cur%k == 0) {
                cur = 0;
            } else {
                cur = cur%k - k;
                cnt ++;
            }

            // System.out.println("cnt, k, v : "+cnt+" "+k+" "+v);
            // System.out.println("cur : "+cur);
        }


        System.out.println(cnt);
    }
}