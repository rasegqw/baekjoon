import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] argv) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());

        HashMap<Integer, Long> route = new HashMap<>();

        for (int i = 0; i<N; i++) {
            st = new StringTokenizer(br.readLine());

            int X = Integer.parseInt(st.nextToken());
            int T = Integer.parseInt(st.nextToken());
            long C = Long.parseLong(st.nextToken());

            if (route.keySet().contains(X-T)) {
                C += route.get(X-T);
                route.put(X-T, C);
            } else {
                route.put(X-T, C);
            }
        }
        // System.out.println(route.toString());
        long max = 0;

        for (Map.Entry<Integer, Long> entry : route.entrySet()) {
            max = Math.max(max, entry.getValue());
        }

        System.out.println(max);
    }
}