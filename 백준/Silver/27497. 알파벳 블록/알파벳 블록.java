import java.io.*;
import java.util.*;

public class Main {

    // 1 : 맨 뒤에 추가, 2 : 맨 앞에 추가, 3: 가장 최근 삭제
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());

        List<Character> ans = new LinkedList<>();
        StringBuilder order = new StringBuilder();

        for (int i = 0; i<N; i++) {
            st = new StringTokenizer(br.readLine());

            int type = Integer.parseInt(st.nextToken());
            if (type == 1 || type == 2) {
                char target = st.nextToken().toCharArray()[0];
                
                // System.out.println(target);
                if (type == 1) {
                    ans.add(target);
                    order.append(type);
                } else {
                    ans.add(0, target);
                    order.append(type);
                }
            // 맨 뒤에 추가하는 경우
            } else {
                if (order.length() != 0) {
                    if (order.charAt(order.length()-1) == '1') {
                        order.deleteCharAt(order.length()-1);
                        ans.remove(ans.size()-1);
                    }
                    else {
                        order.deleteCharAt(order.length()-1);
                        ans.remove(0);
                    }
                }
            }

            // System.out.println(ans);
        }

        // System.out.println(Arrays.toString(order.toArray()));
        
        if (order.length() == 0) System.out.println(0);
        else {
            StringBuilder sb = new StringBuilder();
            for (char c : ans) {
                sb.append(c);
            }
            System.out.println(sb.toString());
        }
    }
}