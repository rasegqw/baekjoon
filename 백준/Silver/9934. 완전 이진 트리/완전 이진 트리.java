import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int K = Integer.parseInt(st.nextToken());
        int x = (int)(Math.pow(2, K) - 1);

        List<int[]> treeLevel = new ArrayList<>();
        for (int i = 0; i<K; i++) {
            int[] arr = new int[(int)Math.pow(2, i)];
            treeLevel.add(arr);
        }

        st = new StringTokenizer(br.readLine());

        for (int i = 0; i<x; i++) {
            if (i % 2 == 0) {
                int[] arr = treeLevel.get(treeLevel.size()-1);
                arr[i/2] = Integer.parseInt(st.nextToken());
            } else {
                for (int j = 1; j<K; j++) {
                    int target = (int)Math.pow(2, j+1);

                    if (i%target == ((target/2)-1)) {
                        int[] arr = treeLevel.get(K-j-1);
                        arr[i/target] = Integer.parseInt(st.nextToken());

                        break;
                    }
                }
            }
        }

        for (int[] ans : treeLevel) {
            StringBuilder sb = new StringBuilder();
            for (int a : ans) {
                sb.append(a+" ");
            }
            System.out.println(sb);
        }
    }
}