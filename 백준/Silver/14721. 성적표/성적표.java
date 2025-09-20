import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());

        int a;
        int b;

        int[] x = new int[N];
        int[] y = new int[N];

        for (int i = 0; i<N; i++) {
            st = new StringTokenizer(br.readLine());

            x[i] = Integer.parseInt(st.nextToken());
            y[i] = Integer.parseInt(st.nextToken());
        }

        long min_res = 1<<60;
        long res = 0;
        int ans_a = 0;
        int ans_b = 0;

        for (int i = 1; i<=100; i++) {
            for (int j = 1; j<=100; j++) {
                res = 0;

                for (int k = 0; k<N; k++) {
                    
                    long ss = y[k]-i*x[k]-j;
    
                    res += ss*ss;
                }

                if (min_res>res) {
                    // System.out.println(res+" "+i+" "+j);
                    min_res = res;
                    ans_a = i;
                    ans_b = j;
                }
            }
        }

        System.out.println(ans_a+" "+ans_b);
    }
}