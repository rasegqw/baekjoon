import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        N -= 4;
        
        Map<Integer, Integer> nums = new HashMap<Integer, Integer>(){{
            put(1, 2);
            put(2, 5);
            put(3, 5);
            put(4, 4);
            put(5, 5);
            put(6, 6);
            put(7, 3);
            put(8, 7);
            put(9, 6);
            put(0, 6);
        }};
        
        int ans1 = -1;
        int ans2 = -1;
        int ans3 = -1;

        for (int num1 = 0; num1<100; num1++) {
            int total = 0;
            for (int num2 = 0; num2<100; num2++) {
                total = 0;
                int num3 = num1 + num2;

                if (num1<10) {
                    total += nums.get(num1) + 6;
                } else {
                    total += nums.get(num1/10) + nums.get(num1%10);
                }

                if (num2<10) {
                    total += nums.get(num2) + 6;
                } else {
                    total += nums.get(num2/10) + nums.get(num2%10);
                }

                if (num3 >= 100) break;

                if (num3<10) {
                    total += nums.get(num3) + 6;
                } else {
                    total += nums.get(num3/10) + nums.get(num3%10);
                }

                if (total == N) {
                    ans1 = num1;
                    ans2 = num2;
                    ans3 = num3;
                    break;
                }
            }
            if (total == N) break;
        }

        if (ans1 != -1) {
            String res = "";
            if (ans1 < 10) {
                res += "0"+ans1+"+";
            } else {
                res += ans1 + "+";
            }

            if (ans2 < 10) {
                res += "0"+ans2+"=";
            } else {
                res += ans2 + "=";
            }

            if (ans3 < 10) {
                res += "0"+ans3;
            } else {
                res += ans3;
            }

            System.out.println(res);
        } else {
            System.out.println("impossible");
        }
    }
}