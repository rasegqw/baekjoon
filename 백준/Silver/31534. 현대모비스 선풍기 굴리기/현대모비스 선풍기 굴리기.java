import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        double a = Integer.parseInt(st.nextToken());
        double b = Integer.parseInt(st.nextToken());
        double h = Integer.parseInt(st.nextToken());

        // System.out.println("h : "+ h);
        if (a>b) {
            double c = b;
            b = a;
            a = c;
        }
        // 큰 원의 반지름 구해서, 작은 원 빼주면 됨.
        double AREA = 0;
        double area = 0;

        if (a == 0) {
            AREA = b*b + h*h;
        }
        else if (a == b) {
            System.out.println(-1);
            return;
        }
        else {
            double small_h = (h/(b-a))*a;

            // System.out.println(h);
            // System.out.println(b-a);
            // System.out.println(h/(b-a));
            // System.out.println(small_h);

            area = small_h*small_h + a*a;
            AREA = b*b + (h+small_h)*(h+small_h);
            // System.out.println("area, AREA : "+area+" "+AREA);
        }

        System.out.printf("%.7f", AREA*Math.PI - area*Math.PI);
    }
}