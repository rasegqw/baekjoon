import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int minLen = Integer.parseInt(st.nextToken());

        Map<String, Integer> words = new HashMap<>();

        for (int i = 0; i<N; i++) {
            st = new StringTokenizer(br.readLine());

            String target = st.nextToken().strip();

            if (target.length() < minLen) {
                continue;
            }


            words.put(target, words.getOrDefault(target, 0)+1);

        }
        // System.out.println(words.toString());

        List<Map.Entry<String, Integer>> sort_words = new ArrayList<>(words.entrySet());

        sort_words.sort((e1, e2) -> {
            int cmp = e2.getValue().compareTo(e1.getValue());
            // System.out.println("cmp : "+ cmp);
            if (cmp != 0) return cmp;

            int cmpLen = Integer.compare(e2.getKey().length(), e1.getKey().length());
            
            if (cmpLen != 0) return cmpLen;
            else {
                return e1.getKey().compareTo(e2.getKey());
            }

        });

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        for (Map.Entry<String, Integer> e : sort_words) {
            bw.write(e.getKey()+"\n");
        }

        bw.flush();

    }
}