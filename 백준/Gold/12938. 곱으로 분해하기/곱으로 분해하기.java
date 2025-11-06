import java.io.*;
import java.util.*;

public class Main {

    static final int MOD = 1000000009;
    static final int MAX_COMB_N = 15500;
    
    static long[] fact = new long[MAX_COMB_N];
    static long[] invFact = new long[MAX_COMB_N];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());

        // 팩토리얼 및 모듈러 역원 전처리
        precomputeFactorials();

        // M의 전체 소인수분해 결과를 저장할 맵
        Map<Integer, Integer> primeExponents = new HashMap<>();

        // N개의 숫자를 순회하며 소인수분해
        for (int i = 0; i < N; i++) {
            int num = Integer.parseInt(st.nextToken());
            factorize(num, primeExponents);
        }

        long totalWays = 1;

        // M의 각 소인수(p)와 그 총 지수(e)에 대해 중복 조합 계산
        for (int exponent : primeExponents.values()) {
            // 이 소인수를 N개로 나누는 경우의 수
            long waysForThisPrime = nCr(exponent + N - 1, N - 1);
            
            // 총 경우의 수에 곱해줌 (모듈러 연산)
            totalWays = (totalWays * waysForThisPrime) % MOD;
        }

        System.out.println(totalWays);
    }

    public static void factorize(int n, Map<Integer, Integer> map) {
        for (int d = 2; d * d <= n; d++) {
            if (n % d == 0) {
                int count = 0;
                while (n % d == 0) {
                    n /= d;
                    count++;
                }
                map.put(d, map.getOrDefault(d, 0) + count);
            }
        }

        if (n > 1) {
            map.put(n, map.getOrDefault(n, 0) + 1);
        }
    }

    public static void precomputeFactorials() {
        fact[0] = 1;
        invFact[0] = 1;

        for (int i = 1; i < MAX_COMB_N; i++) {
            fact[i] = (fact[i - 1] * i) % MOD;
        }

        invFact[MAX_COMB_N - 1] = power(fact[MAX_COMB_N - 1], MOD - 2);

        for (int i = MAX_COMB_N - 2; i >= 1; i--) {
            invFact[i] = (invFact[i + 1] * (i + 1)) % MOD;
        }
    }

    public static long nCr(int n, int r) {
        if (r < 0 || r > n) {
            return 0;
        }

        return (((fact[n] * invFact[r]) % MOD) * invFact[n - r]) % MOD;
    }

    public static long power(long base, int exp) {
        long res = 1;
        base %= MOD;
        while (exp > 0) {
            if (exp % 2 == 1) { // 지수가 홀수이면
                res = (res * base) % MOD;
            }
            base = (base * base) % MOD; // 밑을 제곱
            exp /= 2; // 지수를 반으로
        }
        return res;
    }
}