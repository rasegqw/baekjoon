import java.io.*;
import java.util.*;

public class Main {

    static int MOD = 1000000007;
    static int MAX = 100000;
    static long[] fact = new long[MAX + 1];
    static int[] mu = new int[MAX + 1];
    static int[] minPrime = new int[MAX + 1];
    static List<Integer> primes = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int T = Integer.parseInt(st.nextToken());
        precomputeMobius();
        precomputeFactorials();

        for (int i = 0; i < T; i++) {
            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int f = Integer.parseInt(st.nextToken());

            testCase(n, f);
        }
    }

    // 뫼비우스 함수 전처리
    static void precomputeMobius() {
        mu[1] = 1;
        for (int i = 2; i <= MAX; i++) {
            if (minPrime[i] == 0) {
                minPrime[i] = i;
                mu[i] = -1;
                primes.add(i);
            }
            for (int p : primes) {
                if (i * p > MAX) break;
                minPrime[i * p] = p;
                if (i % p == 0) {
                    mu[i * p] = 0; // 제곱 인수가 포함됨
                    break;
                } else {
                    mu[i * p] = -mu[i]; // mu[i*p] = mu[i] * mu[p]
                }
            }
        }
    }

    static void precomputeFactorials() {
        fact[0] = 1;
        for (int i = 1; i <= MAX; i++) {
            fact[i] = (fact[i - 1] * i) % MOD;
        }
    }
            
    static long nCr(int n, int r) {
        if (r < 0 || r > n) {
            return 0;
        }

        long num = fact[n];
        long den = (fact[r] * fact[n - r]) % MOD;
        return (num * modInverse(den)) % MOD;
    }

    static long modInverse(long n) {
        return power(n, MOD - 2);
    }

    static long power(long a, long b) {
        long res = 1;
        a %= MOD;
        while (b > 0) {
            if ((b & 1) == 1) { // b가 홀수이면
                res = (res * a) % MOD;
            }
            a = (a * a) % MOD;
            b >>= 1; // b = b / 2
        }
        return res;
    }

    // 서로 같은 n-f 개를 서로 다른 f개의 바구니에 나눠 담는 상황
    // 이것 또한 중복 조합을 사용. -> n-1Cf-1 여기까진 할 수 있음.
    // 근데 여기서 한가지 조건이 더 붙는데, 나눠준 모든 사탕을 공통적으로 나누는 인수가 존재하면 안된다.
    // 마지막 조건을 어떻게 살펴야할까.
    public static void testCase(int n, int f) {

        long ans = 0;

        // n의 약수를 탐색 (O(sqrt(n)))
        for (int d = 1; d * d <= n; d++) {
            if (n % d == 0) {
                // 약수 d에 대해 계산
                int n_d1 = n / d;
                // mu[d] * C(n/d - 1, f - 1)
                long term1 = (long) mu[d] * nCr(n_d1 - 1, f - 1);
                ans = (ans + term1) % MOD;

                // 중복 방지 (d*d == n 인 경우)
                if (d * d != n) {
                    // 약수 n/d에 대해 계산
                    int d2 = n / d;
                    int n_d2 = n / d2; // == d
                    // mu[n/d] * C(d - 1, f - 1)
                    long term2 = (long) mu[d2] * nCr(n_d2 - 1, f - 1);
                    ans = (ans + term2) % MOD;
                }
            }
        }

        System.out.println((ans + MOD) % MOD) ;
        return;
    }
}