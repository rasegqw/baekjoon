import java.io.*;
import java.util.*;

public class Main {

    static int ALPBT_LEN = 26;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int maxN = Integer.parseInt(br.readLine());
        String password = br.readLine().strip();

        char[] passwordCharArr = password.toCharArray();
        int target = 0;
        char cur = 'a';

        long result = 0;

        while (target < password.length()) {
            if (passwordCharArr[target] == cur) {
                if (cur == 'a') {
                    target++;
                    result++;
                    continue;
                } else {
                    target++;
                    cur = 'a';
                    result++;
                    continue;
                }
            }

            if (passwordCharArr[target] != cur) {
                result += getTotal(maxN-target-1);
                cur += 1;
                // System.out.println(result+" "+cur+" "+target);
                continue;
            }

        }

        System.out.println(result);

    }

    static long getTotal(int length) {
        
        if (length == 0) return 1;
        return getTotal(length-1) * ALPBT_LEN + 1;
    }
}