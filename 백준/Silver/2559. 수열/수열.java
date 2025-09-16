import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int cnt = Integer.parseInt(st.nextToken());

        int[] nums = new int[N];

        st = new StringTokenizer(br.readLine());

        for (int i = 0; i<N; i++) 
            nums[i] = Integer.parseInt(st.nextToken());    
        
        int left = 0;
        int max_sum = -5000;

        int sum = 0;
        for (int right = 0; right<N; right++) {
            sum += nums[right];

            if (right - left >= cnt) {
                sum -= nums[left];
                left++;
            }
            
            if (sum > max_sum && right-left == cnt-1) max_sum = sum;
        }

        System.out.println(max_sum);
    }
}