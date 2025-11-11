import java.io.*;
import java.util.*;

public class Main {
    static int N, M;
    static List<Integer>[] graph;
    static boolean[] visited;
    static int[] degree, cnt;
    static final int MOD = 1_000_000_007;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        graph = new List[N + 1];

        for (int i = 1; i <= N; i++) {
            graph[i] = new ArrayList<>();
        }

        visited = new boolean[N + 1];
        degree = new int[N + 1];
        cnt = new int[N + 1];
        Arrays.fill(cnt, 1);

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            graph[x].add(y);
            degree[y]++;
        }

        int answer = 0;
        Queue<Integer> q = new LinkedList<>();
        
        for (int i = 1; i <= N; i++) {
            if (degree[i] == 0) {
                q.add(i);
            }
        }

        while (!q.isEmpty()) {
            int node = q.poll();
            answer = (answer + cnt[node]) % MOD;

            Queue<Integer> subQ = new LinkedList<>();
            boolean[] visited = new boolean[N + 1];

            for (int next : graph[node]) {
                if (--degree[next] == 0) {
                    q.add(next);
                }
                if (!visited[next]) {
                    visited[next] = true;
                    subQ.add(next);
                }
            }

            while (!subQ.isEmpty()) {
                int cur = subQ.poll();
                cnt[cur] = (cnt[cur] + cnt[node]) % MOD;

                for (int next : graph[cur]) {
                    if (!visited[next]) {
                        visited[next] = true;
                        subQ.add(next);
                    }
                }
            }
        }
        System.out.println(answer);
        br.close();
    }

}