import java.io.*;
import java.util.*;

public class Main {

    public static int T;
    public static int A, B;
    public static int[] pizzaA, pizzaB;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        T = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        A = Integer.parseInt(st.nextToken());
        B = Integer.parseInt(st.nextToken());

        pizzaA = new int[A];
        pizzaB = new int[B];

        for (int i = 0; i < A; i++) {
            pizzaA[i] = Integer.parseInt(br.readLine());
        }
        
        for (int i = 0; i < B; i++) {
            pizzaB[i] = Integer.parseInt(br.readLine());
        }
        
        Map<Integer, Integer> pizzaASet = preSetSubSumA(T);
        Map<Integer, Integer> pizzaBSet = preSetSubSumB(T);

        int res = 0;
        
        for (int i : pizzaASet.keySet()) {
            int needB = T - i;

            if (pizzaBSet.containsKey(needB)) {
                int x = pizzaASet.get(i);
                int y = pizzaBSet.get(needB);

                res += x * y;
            }
            
        }

        System.out.println(res);
    }

    public static Map<Integer, Integer> preSetSubSumA (int t) {
        Map<Integer, Integer> res = new HashMap<>();

        for (int i = 0; i < A; i++) {
            int subSum = 0;
            for (int j = 1; j<A; j++) {
                int index = (i + j - 1) % A;

                subSum += pizzaA[index];
                if (subSum > t) break;
                
                if (res.containsKey(subSum)) res.put(subSum, res.get(subSum) + 1);
                else res.put(subSum, 1);
            }
        }

        int max = 0;

        for (int i = 0; i < A; i++) {
            max += pizzaA[i];
        }

        res.put(max, 1);
        res.put(0, 1);

        return res;
    }

    public static Map<Integer, Integer> preSetSubSumB (int t) {
        Map<Integer, Integer> res = new HashMap<>();

        for (int i = 0; i < B; i++) {
            int subSum = 0;
            for (int j = 1; j<B; j++) {
                int index = (i + j - 1) % B;

                subSum += pizzaB[index];
                if (subSum > t) break;
                
                if (res.containsKey(subSum)) res.put(subSum, res.get(subSum) + 1);
                else res.put(subSum, 1);
            }
        }

        int max = 0;

        for (int i = 0; i < B; i++) {
            max += pizzaB[i];
        }

        res.put(max, 1);
        res.put(0, 1);

        return res;
    }
}
