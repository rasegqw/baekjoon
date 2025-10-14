import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());

        Integer[] cakes = new Integer[N];

        for (int i = 0; i<N; i++) {
            cakes[i] = Integer.parseInt(st.nextToken());
        }


        Arrays.sort(cakes, new Comparator<Integer>() {
            @Override
            public int compare(Integer a, Integer b) {
                boolean aDiv10 = a % 10 == 0;
                boolean bDiv10 = b % 10 == 0;

                if (aDiv10 && !bDiv10) return -1;
                if (!aDiv10 && bDiv10) return 1;

                return a - b;
            }
        });

        int cakeCnt = 0;
        int cutCnt = 0;

        for(int cake : cakes) {
            if (cake == 10) cakeCnt++;
            else if (cake < 10) continue;
            else {
                if (cake % 10 != 0) {
                    cakeCnt += cake/10;
                    cutCnt += cake/10;

                    if (cutCnt > M) {
                        cakeCnt -= (cutCnt-M);
                        break;
                    }
                } else {
                    cakeCnt += cake/10;
                    cutCnt += cake/10 - 1;

                    if (cutCnt > M) {
                        cakeCnt -= (cutCnt-M)+1;
                        break;
                    }
                }
            }

            // System.out.println("cakeCnt, cutCnt : "+cakeCnt+" "+cutCnt);
        }

        System.out.println(cakeCnt);
    }
}