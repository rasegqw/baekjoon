import java.io.*;
import java.util.*;

public class Main {

    public static int[] findMinMidMax(int x, int y, int z) {
        int[] res = new int[3];

        if (x > y) {
            if (x > z) {
                if (y > z) {
                    res[0] = z;
                    res[1] = y;
                    res[2] = x;
                } else {
                    res[0] = y;
                    res[1] = z;
                    res[2] = x;
                }
            } else {
                res[0] = y;
                res[1] = x;
                res[2] = z;
            }
        } else {
            if (y > z) {
                if (x > z) {
                    res[0] = z;
                    res[1] = x;
                    res[2] = y;
                } else {
                    res[0] = x;
                    res[1] = z;
                    res[2] = y;
                }
            } else {
                res[0] = x;
                res[1] = y;
                res[2] = z;
            }
        }
        return res;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int T = Integer.parseInt(st.nextToken());

        for (int i = 0; i<T; i++) {
            st = new StringTokenizer(br.readLine());

            int N = Integer.parseInt(st.nextToken());
            int[] dots = new int[N];

            int cnt = 0;

            st = new StringTokenizer(br.readLine());
            for (int j = 0; j<N; j++) dots[j] = Integer.parseInt(st.nextToken());

            Arrays.sort(dots);

            Set<Integer> midVal = new HashSet<>();

            for (int j = 1; j<N-1; j++) {
                midVal.add(dots[j]*2);
            }

            for (int left = 0; left<N-2; left++) {
                for (int right = left+2; right<N; right++) {
                    if (midVal.contains(dots[left] + dots[right])) cnt++;
                }
            }

            System.out.println(cnt);
        }
    }
}