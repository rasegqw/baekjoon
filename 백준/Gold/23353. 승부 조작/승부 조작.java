import java.io.*;
import java.util.*;

public class Main {

    static char[][] board;
    static int N;
    static int[] dx = new int[]{1, 1, 0, 1};
    static int[] dy = new int[]{0, 1, 1, -1};
    static int[][][] visited;
    static int ans = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        board = new char[N][N];
        visited = new int[N][N][4];
        List<int[]> twoPos = new ArrayList<>();

        for (int i = 0; i<N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j<N; j++) {
                board[i][j] = st.nextToken().toCharArray()[0];

                if (board[i][j] == '2') {
                    twoPos.add(new int[]{i, j});
                }
            }
        }

        if (board[0][0] == '1') {
            for (int i = 0; i<4; i++) {
                visited[0][0][i] = 1;
            }
        }

        for (int i = 1; i<N; i++) {
            if (board[i][0] == '1') {
                visited[i][0][0] = visited[i-1][0][0] + 1;
                visited[i][0][1] = 1;
                visited[i][0][2] = 1;
                visited[i][0][3] = 1;
            }
            if (board[0][i] == '1') {
                visited[0][i][0] = 1;
                visited[0][i][1] = 1;
                visited[0][i][2] = visited[0][i-1][2] + 1;
                visited[0][i][3] = 1;
            }
        }
        for (int i = 1; i<N; i++) {
            if (board[i][N-1] == '1')
                visited[i][N-1][3] = 1;
        }        

        for (int i = 1; i<N; i++) {
            for (int j = 1; j<N; j++) {
                for (int k = 0; k<4; k++) {
                    if (i-dx[k] >= 0 && i-dx[k] < N && j-dy[k] >= 0 && j-dy[k] < N && board[i][j] == '1') {
                        visited[i][j][k] = visited[i-dx[k]][j-dy[k]][k] + 1;
                    }
                }
            }
        }

        for (int i = 1; i<N; i++) {
            if (board[i][0] == '1')
                visited[i][0][3] = visited[i-1][1][3] + 1;
        }

        // for (int i = 0; i<N; i++) {
        //     StringBuilder sb = new StringBuilder();
        //     for (int j = 0; j<N; j++) {
        //         sb.append('(');
        //         for (int k = 0; k<3; k++) {
        //             sb.append(visited[i][j][k]+" ");
        //         }
        //         sb.append("), ");
        //     }
        //     System.out.println(sb);
        // }

        for (int[] xy : twoPos) {
            int x = xy[0];
            int y = xy[1];
            int result;

            for (int i = 0; i<4; i++) {
                result = 1;
                if (x-dx[i] >= 0 && y-dy[i] >= 0 && x - dx[i] < N && y - dy[i] < N && board[x-dx[i]][y-dy[i]] == '1') {
                    result += visited[x-dx[i]][y-dy[i]][i];
                }

                int nx = x + dx[i];
                int ny = y + dy[i];

                if (nx >= N || ny >= N || nx < 0 || ny < 0 ) {
                    visited[x][y][i] = result;
                    continue;
                }

                while (true) {
                    if (board[nx][ny] == '1') {
                        nx += dx[i];
                        ny += dy[i];
                        if (nx >= N || ny >= N || nx < 0 || ny < 0) {
                            result += visited[nx - dx[i]][ny - dy[i]][i];
                            break;
                        }
                    } else {
                        result += visited[nx - dx[i]][ny - dy[i]][i];
                        break;
                    }
                }
                visited[x][y][i] = result;
            }
        }

        for (int i = 0; i<N; i++) {
            for (int j = 0; j<N; j++) {
                for (int k = 0; k<4; k++)
                    if (ans < visited[i][j][k]) ans = visited[i][j][k];
            }
        }

        // for (int i = 0; i<N; i++) {
        //     StringBuilder sb = new StringBuilder();
        //     for (int j = 0; j<N; j++) {
        //         sb.append('(');
        //         for (int k = 0; k<4; k++) {
        //             sb.append(visited[i][j][k]+" ");
        //         }
        //         sb.append("), ");
        //     }
        //     System.out.println(sb);
        // }

        System.out.println(ans);
        
   }
}