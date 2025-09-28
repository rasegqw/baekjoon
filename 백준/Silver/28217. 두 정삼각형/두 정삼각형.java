import java.io.*;
import java.util.*;

public class Main {

    public static List<int[]> Daching (List<int[]> target, int N) {

        List<int[]> cmpTri = new ArrayList<>();

        for (int i = 0; i<N; i++) {
            int[] newRow = new int[i+1];
            cmpTri.add(newRow);
        }

        for (int i = 0; i<N; i++) {
            int[] row = target.get(i);
            int[] newRow = cmpTri.get(i);

            int len = row.length;
            
            for (int j = 0; j<=len/2; j++) {
                int x = row[j];
                int y = row[len-1-j];
                
                newRow[len-1-j] = x;
                newRow[j] = y;
            }
        }

        // for (int i = 0; i<N; i++) {
        //     System.out.println(Arrays.toString(cmpTri.get(i)));
        // }

        return cmpTri;
    }

    public static List<int[]> Turn (List<int[]> target, int N) {

        List<int[]> newTri = new ArrayList<>();

        for (int i = 0; i<N; i++) {
            int[] newRow = new int[i+1];
            newTri.add(newRow);
        }

        for (int i = 0; i<N; i++) {
            int[] curRow = target.get(i);
            
            for (int j = 0; j<curRow.length; j++) {
                int[] row = newTri.get(N-1-j);

                row[i-j] = curRow[j];
            }
        }

        // for (int i = 0; i<N; i++) {
        //     System.out.println(Arrays.toString(newTri.get(i)));
        // }

        return newTri;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        List<int[]> triangle1 = new ArrayList<>();

        for (int i = 0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            int[] rows = new int[i+1];

            for (int j = 0; j<=i; j++) {
                rows[j] = Integer.parseInt(st.nextToken());
            }
            triangle1.add(rows);
        }

        List<int[]> triangle2 = new ArrayList<>();

        for (int i = 0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            int[] rows = new int[i+1];

            for (int j = 0; j<=i; j++) {
                rows[j] = Integer.parseInt(st.nextToken());
            }
            triangle2.add(rows);
        }

        int min = 1<<11;
        
        for (int i = 0; i<3; i++) {
            int cnt = 0;
            
            List<int[]> cmpTri = Daching(triangle2, N);
            int row = 0;
            
            while (row < N) {
                int[] cmpRow = cmpTri.get(row);
                int[] initRow = triangle1.get(row);
                
                for (int j = 0; j<cmpRow.length; j++) {
                    if (cmpRow[j] != initRow[j]) cnt++;
                }
                row++;
            }
            
            min = min>cnt ? cnt:min;
            
            // System.out.println(min);
            triangle2 = Turn(triangle2, N);
            cnt = 0;
            
            row = 0;
            
            while (row < N) {
                int[] cmpRow = triangle2.get(row);
                int[] initRow = triangle1.get(row);

                for (int j = 0; j<cmpRow.length; j++) {
                    if (cmpRow[j] != initRow[j]) cnt++;
                }
                row++;
            }

            min = min>cnt ? cnt:min;
            // System.out.println(min);

            if (min == 0) break;
        }
        
        System.out.println(min);

    }
}