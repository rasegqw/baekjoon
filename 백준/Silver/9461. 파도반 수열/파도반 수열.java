import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int T = Integer.parseInt(st.nextToken());
        long[] res = new long[100];
        res[0] = 1;
        res[1] = 1;
        res[2] = 1;
        res[3] = 2;
        res[4] = 2;

        for (int i = 0; i<T; i++) {
            st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            
            // if (res[N-1] != 0) System.out.println(res[N-1]);
            // else {
                for (int j = 5; j<N; j++) {
                    res[j] = res[j-1] + res[j-5];
                    // System.out.println(res[j]);
                }
                System.out.println(res[N-1]);
            // }

        }
    }
}