import java.io.*;
import java.util.*;

public class Main {

    // 모듈러 값 (소수)
    static final int MOD = 1000000009;
    
    // N의 최대값(500) + 소인수 지수의 최대값(500 * log2(10^9) ≈ 15000)
    static final int MAX_COMB_N = 16000; 
    
    // 팩토리얼과 팩토리얼의 모듈러 역원을 저장할 배열
    static long[] fact = new long[MAX_COMB_N];
    static long[] invFact = new long[MAX_COMB_N];

    /**
     * 메인 실행 함수
     */
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        // N 입력
        int N = Integer.parseInt(br.readLine());
        
        // N개의 수 입력
        StringTokenizer st = new StringTokenizer(br.readLine());

        // 팩토리얼 및 모듈러 역원 전처리
        precomputeFactorials();

        // M의 전체 소인수분해 결과를 저장할 맵
        // Key: 소인수, Value: 총 지수
        Map<Integer, Integer> primeExponents = new HashMap<>();

        // N개의 숫자를 순회하며 소인수분해
        for (int i = 0; i < N; i++) {
            int num = Integer.parseInt(st.nextToken());
            factorize(num, primeExponents);
        }

        long totalWays = 1;

        // M의 각 소인수(p)와 그 총 지수(e)에 대해 중복 조합 계산
        // 공식: C(e + N - 1, N - 1)
        for (int exponent : primeExponents.values()) {
            // 이 소인수를 N개로 나누는 경우의 수
            long waysForThisPrime = nCr(exponent + N - 1, N - 1);
            
            // 총 경우의 수에 곱해줌 (모듈러 연산)
            totalWays = (totalWays * waysForThisPrime) % MOD;
        }

        // 최종 결과 출력
        System.out.println(totalWays);
    }

    /**
     * 숫자 n을 소인수분해하여 그 결과를 map에 누적
     * @param n 소인수분해할 숫자
     * @param map (소인수 -> 지수) 맵
     */
    public static void factorize(int n, Map<Integer, Integer> map) {
        // 2부터 sqrt(n)까지 순회
        for (int d = 2; d * d <= n; d++) {
            if (n % d == 0) {
                int count = 0;
                while (n % d == 0) {
                    n /= d;
                    count++;
                }
                // map에 해당 소인수의 지수를 더해줌
                map.put(d, map.getOrDefault(d, 0) + count);
            }
        }
        // 루프가 끝난 후 n > 1 이면, n 자체가 소수임
        if (n > 1) {
            map.put(n, map.getOrDefault(n, 0) + 1);
        }
    }

    /**
     * 팩토리얼과 모듈러 역원(Inverse Factorial)을 전처리
     */
    public static void precomputeFactorials() {
        fact[0] = 1;
        invFact[0] = 1;

        // 팩토리얼 계산 (i! % MOD)
        for (int i = 1; i < MAX_COMB_N; i++) {
            fact[i] = (fact[i - 1] * i) % MOD;
        }

        // invFact[n] = (n!)^(MOD-2) % MOD (페르마의 소정리)
        invFact[MAX_COMB_N - 1] = power(fact[MAX_COMB_N - 1], MOD - 2);

        // invFact[i-1] = invFact[i] * i % MOD
        for (int i = MAX_COMB_N - 2; i >= 1; i--) {
            invFact[i] = (invFact[i + 1] * (i + 1)) % MOD;
        }
    }

    /**
     * 조합(Combination) nCr % MOD 계산
     * nCr = n! / (r! * (n-r)!)
     * = n! * (r!)^(-1) * ((n-r)!)^(-1) % MOD
     */
    public static long nCr(int n, int r) {
        if (r < 0 || r > n) {
            return 0;
        }
        // (fact[n] * invFact[r]) % MOD * invFact[n - r] % MOD
        return (((fact[n] * invFact[r]) % MOD) * invFact[n - r]) % MOD;
    }

    /**
     * 모듈러 거듭제곱 (base^exp % MOD)
     * (Binary Exponentiation)
     */
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