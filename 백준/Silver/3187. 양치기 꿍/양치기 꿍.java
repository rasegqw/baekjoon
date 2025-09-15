import java.io.*;
import java.util.*;

public class Main {

    // . : 땅, # : 울타리, v : 늑대, k : 양
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[][] land = new int[N][M];
        char[][] all = new char[N][M];

        int[] alive = new int[2];

        for (int i = 0; i<N; i++) {
            st = new StringTokenizer(br.readLine());

            String row = st.nextToken();
            char[] target = row.toCharArray();            
            for (int j = 0; j<M; j++) {
                if (target[j] == '#') land[i][j] = -1;
            }
            all[i] = target;
        }

        int[] dx = new int[]{1, -1, 0, 0};
        int[] dy = new int[]{0, 0, 1, -1};

        Deque<int[]> q = new ArrayDeque<>();

        int idx = 0;

        for (int i = 0; i<N; i++) {
            for (int j = 0; j<M; j++) {
                if (land[i][j] == 0) {
                    q.push(new int[]{i, j});
            
                    idx ++;
                    
                    // System.out.println(i+" "+j);
                    while (!q.isEmpty()) {
                        int[] xy = q.poll();
            
                        int y = xy[0];
                        int x = xy[1];
            
                        if (land[y][x] == 0) {
                            land[y][x] = idx;
                        } else {
                            continue;
                        }
                        
                        for (int k = 0; k<4; k++) {
                            int nx = x+dx[k];
                            int ny = y+dy[k];
                            if (0 <= nx && nx < M && 0 <= ny && ny < N)
                                q.push(new int[]{y+dy[k],x+dx[k]});
                        }
                    }
                }
            }
        }
        
        // for (int i = 0; i<N; i++) {
        //     System.out.println(Arrays.toString(land[i]));
        // }

        int x = 0;
        while (x <= idx) {
            x++;
            int wolves = 0;
            int sheeps = 0;

            for (int i = 0; i<N; i++) {
                for (int j = 0; j<M; j++) {
                    if (land[i][j] == x) {
                        if (all[i][j] == 'v') {
                            wolves++;
                        } else if (all[i][j] == 'k') {
                            sheeps++;
                        }
                    }
                }
            }

            if (wolves >= sheeps) alive[1] += wolves;
            else alive[0] += sheeps;
        }
        
        System.out.println(alive[0] + " " +alive[1]);

    }
}