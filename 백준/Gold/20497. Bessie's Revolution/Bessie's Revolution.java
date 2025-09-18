import java.io.*;
import java.util.*;

public class Main {

    int[] dx = new int[]{1, -1, 0, 0};
    int[] dy = new int[]{0, 0, 1, -1};


    public static int count(boolean[][] visited, int N, int cnt) {
        
        Deque<int[]> cur = new ArrayDeque<>();

        int[] dx = new int[]{1, -1, 0, 0};
        int[] dy = new int[]{0, 0, 1, -1};

        for (int i = 0; i<N; i++) {
            for (int j = 0; j<N; j++) {
                if (visited[i][j] == true) {
                    int[] xy = new int[2];
                    xy[0] = i;
                    xy[1] = j;

                    
                    cur.add(xy);
                    while (!cur.isEmpty()) {
                        int[] cx_cy = cur.poll();
                        visited[cx_cy[0]][cx_cy[1]] = false;
                        
                        for (int k = 0; k<4; k++) {
                            int ny = cx_cy[0] + dy[k]; 
                            int nx = cx_cy[1] + dx[k];

                            if (0 <= nx && nx < N && 0<=ny && ny<N && visited[ny][nx]) {
                                cur.add(new int[]{ny, nx});
                            }
                        }
                    }

                    cnt++;
                }
            }
        }

        // System.out.println("cnt : "+cnt);
        return cnt;

    }

    public static int check(boolean[][] board, int y, int x, int N) {

        boolean[][] visited = new boolean[N][N];
        for (int i = 0; i<N; i++) {
            visited[i] = board[i].clone();
        }
        
        int[] dx = new int[]{1, -1, 0, 0};
        int[] dy = new int[]{0, 0, 1, -1};

        int[] xy = new int[2];
        xy[0] = y;
        xy[1] = x;

        int cnt = 0;

        for (int k = 0; k<4; k++) {
            int ny = y + dy[k]; 
            int nx = x + dx[k];

            if (0 <= nx && nx < N && 0<=ny && ny<N && visited[ny][nx]) {
                cnt++;
            }
        }

        visited[y][x] = false;

        int c;
        if (cnt == 0) {
            c = count(visited, N, 1);
        }
        else {
            c = count(visited, N, 0);
        }
        
        return c;

    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());

        boolean[][] visited = new boolean[N][N];


        for (int i = 0; i<N; i++) {
            st = new StringTokenizer(br.readLine());

            String row = st.nextToken().strip();

            char[] x = row.toCharArray();
            for (int j = 0; j<N; j++) {
                if (x[j] == '.') visited[i][j] = true;
                else visited[i][j] = false;
            }
        }

        boolean[][] board = new boolean[N][N];
        for (int i = 0; i<N; i++) {
            board[i] = visited[i].clone();
        }

        int init = count(board, N, 0);

        // System.out.println("init : "+init);
        int cnt = 0 ;

        // for (int i = 0; i<N; i++) {
        //     System.out.println(Arrays.toString(visited[i]));
        // }

        for (int i = 0; i<N; i++) {
            for (int j = 0; j<N; j++) {
                if (visited[i][j] == true) {
                    if (check(visited, i, j, N) != init) cnt++;
                }
            }
        }

        System.out.println(cnt);
    }
}