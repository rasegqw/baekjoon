import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        
        if (N < 8) {
            System.out.println(-1);
        }

        // find sosu
        List<Integer> Sosu = new ArrayList<>();
        Sosu.add(2);
        Sosu.add(3);
        Sosu.add(5);
        Sosu.add(7);

        for (int i = 10; i<N-4; i++) {
            int lastThing = (int)Math.sqrt(i);
            boolean sosuFlag = true;
            for (int j = 2; j<=lastThing; j++) {
                if (i%j == 0) sosuFlag = false;
            }

            if (sosuFlag) Sosu.add(i);
        }

        // System.out.println(Arrays.toString(Sosu.toArray()));
        int len = Sosu.size();
        int p = 0;
        if (N % 2 == 0) p = 4;
        else p = 5;

        for (int i = 0; i<len; i++) {
            for (int j = 0; j<len; j++) {
                if (N - p == Sosu.get(i)+Sosu.get(j)) {
                    if (p == 4) System.out.println("2 2 "+Sosu.get(i)+" "+Sosu.get(j));
                    else System.out.println("2 3 "+Sosu.get(i)+" "+Sosu.get(j));
                    return;
                }
            }
        }

        System.out.println(-1);
    }
}