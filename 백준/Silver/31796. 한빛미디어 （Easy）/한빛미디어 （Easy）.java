import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());

        int[] prices = new int[N];

        for (int i = 0; i<N; i++) prices[i] = Integer.parseInt(st.nextToken());

        Arrays.sort(prices);
        
        // System.out.println(Arrays.toString(prices));

        int left = 0;
        int cnt = 1;

        for (int right = 0; right<N; right++) {
            
            if (prices[left]*2 <= prices[right]) {
                cnt++;
                left = right;                
            }

        }

        System.out.println(cnt);

    }
}