import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int t = Integer.parseInt(st.nextToken());

        for (int i = 0; i<t; i++) {
            st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int S = Integer.parseInt(st.nextToken());
            int E = Integer.parseInt(st.nextToken());

            // S와 E가 모두 끝지점인 경우.
            if ((S == 1 && E == N) || (S == N && E == 1) ) {
                System.out.println(0);
            }
            // S와 E 모두 끝지점이 아닌 경우.
            else if (S != 1 && S != N && E != 1 && E != N) {
                // S와 E가 인접한 경우
                int big;
                int small;
                if (S > E) {
                    big = S;
                    small = E;
                }
                else {
                    big = E;
                    small = S;
                }
                if (big - small == 1) {
                    System.out.println(1);
                }
                // S와 E가 인접하지 않은 경우
                else {
                    System.out.println(2);
                }
            }
            // 둘 중 하나만 끝지점인 경우.
            else {
                // S가 끝지점인 경우
                if (S == 1 || S == N) System.out.println(1);
                // E가 끝지점인 경우
                else {
                    int big;
                    int small;
                    if (S > E) {
                        big = S;
                        small = E;
                    }
                    else {
                        big = E;
                        small = S;
                    }
                    if (big - small == 1) {
                        System.out.println(1);
                    }
                    // S와 E가 인접하지 않은 경우
                    else {
                        System.out.println(2);
                    }
                };
            }
        }
    }
}