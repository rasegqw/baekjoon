import java.io.*;
import java.util.*;

public class Main {
    static final char[] EVEN = {'0', '2', '4', '6', '8'};
    static final char[] ODD = {'1', '3', '5', '7', '9'};
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());

        String nums = st.nextToken();
        char[] target = nums.toCharArray();
        
        int even_cnt = 0;
        int odd_cnt = 0;

        for (int i = 0; i<N; i++) {
            odd_cnt++;
            for (char c : EVEN) {
                if (target[i] == c) {
                    odd_cnt--;
                    even_cnt++;
                    break;
                }
            }
        }
        
        if (even_cnt > odd_cnt) System.out.println(0);
        else if (even_cnt < odd_cnt) System.out.println(1);
        else System.out.println(-1);

    }
}