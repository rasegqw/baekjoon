import java.io.*;
import java.util.*;

public class Main {
    static int baseLog(double x, double base) {return (int)(Math.log(x) / Math.log(base));}
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        PriorityQueue<Integer> small_Heap = new PriorityQueue<>(Collections.reverseOrder());
        PriorityQueue<Integer> big_Heap = new PriorityQueue<>();

        st = new StringTokenizer(br.readLine());

        int target = Integer.parseInt(st.nextToken());
        small_Heap.add(target);

        for (int i = 0; i<N-1; i++) {
            target = Integer.parseInt(st.nextToken());
            int cmpNum = small_Heap.peek();

            if (target > cmpNum) {
                if (big_Heap.size() == small_Heap.size()) {
                    if (big_Heap.peek() > target) small_Heap.add(target);
                    else {
                        int x = big_Heap.remove();
                        small_Heap.add(x);
                        big_Heap.add(target);                
                    }
                }
                else big_Heap.add(target);
            }
            else {
                if (big_Heap.size() < small_Heap.size()) {
                    int x = small_Heap.remove();
                    big_Heap.add(x);
                }
                small_Heap.add(target);
            }
            
            // System.out.println("small : "+small_Heap.toString());
            // System.out.println("big : "+big_Heap.toString());
        }
        // System.out.println("find all");
        int count = N/2;
        if (N%2 == 1) count++;
        
        int cnt = 0;
        for (int i = 0; i<count; i++) {
            int middle = small_Heap.remove();
            // System.out.println(middle);
            cnt += baseLog(middle, 2);
            // System.out.println(cnt);
        }
        
        System.out.println(cnt+1);
    }
}