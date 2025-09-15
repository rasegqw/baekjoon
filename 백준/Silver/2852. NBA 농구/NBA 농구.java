import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());

        int[] scores = new int[2];
        int[] leadTime = new int[3];

        int lastTime = 0;

        st = new StringTokenizer(br.readLine());

        int team = Integer.parseInt(st.nextToken());
        String[] Time = st.nextToken().split(":");

        int lead = team;

        scores[team-1]++;
        lastTime += Integer.parseInt(Time[0])*60 + Integer.parseInt(Time[1]);

        for (int i = 0; i<N-1; i++) {
            st = new StringTokenizer(br.readLine());

            team = Integer.parseInt(st.nextToken());
            Time = st.nextToken().split(":");

            scores[team-1] ++;

            int min = Integer.parseInt(Time[0]);
            int sec = Integer.parseInt(Time[1]);

            int dt = min*60 + sec;

            if (scores[0] == scores[1]) {
                leadTime[lead] += dt - lastTime;
                lead = 0;
            } else {
                if (scores[0] > scores[1]) {
                    leadTime[lead] += dt - lastTime;
                    lead = 1;
                } else {
                    leadTime[lead] += dt - lastTime;
                    lead = 2;
                }
            }
            lastTime = dt;

            // System.out.println(Arrays.toString(leadTime));
        }

        leadTime[lead] += 48*60 - lastTime;

        // System.out.println(Arrays.toString(leadTime));

        StringBuilder sb = new StringBuilder();

        if (leadTime[1]/60 < 10) sb.append("0"+leadTime[1]/60+":");
        else sb.append(leadTime[1]/60+":");
        if (leadTime[1]%60 < 10) sb.append("0"+leadTime[1]%60);
        else sb.append(leadTime[1]%60);

        System.out.println(sb);

        sb = new StringBuilder();

        if (leadTime[2]/60 < 10) sb.append("0"+leadTime[2]/60+":");
        else sb.append(leadTime[2]/60+":");
        if (leadTime[2]%60 < 10) sb.append("0"+leadTime[2]%60);
        else sb.append(leadTime[2]%60);

        System.out.println(sb);

    }
}
