import java.io.*;
import java.util.*;

public class Main {

    public static List<Integer> check(String s, int N, List<Integer> list) {
        
        char[] c = s.toCharArray();
        char last = ' ';
        list.clear();

        for (int i = 0; i<N; i++) {
            if (last != c[i]) {
                list.add(i);
                last = c[i];
            }
        }

        return list;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int N = Integer.parseInt(st.nextToken());
        int R = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());

        String line = st.nextToken().strip();
        // System.out.println(line);
        List<Integer> list = new ArrayList<>();

        list = check(line, N, list);

        for (int i = 0; i<R; i++) {
            st = new StringTokenizer(br.readLine());

            int type = Integer.parseInt(st.nextToken());

            int start = Integer.parseInt(st.nextToken())-1;
            int end = Integer.parseInt(st.nextToken())-1;
            
            if (type == 1) {
                int cnt = 1;
                
                for (int v : list) {
                    if (v > start && v <= end) {
                        cnt++;
                    }
                }
                System.out.println(cnt);
            }
            else {
                char[] target = line.toCharArray();

                for (int j = start; j<=end; j++) {
                    // System.out.println(target[j]);
                    if (target[j] == 'Z') target[j] = 'A';
                    else target[j] ++;
                    // System.out.println(target[j]);
                }

                line = String.copyValueOf(target);
                list = check(line, N, list);
                // System.out.println(line);
            }
        }
    }
}