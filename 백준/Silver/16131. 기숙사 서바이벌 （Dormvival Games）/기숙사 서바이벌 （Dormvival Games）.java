import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int A = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[] rooms = new int[N+1];

        int maxContiCnt = 0;
        int contiCnt = 0;
        int cnt = 0;

        for (int i = 1; i<=N; i++) rooms[i] = i;
        
        if ((A-1)<=B) contiCnt++;

        int[] scores = new int[N+1];

        for (int i = 1; i<M; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 1; j<=N; j++) scores[j] = Integer.parseInt(st.nextToken());

            st = new StringTokenizer(br.readLine());
            for (int j = 1; j<=N; j++) scores[j] -= Integer.parseInt(st.nextToken());

            // System.out.println("Scores: "+Arrays.toString(scores));
            for (int j = 1; j<N; j++) {
                
                int cur = scores[rooms[j]];
                int next = scores[rooms[j+1]];

                boolean flag = false;

                // 모두 점수가 0 이상인 경우, 나쁜방 점수가 2점 이상 높으면 교체,
                if (cur >= 0 && next >= 0 && next >= cur+2) flag = true;
                // 좋은 방 점수가 0 이상이고, 나빤 방 점수가 음수면 안바꿈.
                else if (cur>=0 && next<0) continue;
                // 나쁜방이 0이상이고, 좋은방이 음수면 바꿈.
                else if (cur<0 && next>=0) flag = true;
                // 둘다 음수인 경우, 나쁜방이 4점이상 높으면 바꿈.
                else if (cur<0 && next<0 && next>=cur+4) flag = true;

                if (flag) {
                    // 교체되면 좋아진 사람은 -2점, 안좋아지면 +2점
                    int x = rooms[j];
                    rooms[j] = rooms[j+1];
                    rooms[j+1] = x;

                    scores[rooms[j]] -= 2;
                    scores[rooms[j+1]] += 2;
                }
            }

            int Hong = 0;
            int Jo = 0;

            for (int j = 1; j<=N; j++) {
                if (rooms[j] == 1) Hong = j;
                else if (rooms[j] == A) Jo = j;
            }

            if ((Hong - Jo) <= B && (Hong - Jo) >= -B) {
                contiCnt++;
            } else {
                cnt+=contiCnt;
                if (maxContiCnt<contiCnt) maxContiCnt = contiCnt;
                contiCnt = 0;
            }

            // System.out.println(Arrays.toString(rooms));
            // System.out.println("Hong, Jo: "+Hong+" "+Jo);
        }

        if (contiCnt != 0) {
            cnt+=contiCnt;
            if (maxContiCnt<contiCnt) maxContiCnt = contiCnt;
        }

        System.out.println(cnt+" "+maxContiCnt);

    }
}