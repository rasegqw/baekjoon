import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());

        Set<String> member = new HashSet<>();

        int total_cnt = 0;
        int cnt = 0;

        for (int i = 0; i<N; i++) {
            st = new StringTokenizer(br.readLine());

            String target = st.nextToken().strip();

            if (target.equals("ENTER")) {
                total_cnt += cnt;
                cnt = 0;
                member.clear();
            }
            else if (member.contains(target)) {
                continue;
            }
            else {
                member.add(target);
                cnt++;
            }

            // System.out.println(Arrays.toString(member.toArray()));
        }

        if (cnt != 0) total_cnt += cnt;

        System.out.println(total_cnt);
    }
}