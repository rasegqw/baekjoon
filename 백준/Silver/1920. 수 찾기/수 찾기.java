import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int a = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        List<Integer> a_nums = new ArrayList<>(Collections.nCopies(a, 0));
        for (int i=0 ; i<a ; i++) {
            a_nums.set(i, Integer.parseInt(st.nextToken()));
        }
        Set<Integer> a_set = new HashSet<>(a_nums);

        st = new StringTokenizer(br.readLine());
        int b = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        List<Integer> b_nums = new ArrayList<>(Collections.nCopies(b, 0));
        for (int i = 0 ; i<b ; i++) {
            b_nums.set(i, Integer.parseInt(st.nextToken()));
        }
        List<Integer> res = new ArrayList<>(Collections.nCopies(b, 0));
        for (int i = 0 ; i<b ; i++) {
            if (a_set.contains(b_nums.get(i))) {
                res.set(i, 1);
            }
            else res.set(i, 0);
        }

        for (int i = 0 ; i<b ; i++) {
            System.out.println(res.get(i));
        }
    }
}