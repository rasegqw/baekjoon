import java.io.*;
import java.util.*;

public class Main {

    static boolean[] visited;
    static String[] cards;
    static Set<String> lay_card;
    static int K;
    static int N;
    
    public static void dfs(String lay, int cnt) {
        
        if (cnt == K) {
            lay_card.add(lay);
            return;
        }
        
        for (int i = 0; i<N; i++) {
            
            if (visited[i] == false) {
                visited[i] = true;
                dfs(lay + cards[i], cnt+1);
                visited[i] = false;
            }

        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        K = Integer.parseInt(st.nextToken());

        visited = new boolean[N];
        cards = new String[N];

        for (int i = 0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            cards[i] = st.nextToken(); 
        }

        lay_card = new HashSet<>();
        
        String x = "";

        dfs(x, 0);

        System.out.println(lay_card.size());
    }
}