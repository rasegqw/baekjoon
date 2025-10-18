import java.io.*;
import java.util.*;

public class Main {

    static int N, M, H;
    static int[] home;
    static List<int[]> milks = new ArrayList<>();
    static boolean[] visited;
    static int maxCnt = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        H = Integer.parseInt(st.nextToken());

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                int val = Integer.parseInt(st.nextToken());
                if (val == 1) home = new int[]{i, j};
                else if (val == 2) milks.add(new int[]{i, j});
            }
        }

        visited = new boolean[milks.size()];
        dfs(home[0], home[1], M, 0);

        System.out.println(maxCnt);
    }

    static void dfs(int x, int y, int hp, int cnt) {
        // 집으로 돌아올 수 있다면 최댓값 갱신
        if (distance(x, y, home[0], home[1]) <= hp)
            maxCnt = Math.max(maxCnt, cnt);

        for (int i = 0; i < milks.size(); i++) {
            if (visited[i]) continue;

            int nx = milks.get(i)[0];
            int ny = milks.get(i)[1];

            int dist = distance(x, y, nx, ny);
            if (hp < dist) continue; // 도달 불가

            visited[i] = true;
            dfs(nx, ny, hp - dist + H, cnt + 1);
            visited[i] = false;
        }
    }

    static int distance(int x1, int y1, int x2, int y2) {
        return Math.abs(x1 - x2) + Math.abs(y1 - y2);
    }
}
