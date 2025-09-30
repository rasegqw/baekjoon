import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());

        for (int i = 0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            int R = Integer.parseInt(st.nextToken());

            int[] nums = new int[R];
            long sum = 0;

            for (int j = 0; j<R; j++) {
                nums[j] = Integer.parseInt(st.nextToken());
            }

            for (int j = 0; j<R-1; j++) {
                for (int k = j+1; k<R; k++) {
                    int a = nums[j];
                    int b = nums[k];

                    while (b != 0) {
                        if (b == 0) break;
                        else {
                            int c = b;
                            b = a%b;
                            a = c;
                        }
                    }

                    sum += a;
                }
            }
            System.out.println(sum);
        }
    }
}