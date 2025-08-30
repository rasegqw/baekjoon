import java.io.*;
import java.util.*;

public class Main {
    public static int calculateMonthToDay(int s_m, int diff_month) {
        
        // System.out.println(s_m + " " +diff_month);
        if (diff_month == 0) return 0;
        int res = 0;

        for (int x = s_m; x<diff_month+s_m; x++) {
            if (x == 1 || x == 3 || x == 5 || x == 7 || x == 8 ||x == 10 || x == 12) res += 31;
            else if (x == 2) res += 28;
            else res += 30;
        }
        return res;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int[] start = new int[3];
        int[] end = new int[3];
        int cnt = 0;
        int YunYear = 0;
        for (int i = 0; i<3; i++) start[i] = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i<3; i++) end[i] = Integer.parseInt(st.nextToken());
    
        // 먼저 연도 체크.
        // 연도가 1000년 넘게 차이나면 gg
        int diff_year = end[0] - start[0];
        int diff_month = end[1] - start[1];
        int diff_day = end[2] - start[2];

        
        if (diff_day < 0) {
            diff_month --;
            if (end[1] == 5 || end[1] == 7 ||
                end[1] == 10 || end[1] == 12) diff_day += 30;
            else if (end[1] == 3) diff_day += 28;
            else diff_day += 31;
        }

        if (diff_month < 0) {
            diff_year --;
            diff_month += 12;
        }

        if (diff_year >= 1000) {
            System.out.println("gg");
            return;
        }

        cnt += diff_year*365;
        // System.out.println(cnt);
        cnt += diff_day;
        // System.out.println(cnt);
        cnt += calculateMonthToDay(start[1], diff_month);
        // System.out.println(cnt);

        boolean isYun_end = false;
        boolean isYun_start = false;

        if (end[0]%4 == 0) {
            if (end[0]%100 == 0) { if (end[0]%400 == 0) isYun_end = true;}
            else isYun_end = true;
        }

        if (start[0]%4 == 0) {
            if (start[0]%100 == 0) { if (start[0]%400 == 0) isYun_start = true; }
            else isYun_start = true;
        }

        YunYear += end[0]/4 - start[0]/4;
        YunYear -= end[0]/100 - start[0]/100;
        YunYear += end[0]/400 - start[0]/400;
        // System.out.println(YunYear);
        
        if (isYun_end && end[1] < 3) 
            YunYear--;
        if (isYun_start && start[1] < 3) 
            YunYear++;

        cnt += YunYear;

        // System.out.println(YunYear);
        System.out.println("D-"+cnt);
    
    }
}