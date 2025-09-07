import java.io.*;
import java.util.*;

public class Main {

 static int top;

 public static boolean dfs(int idx, List<Integer> path, String[] src, boolean[] visited) {
    String target = "";
    
    if (path.size() == top) return true;

    for (int i = 0; i<=1; i++) {
        if (idx+i >= src.length) return false;
        target += src[idx + i];
        // System.out.println(target);
        int x = Integer.parseInt(target);

        if (x > top) continue;
        if (visited[x] == true) continue;
        else {
            if (x == 0) return false;
            visited[x] = true;
            path.add(x);

            if (dfs(idx+i+1, path, src, visited)) {
                return true;                
            }
            else {
                visited[x] = false;
                path.remove(path.size()-1);
            }
        }
    }

    return false;
 }
    
 public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    String target = st.nextToken();

    // System.out.println(target);
    List<Integer> res = new ArrayList<>();

    int len = target.length();
    String[] src = new String[len];
    boolean[] visited = new boolean[(len-9)/2+10];    
    src = target.split("");

    // System.out.println(Arrays.toString(src));

    if (len <= 9) {
        for (int i = 0; i<len; i++) {
            res.add(Integer.parseInt(src[i]));
        }
    }
    else {
        top = (len - 9)/2 + 9;
        // System.out.println("top : "+top);

        dfs(0, res, src, visited);
    }


    StringBuilder result = new StringBuilder();

    for (int i = 0; i<res.size(); i++) result.append(res.get(i)+" ");

    System.out.println(result.toString());
 }   
}