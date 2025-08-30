import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = br.readLine()) != null) {
            StringTokenizer st = new StringTokenizer(line);
            int x = Integer.parseInt(st.nextToken());
            
            int res = 1;
            while (res < x) {
                res *= 9;
                if (res >= x) {
                    System.out.println("Baekjoon wins.");
                    break;
                }

                res *= 2;
                if (res >= x) {
                    System.out.println("Donghyuk wins.");
                    break;
                }
            }   
        }
    }
}
