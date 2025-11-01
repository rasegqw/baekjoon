import java.io.*;
import java.util.*;

public class Main {
    static final int N = 5;
    static int[][][] MAP = new int[N][N][N];
    static int[][][] C_MAP = new int[N][N][N];
    static boolean[] used = new boolean[N];
    static int[] Maze_Order = new int[N];
    static int[] Turn_Order = new int[N];
    static boolean[][][] Visit = new boolean[N][N][N];
    static int Answer = Integer.MAX_VALUE;

    static int[] dx = {0, 0, 1, -1, 0, 0};
    static int[] dy = {1, -1, 0, 0, 0, 0};
    static int[] dh = {0, 0, 0, 0, 1, -1};

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        input();
        solution();
    }

    static void input() throws IOException {
        for (int h = 0; h < N; h++) {
            for (int i = 0; i < N; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                for (int j = 0; j < N; j++) {
                    MAP[h][i][j] = Integer.parseInt(st.nextToken());
                }
            }
        }
    }

    static void solution() {
        // 모두 0 또는 모두 1 체크
        if (checkAll(0)) {
            System.out.println(-1);
            return;
        } else if (checkAll(1)) {
            System.out.println(12);
            return;
        }

        makeMazeOrder(0);
        System.out.println(Answer == Integer.MAX_VALUE ? -1 : Answer);
    }

    static boolean checkAll(int value) {
        for (int h = 0; h < N; h++)
            for (int i = 0; i < N; i++)
                for (int j = 0; j < N; j++)
                    if (MAP[h][i][j] != value)
                        return false;
        return true;
    }

    static void makeMazeOrder(int depth) {
        if (depth == N) {
            makeTurnOrder(0);
            return;
        }
        for (int i = 0; i < N; i++) {
            if (!used[i]) {
                used[i] = true;
                Maze_Order[depth] = i;
                makeMazeOrder(depth + 1);
                used[i] = false;
            }
        }
    }

    static void makeTurnOrder(int depth) {
        if (depth == N) {
            makeMaze();
            if (C_MAP[0][0][0] == 1 && C_MAP[4][4][4] == 1) {
                int result = bfs(C_MAP);
                if (result != -1) Answer = Math.min(Answer, result);
            }
            return;
        }
        for (int t = 0; t < 4; t++) {
            Turn_Order[depth] = t;
            makeTurnOrder(depth + 1);
        }
    }

    static void makeMaze() {
        for (int h = 0; h < N; h++) {
            int idx = Maze_Order[h];
            int t = Turn_Order[h];
            C_MAP[h] = rotateLayer(MAP[idx], t);
        }
    }

    static int[][] rotateLayer(int[][] src, int times) {
        int[][] ret = new int[N][N];
        for (int i = 0; i < N; i++)
            ret[i] = Arrays.copyOf(src[i], N);

        for (int t = 0; t < times; t++) {
            int[][] tmp = new int[N][N];
            for (int i = 0; i < N; i++)
                for (int j = 0; j < N; j++)
                    tmp[j][N - 1 - i] = ret[i][j];
            ret = tmp;
        }
        return ret;
    }

    static int bfs(int[][][] A) {
        for (int h = 0; h < N; h++)
            for (int i = 0; i < N; i++)
                Arrays.fill(Visit[h][i], false);

        Queue<Node> q = new ArrayDeque<>();
        q.offer(new Node(0, 0, 0, 0));
        Visit[0][0][0] = true;

        while (!q.isEmpty()) {
            Node cur = q.poll();
            if (cur.h == 4 && cur.x == 4 && cur.y == 4)
                return cur.cnt;

            for (int i = 0; i < 6; i++) {
                int nh = cur.h + dh[i];
                int nx = cur.x + dx[i];
                int ny = cur.y + dy[i];
                if (nh < 0 || nx < 0 || ny < 0 || nh >= N || nx >= N || ny >= N) continue;
                if (!Visit[nh][nx][ny] && A[nh][nx][ny] == 1) {
                    Visit[nh][nx][ny] = true;
                    q.offer(new Node(nh, nx, ny, cur.cnt + 1));
                }
            }
        }
        return -1;
    }

    static class Node {
        int h, x, y, cnt;
        Node(int h, int x, int y, int cnt) {
            this.h = h;
            this.x = x;
            this.y = y;
            this.cnt = cnt;
        }
    }
}
