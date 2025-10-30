import java.io.*;
import java.util.*;

public class Main {
    static final long MOD = 998244353L;

    static class Student {
        int idx;     // 학생 번호 (출력용)
        long c, a;   // 입력값
        long v;      // c - a

        Student(int idx, long c, long a) {
            this.idx = idx;
            this.c = c;
            this.a = a;
            this.v = c - a;
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());
        Student[] arr = new Student[N];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            long c = Long.parseLong(st.nextToken());
            long a = Long.parseLong(st.nextToken());
            arr[i] = new Student(i + 1, c, a);
        }

        // --- 최소값 계산 (v 내림차순 정렬)
        Student[] minArr = arr.clone();
        Arrays.sort(minArr, (o1, o2) -> Long.compare(o2.v, o1.v));
        long minScore = calcScore(minArr);
        long minWays = countWays(minArr);
        String minOrder = getOrder(minArr);

        // --- 최대값 계산 (v 오름차순 정렬)
        Student[] maxArr = arr.clone();
        Arrays.sort(maxArr, Comparator.comparingLong(o -> o.v));
        long maxScore = calcScore(maxArr);
        long maxWays = countWays(maxArr);
        String maxOrder = getOrder(maxArr);

        // --- 출력
        StringBuilder sb = new StringBuilder();
        sb.append(minScore).append(" ").append(minWays).append("\n");
        sb.append(minOrder).append("\n");
        sb.append(maxScore).append(" ").append(maxWays).append("\n");
        sb.append(maxOrder);
        System.out.println(sb);
    }

    // 전체 점수 계산
    static long calcScore(Student[] arr) {
        int N = arr.length;
        long sum = 0;
        for (int i = 0; i < N; i++) {
            sum += arr[i].c * i + arr[i].a * (N - 1 - i);
        }
        return sum;
    }

    // 같은 v 값을 가진 학생끼리 팩토리얼 곱 (모듈러 적용)
    static long countWays(Student[] arr) {
        long result = 1;
        int cnt = 1;

        for (int i = 1; i < arr.length; i++) {
            if (arr[i].v == arr[i - 1].v) cnt++;
            else {
                result = (result * factorial(cnt)) % MOD;
                cnt = 1;
            }
        }
        result = (result * factorial(cnt)) % MOD;
        return result;
    }

    // 팩토리얼 계산
    static long factorial(int n) {
        long f = 1;
        for (int i = 2; i <= n; i++) {
            f = (f * i) % MOD;
        }
        return f;
    }

    // 줄 서기 순서 문자열로 변환
    static String getOrder(Student[] arr) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < arr.length; i++) {
            if (i > 0) sb.append(" ");
            sb.append(arr[i].idx);
        }
        return sb.toString();
    }
}
