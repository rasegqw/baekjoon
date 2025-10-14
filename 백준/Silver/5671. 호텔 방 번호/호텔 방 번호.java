import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();

        while (line != null) {
            StringTokenizer st = new StringTokenizer(line);

            int A = Integer.parseInt(st.nextToken());
            int B = Integer.parseInt(st.nextToken());
            
            // System.out.println(A+" "+B);
            
            int cnt = 0;
            
            for (int i = A; i<=B; i++) {
                String x = Integer.toString(i);
                char[] c = x.toCharArray();
                boolean flag = true;

                Set<Character> set = new HashSet<>();
                
                for (char t:c) {
                    if (set.contains(t)) {
                        flag = false;
                        break;
                    } else {
                        set.add(t);
                    }
                }
                
                if (flag) cnt++;
            }

            System.out.println(cnt);
            line = br.readLine();
            
        }
    }
}