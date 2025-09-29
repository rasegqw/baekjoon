import java.io.*;
import java.util.*;

public class Main {
    static int[] rocks;
    static int[] visited;
    static int start;
    static int end;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        rocks = new int[N];
        st = new StringTokenizer(br.readLine());

        for (int i = 0; i<N; i++) {
            rocks[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        start = Integer.parseInt(st.nextToken())-1;
        end = Integer.parseInt(st.nextToken())-1;

        visited = new int[N];
        for (int i = 0; i<N; i++) {
            visited[i] = -1;
        }

        Queue<Integer> target = new LinkedList<>();

        for (int i = start%rocks[start]; i<N; i+=rocks[start]) {
            visited[i] = 1;
            target.add(i);
        }

        while (!target.isEmpty()) {
            int x = target.poll();
            
            for (int i = x%rocks[x]; i<N; i+=rocks[x]) {
                
                if (visited[i] == -1) {
                    visited[i] = visited[x] + 1;
                    target.add(i);
                }
            }
        }

        System.out.println(visited[end]);        
    }
}