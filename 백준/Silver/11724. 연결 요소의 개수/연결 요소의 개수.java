import java.util.*;
import java.util.stream.*;
import java.io.*;

public class Main {

    public static int[] UnionFind(int[] union, int n1, int n2) {
        int x = union[n1-1];
        int y = union[n2-1];
        
        if (x != y) {
            for (int j = 0; j<union.length; j++) {
                if (union[j] == y) {
                    union[j] = x;
                }
            }
        }

        return union;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        // union - find 사용
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int[] union = new int[N];

        for (int i = 0; i<N ; i++) {
            union[i] = i + 1;
        }

        for (int i = 0; i < M ; i++) {
            st = new StringTokenizer(br.readLine());

            int[] edge = new int[2];
            edge[0] = Integer.parseInt(st.nextToken());
            edge[1] = Integer.parseInt(st.nextToken());

            if (edge[0] < edge[1]) {
                union = UnionFind(union, edge[0], edge[1]);
            }
            else {
                union = UnionFind(union, edge[1], edge[0]);
            }
        }
        // System.out.println(edges.stream().map(Arrays::toString).toList());

        // StringBuilder res = new StringBuilder();

        // for (int i = 0; i<N; i++) {
        //     res.append(union[i]+" ");

        // }
        // System.out.println(res);

        Set<Integer> res_set = Arrays.stream(union).boxed().collect(Collectors.toSet());
        System.out.println(res_set.size());
    }
    
}