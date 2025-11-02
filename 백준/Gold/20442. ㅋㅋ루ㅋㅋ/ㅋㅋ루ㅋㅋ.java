import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();

        List<Integer> leftK = new ArrayList<>();
        List<Integer> rightK = new ArrayList<>();
        List<Integer> rIndex = new ArrayList<>();

        // 왼쪽 K
        int countK = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == 'K') countK++;
            else if (c == 'R') {
                leftK.add(countK);
                rIndex.add(i);
            }
        }

        // 오른쪽 K
        countK = 0;
        for (int i = s.length() - 1; i >= 0; i--) {
            char c = s.charAt(i);
            if (c == 'K') countK++;
            else if (c == 'R') {
                rightK.add(countK);
            }
        }
        Collections.reverse(rightK);

        if (rIndex.size() == 0) {
            System.out.println(0);
            return;
        }

        int l = 0, r = rIndex.size() - 1;
        int maxLen = 0;

        while (l <= r) {
            int lenR = r - l + 1;
            int minK = Math.min(leftK.get(l), rightK.get(r));
            maxLen = Math.max(maxLen, lenR + 2 * minK);

            if (leftK.get(l) < rightK.get(r)) {
                l++;
            } else if (leftK.get(l) > rightK.get(r)) {
                r--;
            } else {
                l++;
                r--;
            }
        }

        System.out.println(maxLen);
    }
}
