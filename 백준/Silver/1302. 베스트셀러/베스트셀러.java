import java.io.*;
import java.util.*;

public class Main {

  public static void main(String[] args) throws IOException {
    // 입력 처리
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int N = Integer.parseInt(br.readLine());
    Map<String, Integer> hashMap = new HashMap<>();

    for (int i = 0; i < N; i++) {
      String target = br.readLine().strip();

      if (hashMap.containsKey(target)) {
        hashMap.put(target, hashMap.get(target) + 1);
      } else {
        hashMap.put(target, 1);
      }
    }

    // 제일 많이 팔린 책 개수 찾기.
    // 개수가 같은 경우, 책 이름 사전순으로 빠른게 maxBookName
    List<String> maxBookList = new ArrayList<>(); 
    int maxVal = Integer.MIN_VALUE;

    for (String s : hashMap.keySet()) {
      int val = hashMap.get(s);

      if (maxVal < val) {
        maxVal = val;
        maxBookList = new ArrayList<>();
        maxBookList.add(s);
      } else if (maxVal == val) {
        maxBookList.add(s);
      }
    }

    // 같은 개수들 중, 사전순 정렬.
    String[] target = new String[maxBookList.size()];
    maxBookList.toArray(target);
    Arrays.sort(target);

    // 출력
    System.out.println(target[0]);
  }
}