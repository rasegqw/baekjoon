import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int num = Integer.parseInt(st.nextToken());

        int cnt = 0;

        Deque<int[]> q = new ArrayDeque<>();
        q.add(new int[]{1, 0}); // num, cnt
        Set<Integer> visited = new HashSet<>();

        while (!q.isEmpty()) {

            int[] target = q.poll();

            int x = target[0];
            int curCnt = target[1];
            // System.out.println(x);

            if (x == num) {
                cnt = target[1];
                break;
            }

            if (visited.contains(x)) continue;
            else visited.add(x);

            if (x*3 <= num) q.add(new int[]{x*3, curCnt+1});
            if (x*2 <= num) q.add(new int[]{x*2, curCnt+1});
            if (x+1 <= num) q.add(new int[]{x+1, curCnt+1});
        }

        System.out.println(cnt);

    }
}