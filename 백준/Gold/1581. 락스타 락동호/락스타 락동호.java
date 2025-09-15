import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int[] FF_FS_SF_SS = new int[4];

        for (int i = 0; i<4; i++) FF_FS_SF_SS[i] = Integer.parseInt(st.nextToken());

        int max_cnt = 0;

        if (FF_FS_SF_SS[0] == 0 && FF_FS_SF_SS[1] == 0) {
            max_cnt += FF_FS_SF_SS[3];
            if (FF_FS_SF_SS[2] != 0) max_cnt += 1;
        } else if (FF_FS_SF_SS[1] == 0) {
            max_cnt += FF_FS_SF_SS[0];
        } else {
            max_cnt += FF_FS_SF_SS[0] + FF_FS_SF_SS[3];
            if (FF_FS_SF_SS[1] > FF_FS_SF_SS[2]) {
                max_cnt += FF_FS_SF_SS[2] * 2 + 1; 
            }
            else {
                max_cnt += FF_FS_SF_SS[1] * 2; 
            }
        }
        
        System.out.println(max_cnt);
    }
}