import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());

        StringBuilder sb = new StringBuilder();

        for (int i = 1; i<=N; i++) {
            for (int j = 0; j<2; j++) sb.append(i+" ");
        }

        for (int i = 1; i<N-1; i++) {
            for (int j = i+2; j<=N; j++) {
                sb.append(i+" "+j+" ");
            }
        }

        for (int i = N-1; i>0; i--) {
            sb.append(i+" ");
        }

        System.out.println(N*N+1);
        System.out.println(sb);
    }
}