import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int R = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());

        boolean[][] board = new boolean[R][C];

        for (int i = 0; i<R; i++) {
            st= new StringTokenizer(br.readLine());

            for (int j = 0; j<C; j++) {
                int x = Integer.parseInt(st.nextToken());

                if (x == 1) board[i][j] = true;
                else board[i][j] = false;
            }
        }

        st = new StringTokenizer(br.readLine());

        int rules = Integer.parseInt(st.nextToken());

        int[] dx = new int[rules];
        int[] dy = new int[rules];

        for (int i = 0; i<rules; i++) {
            st = new StringTokenizer(br.readLine());

            dx[i] = Integer.parseInt(st.nextToken());
            dy[i] = Integer.parseInt(st.nextToken());
        }


        Deque<int[]> q = new ArrayDeque<>();
        int minResult = Integer.MAX_VALUE;

        boolean[][] visited = new boolean[R][C];

        for (int i = 0; i<C; i++) {
            if (board[0][i] == true) {
                q.add(new int[]{0, i, 0});                
            }
        }

        while (!q.isEmpty()) {
            int[] cur = q.poll();

            if (visited[cur[0]][cur[1]]) continue;
            
            visited[cur[0]][cur[1]] = true;

            // System.out.println(Arrays.toString(cur));
            if (minResult <= cur[2]) continue;

            if (cur[0] == R-1 && minResult > cur[2]) {
                minResult = cur[2];
                continue;
            }


            for (int j = 0; j<rules; j++) {
                int nx = cur[0] + dx[j];
                int ny = cur[1] + dy[j];

                if (0<=nx && nx<R && 0<=ny && ny<C && board[nx][ny]==true) {
                    if (!visited[nx][ny]) q.add(new int[]{nx, ny, cur[2]+1});
                    else continue;
                }
            }
        }

        if (minResult == Integer.MAX_VALUE) System.out.println(-1);
        else System.out.println(minResult);

    }
}
