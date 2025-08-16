import java.util.*;
import java.io.*;

public class Main {
    static int N;
    static int[] target;
    static int[][] foods;
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        target = new int[4];

        N = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i<4 ; i++) {
            target[i] = Integer.parseInt(st.nextToken());
        }

        foods = new int[N][5];
        for (int i = 0; i<N ; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j<5 ; j++) {
                foods[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int res = 0;
        int min_price = 1<<13;
        
        for (int mask = 1; mask<(1<<N) ; mask++) {
            int a = 0, b = 0, c = 0, d = 0, e = 0;

            for (int i = 0; i<N ; i++) {
                if ((mask & (1<<i)) != 0) {
                    a += foods[i][0];
                    b += foods[i][1];
                    c += foods[i][2];
                    d += foods[i][3];
                    e += foods[i][4];
                }
            }
            if (a >= target[0] && b >= target[1] && c >= target[2] && d>= target[3]) {
                if (e < min_price) {
                    min_price = e;
                    res = mask;
                }
                else if (e == min_price) {
                    // 사전순 비교
                    if (isLexSmaller(mask, res)) {
                        res = mask;
                    }
                }

            }
        }
        

        if (min_price == 1<<13) {
            System.out.println(-1);
        }
        else {
            System.out.println(min_price);            
            for (int i = 0; i<N ; i++) {
                if ((res & (1<<i)) != 0) {
                    System.out.print((i+1)+" ");
                }
            }
            System.out.println();
        }
    }
    
    // 리스트 사전순 비교
    static boolean isLexSmaller(int a, int b) {
        List<Integer> a_List = new ArrayList<>();
        List<Integer> b_List = new ArrayList<>();

        for (int i = 0; i<N; i++) {
            if ((a & (1<<i)) != 0) {
                a_List.add(i + 1);
            }
            if ((b & (1<<i)) != 0) {
                b_List.add(i + 1);
            }
        }

        for (int i = 0; i < Math.min(a_List.size(), b_List.size()); i++) {
            if (!a_List.get(i).equals(b_List.get(i))) {
                return a_List.get(i) < b_List.get(i);
            }
        }
        return a_List.size() < b_List.size();
    }
}
