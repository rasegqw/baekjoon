import java.io.*;
import java.util.*;

public class Main {

    public static int cntMatch(int N, int M, int k, int D) {
        int league_cnt = 0;
        int another_league_cnt = 1;

        int min_res = 0;
        int res = 0;
        for (int i = 1; i<M; i++) {
            league_cnt += i;
        }
        for (int i = 0; i<N; i++) {
            another_league_cnt *= M;
        }
        // System.out.println("L,A : "+league_cnt+" "+another_league_cnt);

        int B = 1;
        int A = k * B;
        while (res < D) {
            res = A*league_cnt*N + B*another_league_cnt;
            // System.out.println("res : "+res);
            if (res <= D) min_res = res;
            else break;
            B++;
            A = k*B;
        }
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