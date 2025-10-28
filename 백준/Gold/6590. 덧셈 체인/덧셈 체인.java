import java.io.*;
import java.util.*;

public class Main {
    static int n;
    static int bestLen;
    static List<Integer> bestChain;
    static List<Integer> curChain;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        while (true) {
            n = Integer.parseInt(br.readLine().trim());
            if (n == 0) break;
            bestLen = Integer.MAX_VALUE;
            bestChain = new ArrayList<>();
            curChain = new ArrayList<>();
            curChain.add(1);
            dfs();
            // bestChain 출력
            for (int x : bestChain) {
                System.out.print(x + " ");
            }
            System.out.println();
        }
    }

    static void dfs() {
        if (curChain.size() >= bestLen) return;  // 가지치기
        int last = curChain.get(curChain.size() - 1);
        if (last == n) {
            bestLen = curChain.size();
            bestChain = new ArrayList<>(curChain);
            return;
        }
        // 후보 생성
        int size = curChain.size();
        for (int i = size - 1; i >= 0; i--) {
            int candidate = last + curChain.get(i);
            if (candidate > n) continue;
            curChain.add(candidate);
            dfs();
            curChain.remove(curChain.size() - 1);
        }
    }
}
