import java.io.*;
import java.math.BigInteger;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        long n = Long.parseLong(st.nextToken());
        long b = Long.parseLong(st.nextToken());

        long total_x = 0;
        long total = b*n;

        for (long i = 0; i<n; i++) {
            st = new StringTokenizer(br.readLine());
            
            total_x += Long.parseLong(st.nextToken());
            total -= Long.parseLong(st.nextToken());
        }
        
        // System.out.println("x, total : "+total_x + " " +total);
        if (total_x == 0) System.out.println("EZPZ");
        else {
            BigInteger int1 = BigInteger.valueOf(total_x);
            BigInteger int2 = BigInteger.valueOf(total);
            Long gcd = Long.parseLong(int1.gcd(int2).toString());

            // System.out.println("gcd : "+gcd);
            
            if (total % total_x != 0) {
                long A = total_x / gcd;
                long B = total / gcd;
                
                // System.out.println("A, B : "+A+B);
                if (A < 0 ^ B < 0) System.out.println(Math.abs(B)+"/"+Math.abs(A));
                else System.out.println("-"+Math.abs(B)+"/"+Math.abs(A));
                
            } else {
                long res = -total / total_x;
                System.out.println(res);
            }
        }
    }
}