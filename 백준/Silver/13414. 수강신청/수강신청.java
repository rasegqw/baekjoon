import java.io.*;
import java.util.*;

public class Main {

  static BufferedReader br;
  static Set<String> hash;
    
  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    hash = new LinkedHashSet<String>();

    StringTokenizer st = new StringTokenizer(br.readLine());

    int K = Integer.parseInt(st.nextToken());
    int L = Integer.parseInt(st.nextToken());

    for (int i = 0; i<L; i++) {
      String target = br.readLine().strip();

      if (hash.contains(target)) {
        hash.remove(target);
      }
      
      hash.add(target);
    }

    String[] result = new String[hash.size()];
    hash.toArray(result);

    if (result.length <= K) {
      for (String target : result) {
        System.out.println(target);
      }
    } else {
      for (int i = 0; i<K; i++) {
        System.out.println(result[i]);
      }
    }
    
  }
}