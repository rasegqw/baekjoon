import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int x = Integer.parseInt(st.nextToken());

        if (x%4 == 0) {
            if (x%100 == 0) {
                if (x%400 == 0) System.out.println(1);
                else System.out.println(0);
            }
            else System.out.println(1);
        }
        else System.out.println(0);
    }
}