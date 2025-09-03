import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        long K = Long.parseLong(st.nextToken());

        st = new StringTokenizer(br.readLine());
        PriorityQueue<Long> scores = new PriorityQueue<>();

        long all_cnt = 0;
        for (int i = 0; i<N; i++) {
            Long score = Long.parseLong(st.nextToken());
            scores.add(score);
            all_cnt += score;
        }

        // System.out.println(scores.toString());
        long cnt = all_cnt;
        // System.out.println(N+" "+K+" "+cnt);
        long prev_last = 0;
        long last = 0;
        while (cnt > K) {
            Long x = scores.poll();
            cnt -= (x - last)*(scores.size() + 1);
            prev_last = last;
            last = x;
        }
        // System.out.println("cnt : "+cnt);
        long res = 0;
        while (last > prev_last && last != 0) {
            long x = (last + prev_last) / 2;
            // System.out.println(x+" "+last+" "+prev_last);

            res = cnt + (scores.size()+1)*(last - x);
            // System.out.println("res : "+res);
            if (res > K) {
                prev_last = x+1;
            }
            else {
                last = x;
                cnt = res;
            }
        }
        
        System.out.println(last);
    }
}