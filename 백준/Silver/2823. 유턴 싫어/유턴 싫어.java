import java.io.*;
import java.util.*;

public class Main {

    static int[] dx = new int[]{1, -1, 0, 0};
    static int[] dy = new int[]{0, 0, 1, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int R = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());

        boolean[][] board = new boolean[R][C];

        for (int i = 0; i<R; i++) {
            st = new StringTokenizer(br.readLine());

            String row = st.nextToken();
            char[] row_data = row.toCharArray();

            for (int j = 0; j<C; j++) {
                if (row_data[j] == '.') board[i][j] = true;
                else board[i][j] = false;
            }
        }

        boolean flag = true;

        // for (int i = 0; i<R; i++) {
        //     System.out.println(Arrays.toString(board[i]));
        // }

        for (int i = 0; i<R; i++) {
            for (int j = 0; j<C; j++) {
                if (!board[i][j]) continue;

                int cnt = 0;

                for (int n = 0; n<4; n++) {
                    int nx = j + dx[n];
                    int ny = i + dy[n];

                    // if (i==2 && j == 0) System.out.println(nx+" "+ny);
                    if (0<=nx && nx<C && 0<=ny && ny<R) {
                        if (board[ny][nx] == true) {
                            cnt++;
                        }
                    }
                }

                if (cnt == 1) {
                    // System.out.println("i, j : "+i+" "+j);
                    flag = false;
                    break;
                }
            }
        }

        if (flag) System.out.println(0);
        else System.out.println(1);
    }
}