import java.io.*;
import java.util.*;

public class Main {

    public static long cntMatch(int N, int M, int k, int D) {
        long league_cnt = 0;
        long another_league_cnt = (long)(Math.pow(M, 2));

        if ((N-1)%2 == 0) {
            another_league_cnt *= N*((N-1)/2);
        } else {
            another_league_cnt *= N*((N-1)/2) + N/2;
        }

        long min_res = 0;
        long res = 0;

        if ((M-1)%2 == 0) {
            league_cnt = M * ((M-1)/2);
        }
        else {
            league_cnt = M * ((M-1)/2) + M/2;
        }
        
        // System.out.println("L,A : "+league_cnt+" "+another_league_cnt);
        
        long B = 1;
        long A = k * B;
        while (res < D) {
            res = A*league_cnt*N + B*another_league_cnt;
            if (res <= D && res > 0) min_res = res;
            else break;
            B++;
            A = k*B;
        }
        // System.out.println("B : "+(B-1));
        if (min_res == 0) min_res = -1;
        return min_res;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int C = Integer.parseInt(st.nextToken());

        for (int i = 0; i<C; i++) {
            st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());
            int k = Integer.parseInt(st.nextToken());
            int D = Integer.parseInt(st.nextToken());

            System.out.println(cntMatch(N, M, k, D));
        }
    }
}