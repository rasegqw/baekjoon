import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int R = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        
        int[] weights = new int[N];

        for (int i = 0; i<N; i++) {
            weights[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(weights);
        
        int i = 0;
        int j = N-1;
        int cnt = 0;

        while (j>i) {
            int sum = weights[i] + weights[j];

            if (sum > R) {
                j--;
            } else {
                i++;
                j--;
                cnt++;
            }
            
        }

        System.out.println(cnt);
    }
}