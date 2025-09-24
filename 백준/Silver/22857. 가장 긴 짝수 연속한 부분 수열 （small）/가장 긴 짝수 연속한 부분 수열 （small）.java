import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());

        // 문제 풀이 방법
        // 
        // ex) 
        // 1 2 3 4 5 6 7 8 이렇게 들어왔다면,
        // 홀수가 들어올때마다, 이전 홀수에서부터 자신까지 사이에 몇개의 짝수가 존재하는지 기록.
        // 홀수는 1, 3 ,5, 7 이므로,
        // 각각 왼쪽에 있는 짝수 개수는 0, 1, 1, 1 로 기록됨.

        // K개 만큼의 홀수를 제외시켜야되는데,
        // 수열의 길이가 길게 만드려면 연속한 홀수들을 제외시켜야 함.
        // (2개라면 1, 3 혹은 3, 5 이렇게. 1, 5 이렇게는 하면 안된다는 거.)

        // 그래서 가장 왼쪽에 있는 홀수를 left, 가장 오른쪽에 있는 홀수를 right로 두고,
        // 그 사이에 있는 짝수 개수, 즉, 아까 기록해놨던 짝수 개수를 전부 더해줌.
        // 그래서 가장 큰 수를 기록해뒀다가, 출력하면 끝.

        int even_cnt = 0;
        List<Integer> odds = new ArrayList<>();

        for (int i = 0; i<N; i++) {
            int num = Integer.parseInt(st.nextToken());

            if (num % 2 == 0) even_cnt++;
            else {
                odds.add(even_cnt);
                even_cnt = 0;
            }
        }

        int len = odds.size();
        int max_cnt = 0;

        if (len <= K) {
            max_cnt = N - len;
        }
        else {
            int left = 0;
            int ans_cnt = 0;
    
            for (int right = 0; right<len; right++) {
                ans_cnt += odds.get(right);
    
                if (right-left > K) {
                    ans_cnt -= odds.get(left);
                    left ++;    
                }

                // System.out.println("left, right : "+left+" "+right);
                if (max_cnt < ans_cnt) max_cnt = ans_cnt;
                // System.out.println(max_cnt);
            }

            ans_cnt += even_cnt;
            ans_cnt -= odds.get(left);
            
            if (max_cnt < ans_cnt) max_cnt = ans_cnt;

        }

        System.out.println(max_cnt);

        
    }
}