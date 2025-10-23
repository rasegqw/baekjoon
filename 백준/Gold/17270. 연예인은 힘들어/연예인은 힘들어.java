import java.io.*;
import java.util.*;

public class Main {

    static class Node implements Comparable<Node> {
        int to, cost;
        Node(int to, int cost) {
            this.to = to;
            this.cost = cost;
        }
        public int compareTo(Node o) {
            return this.cost - o.cost;
        }
    }

    static final int INF = 1_000_000_000;
    static int V, M;
    static List<Node>[] graph;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        V = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        graph = new ArrayList[V + 1];
        for (int i = 1; i <= V; i++) graph[i] = new ArrayList<>();

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            graph[a].add(new Node(b, c));
            graph[b].add(new Node(a, c));
        }

        st = new StringTokenizer(br.readLine());
        int J = Integer.parseInt(st.nextToken());
        int S = Integer.parseInt(st.nextToken());

        if (J == S) System.out.println(-1);
        else {
        int[] distJ = dijkstra(J);
        int[] distS = dijkstra(S);

        int minSum = INF;
        for (int i = 1; i <= V; i++) {
            if (i == J || i == S) continue;
            if (distJ[i] == INF || distS[i] == INF) continue;
            minSum = Math.min(minSum, distJ[i] + distS[i]);
        }

        int answer = -1;
        int bestJ = INF;

        for (int i = 1; i <= V; i++) {
            if (i == J || i == S) continue;
            if (distJ[i] == INF || distS[i] == INF) continue;

            // 최소 합이 아니면 제외
            if (distJ[i] + distS[i] != minSum) continue;
            // 지헌이가 늦으면 제외
            if (distJ[i] > distS[i]) continue;

            // 조건 4: 지헌이가 더 빨리 오거나 번호가 작은 장소
            if (distJ[i] < bestJ || (distJ[i] == bestJ && (answer == -1 || i < answer))) {
                bestJ = distJ[i];
                answer = i;
            }
        }

        System.out.println(answer);
    }
    }

    static int[] dijkstra(int start) {
        int[] dist = new int[V + 1];
        Arrays.fill(dist, INF);
        dist[start] = 0;

        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.add(new Node(start, 0));

        while (!pq.isEmpty()) {
            Node cur = pq.poll();
            if (cur.cost > dist[cur.to]) continue;

            for (Node next : graph[cur.to]) {
                int newCost = cur.cost + next.cost;
                if (newCost < dist[next.to]) {
                    dist[next.to] = newCost;
                    pq.add(new Node(next.to, newCost));
                }
            }
        }

        return dist;
    }
}
