import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int[] steps = new int[N];

        Map<Integer, Set<Character>> GunBan = new HashMap<>();

        Set<Character> upDouble = new HashSet<>();
        upDouble.add('C');
        upDouble.add('D');
        upDouble.add('F');
        upDouble.add('G');
        upDouble.add('A');

        Set<Character> upOnce = new HashSet<>();
        upOnce.add('E');
        upOnce.add('B');

        Set<Character> downDouble = new HashSet<>();
        downDouble.add('D');
        downDouble.add('E');
        downDouble.add('G');
        downDouble.add('A');
        downDouble.add('B');

        Set<Character> downOnce = new HashSet<>();
        downOnce.add('C');
        downOnce.add('F');

        GunBan.put(2, upDouble);
        GunBan.put(1, upOnce);
        GunBan.put(-2, downDouble);
        GunBan.put(-1, downOnce);

        List<String> ans = new ArrayList<>();

        for (int i = 0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            steps[i] = Integer.parseInt(st.nextToken());
        }

        for (char s : new char[]{'C','D','E','F','G','A','B'}) {

            // System.out.println(s);
            char Start = s;

            char cur = s;
            boolean flag = true;

            for (int i : steps) {
                while (i != -1 &&i != -2 &&i != 2 &&i != 1) {
                    if (i<0) {
                        if (cur == 'C' || cur == 'F') {
                            cur -= 1;
                            i++;
                        } else {
                            if (cur == 'A') cur = 'G';
                            else cur -= 1;
                            i+=2;
                        }
                    } else {
                        if (cur == 'E' || cur == 'B') {
                            cur += 1;
                            i--;
                        } else {
                            if (cur == 'G') cur = 'A';
                            else cur += 1;
                            i-=2;
                        }
                    }
                }
                if (GunBan.get(i).contains(cur)) {                    
                    if (i < 0) {
                        if (cur == 'A') cur = 'G';
                        else cur -= 1;
                    } else {
                        if (cur == 'G') cur = 'A';
                        else cur += 1;
                    }
                } else {
                    flag = false;
                    break;
                }
                if (!flag) break;
            }

            if (flag) {
                char End = cur;

                ans.add(Start+" "+End);
            }
        }

        ans.sort(null);

        for (String res : ans) {
            System.out.println(res);
        }
        
    }
}