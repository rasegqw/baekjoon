import java.io.*;
import java.util.*;

public class Main {

    public static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int T = Integer.parseInt(st.nextToken());

        for (int i = 0; i<T; i++) {
            st = new StringTokenizer(br.readLine());

            long min = Long.parseLong(st.nextToken());
            long max = Long.parseLong(st.nextToken());

            tournament(min, max);
        }

        System.out.println(sb);
    }

    public static void tournament(long min, long max) {

        int start = 63 - Long.numberOfLeadingZeros(min);
        int end = 63 - Long.numberOfLeadingZeros(max);

        if (start != end) {
            sb.append(0).append("\n");
            return;
        }

        if (min == (1L << start)) {
            sb.append(0).append("\n");
            return;
        }

        long target = (1L << start);        
        
        for (int i = start; i >= 0; i--) {
            target |= (1L << i);
            
            if (target >= min && target <= max)
                break;            

            if (target < min)
                continue;

            if (target > max)
                target ^= (1L << i);
        }
        
        // System.out.println("target : "+target+" ");
        int cnt = 1;
        
        // if ((target & 1L) == 0) cnt = 1;
        // else cnt = 0;

        while ((target & 1L) == 0) {
            target = target >> 1L;
            start--;
        }

        for (int i = 0; i <= start; i++) {
            if ((target & (1L << i)) == 0) {
                cnt ++;
            }
        }
        
        sb.append(cnt).append("\n");
    }
}
