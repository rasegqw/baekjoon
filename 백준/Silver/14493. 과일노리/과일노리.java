import java.io.*;
import java.util.*;

public class Main {
    // 1 1 1 1  1
    // 1 0 1 1  2
    // 1 0 1 1  3
    // 1 0 0 1  4
    // 1 0 0 0  5
    // - 1 0 0  6
    // 0 - 1 0  7
    // 0 0 1 0  8
    // 0 0 1 0  9
    // 0 0 - 0  10
    // 0 0 0 1  11
    // 대략 이런식의 흐름이다.
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int N = Integer.parseInt(st.nextToken());
        // System.out.println(N);
        
        // 사용할 수 있는 리스트 종류는 ArrayList, LinkedList 두가지 있음.
        // ArrayList는 그냥 List, LinkedList는 연결리스트
        List<int[]> A = new ArrayList<>();

        for (int i = 0 ; i < N ; i++) {
            st = new StringTokenizer(br.readLine());
            
            int bot_interval = Integer.parseInt(st.nextToken());
            int bot_time = Integer.parseInt(st.nextToken());
            
            int[] bot = new int[2];
            bot[0] = bot_interval;
            bot[1] = bot_time;
            
            A.add(bot);
            // System.out.println(Arrays.toString(bot));
            // System.out.println(A.stream().map(Arrays::toString).toList());
        }

        int time = 0;
        time += A.get(0)[1] + 1;
        int cnt = 1;
        int i = 1;
        // System.out.println(cnt+" "+time);
        while (cnt < N) {

            if (time < i * (A.get(cnt)[0] + A.get(cnt)[1]) && 
            time >= i * (A.get(cnt)[0] + A.get(cnt)[1]) - A.get(cnt)[0]) {
                cnt ++;
                time ++;
                i = 1;
            } else if (time < A.get(cnt)[1]) {
                time = A.get(cnt)[1];
            } else {
                i ++;
                if (time < (i-1) * (A.get(cnt)[0] + A.get(cnt)[1]) + A.get(cnt)[1]) {
                    time = (i-1) * (A.get(cnt)[0] + A.get(cnt)[1]) + A.get(cnt)[1];
                }
            }
            // System.out.println(cnt+" "+time);
        }

        System.out.println(time);
    }
}


// 1 1 1    1
// - 0 0    2
// 1 1 1    3
// 0 - 0    4
// 1 1 1    5
// 0 0 -    6

// 1 1 1    1
// - 1 1    2
// 1 1 1    3
// 0 - 0    4
// 1 1 1    5
// 0 1 1    6
// 1 1 1    7
// 0 0 -    8

