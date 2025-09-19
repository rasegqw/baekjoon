import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());

        int counter = 0;
        
        for (int i = N-1; i>0; i--) {
            counter++;
            if (N%i == 0) break;
        }

        System.out.println(counter);
    }
}