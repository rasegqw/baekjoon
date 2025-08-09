import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int n = Integer.parseInt(st.nextToken());
        List<Integer> nums = new ArrayList<>(Collections.nCopies(n, 0));

        for (int i = 0;i<n;i++) {
            st = new StringTokenizer(br.readLine());
            nums.set(i, Integer.parseInt(st.nextToken()));
        }

        int cur_height = nums.remove(nums.size()-1);
        int cnt = 1;

        while (!nums.isEmpty()) {
            int last = nums.remove(nums.size()-1);

            if (last > cur_height) {
                cur_height = last;
                cnt++;
            }
        }

        System.out.println(cnt);
    }
}