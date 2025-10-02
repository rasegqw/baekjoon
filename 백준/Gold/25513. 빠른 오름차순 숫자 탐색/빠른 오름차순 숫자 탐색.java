import java.io.*;
import java.util.*;

public class Main {

    static int[] dx = new int[]{1, -1, 0, 0};
    static int[] dy = new int[]{0, 0, 1, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int[][] board = new int[5][5];
        
        for (int i = 0; i<5; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j<5; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        boolean[][] visited = new boolean[5][5];
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] start = new int[3];
        start[0] = Integer.parseInt(st.nextToken());
        start[1] = Integer.parseInt(st.nextToken());
        start[2] = 0;

        visited[start[0]][start[1]] = true;

        Deque<int[]> q = new ArrayDeque<>();
        q.add(start);
        int target = 1;
        int ans = -1;

        while (!q.isEmpty()) {
            int[] cur = q.poll();
            if (board[cur[0]][cur[1]] == -1) continue;
            else if (board[cur[0]][cur[1]] == target) {
                if (target == 6) {
                    ans = cur[2];
                    break;
                }
                else {
                    visited = new boolean[5][5];
                    visited[cur[0]][cur[1]] = true;
                    target++;
                    q = new ArrayDeque<>();
                    q.add(cur);
                    continue;
                }
            }
            
            visited[cur[0]][cur[1]] = true;

            for (int i = 0; i<4; i++) {
                int ny = cur[0] + dy[i];
                int nx = cur[1] + dx[i];

                if (nx >= 0 && nx < 5 && ny >= 0 && ny < 5 && visited[ny][nx] == false)
                    q.add(new int[]{ny, nx, cur[2]+1});
            }
        }
        
        System.out.println(ans);
    }
}