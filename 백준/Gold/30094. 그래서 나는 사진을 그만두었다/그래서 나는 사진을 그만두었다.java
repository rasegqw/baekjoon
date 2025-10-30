import java.io.*;
import java.util.*;

public class Main {

  static int DIV_NUM = 998244353;
  static int N;
  static long[][] totalDiff;
  static long maxRes = 0;
  static long constant;
  static long minRes = Long.MAX_VALUE;
  

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    N = Integer.parseInt(st.nextToken());
    totalDiff = new long[N][2];
    Map<Long, Integer> diffMap = new HashMap<>();

    for (int i = 0; i < N; i++) {
      st = new StringTokenizer(br.readLine());

      long c = Integer.parseInt(st.nextToken());
      long a = Integer.parseInt(st.nextToken());
      totalDiff[i][0] = c - a;
      totalDiff[i][1] = i;
      if (diffMap.containsKey(totalDiff[i][0])) {
        int x = diffMap.get(totalDiff[i][0]);
        diffMap.put(totalDiff[i][0], x+1);
      } else {
        diffMap.put(totalDiff[i][0], 1);
      }

      constant -= c;
      constant += a * N;
    }

    // 학생 i의 인물 점수 : c_i*l_i + a_i*r_i
    // l_i : 학생i 왼쪽 사람 수, r_i : 오른쪽 사람 수
    // 사진 점수 : N명의 인물점수 모두 더하기.

    // sum(c*(i-1) + a*(N-i)) 이 값을 구하고 싶은 거니까,
    // sum(i*(c-a)-c+a*N)으로 식을 고칠 수 있었고,
    // sum(-c + a*N) 부분은 상수이기 때문에, sum(i*(c-a)) 만 신경쓰면 됐다.
    
    // 결국 전체 팩토리얼을 브루트포스로 만들어낼 필요는 없었고, c-a 값이 같은 놈들 집합이 몇개, 몇개의 원소를 가지고 있는지만 파악해서, 경우의 수를 계산하면 됐다.
    // 그래서 최댓값을 구하기 위해선, c-a를 오름차순으로 배치하면 되고,
    // 최솟값을 구하기 위해선 c-a를 내림차순으로 배치하면 된다.
    Arrays.sort(totalDiff, (a, b) -> Long.compare(b[0], a[0]));
    long res = 0;

    for (int i = 0; i < N; i++) {
        res += totalDiff[i][0] * (i+1);
    }

    long cnt = 1;
    for (int val : diffMap.values()) {
        // System.out.println("val : " + val);
        cnt *= factorial(val);
        cnt %= DIV_NUM;
    }
    System.out.println(res+constant + " " +cnt);

    StringBuilder sb = new StringBuilder();

    for (int i = 0; i<N; i++) {
        sb.append(totalDiff[i][1]+1 + " ");
    }
    System.out.println(sb.toString());

    Arrays.sort(totalDiff, (a, b) -> Long.compare(a[0], b[0]));
    res = 0;

    for (int i = 0; i < N; i++) {
        res += totalDiff[i][0] * (i+1);
    }

    cnt = 1;
    for (int val : diffMap.values()) {
        cnt *= factorial(val);
        cnt %= DIV_NUM;
    }
    System.out.println(res+constant + " " +cnt);

    sb = new StringBuilder();

    for (int i = 0; i<N; i++) {
        sb.append(totalDiff[i][1]+1 + " ");
    }
    System.out.println(sb.toString());
  }


  public static long factorial(int n) {

    long result = 1;

    for (int i = 1 ; i <= n; i++) {
      result *= i;
      result %= DIV_NUM;
    }

    return result;
  }
}
