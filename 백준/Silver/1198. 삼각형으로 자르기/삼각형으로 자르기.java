import java.io.*;
import java.util.*;

public class Main {

    public static double calculate(int[] dot1, int[] dot2, int[] dot3) {
        double area = Math.abs(dot1[0]*dot2[1] + dot2[0]*dot3[1] + dot3[0]*dot1[1]
                    - (dot1[1]*dot2[0] + dot2[1]*dot3[0] + dot3[1]*dot1[0]));
        return area/2;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());

        int[][] dots = new int[N][2];

        for (int i = 0; i<N; i++) {
            st = new StringTokenizer(br.readLine());

            dots[i][0] = Integer.parseInt(st.nextToken());
            dots[i][1] = Integer.parseInt(st.nextToken());
        }

        double max_area = 0;

        for (int i = 0; i<N-2; i++) {
            for (int j = i+1; j<N-1; j++) {
                for (int k = j+1; k<N; k++) {
                    // System.out.println(i+" "+j+" "+k);

                    double area = calculate(dots[i], dots[j], dots[k]);

                    if (area > max_area) max_area = Math.max(area, max_area);
                }
            }
        }

        System.out.println(max_area);
    }
}