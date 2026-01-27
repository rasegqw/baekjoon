import java.util.*;

// 1. 왼쪽에서부터 k번째 수부터 접근.(오른쪽에서부터 length - k 부터 접근.)
// 2. 왼쪽 0 ~ k index 까지, max 값 찾기.
// 3. 해당 max값의 index 왼쪽들은 모두 탈락.
// 4. 해당 index + 1 부터는 계속 오른쪽으로 k - index 만큼 카운트 하다가,
//    더 큰게 나온다? -> 해당 인덱스만큼 또 빼주고 다시 진행
// 5. 만약 전부 진행했는데, 더 큰수가 안나왔다? 그럼 해당 값 stringBuilder에 넣고, 재순환.

// 해당 방식으로 진행하면 시간 초과를 마주하지 않을까?
// 다시 리뉴얼

// 1. 왼쪽부터 length - k까지 max값 찾아서 진행,
// 2. max값이 갱신된다? -> 그러면 Array 다시 만들기.
// 3. max값을 새로 갱신할 수 없다? -> 가장 뒤부터 비교하며 자리찾기.
//    거의 가장 큰 내림차순 만들기 느낌.

// 1. 

class Solution {
    public String solution(String number, int k) {
        
        int len = number.length() - k;
        char[] numberCharArr = number.toCharArray();
        char[] answerArr = new char[len];
        int index = 0;
        int rmCnt = 0;
        char maxChar = 0;
        
        for (int i = 0; i < number.length(); i++) {
            char c = numberCharArr[i];
            
            // 삭제 카운트를 모두 소모했을 때,
            if (rmCnt == k) {
                answerArr[++index] = c;
                continue;
            }
            
            // 삭제 카운트가 여유가 있고, 새로운 알파가 나타난 경우,
            if (c > maxChar && i <= k) {
                maxChar = c;
                answerArr = new char[len];
                answerArr[0] = c;
                index = 0;
                rmCnt = i;
                continue;
            }
            
            // 마지막 숫자보다 큰 수가 들어오면 숫자 교체.
            if (c > answerArr[index]) {
                // 새로운 숫자가 들어왔다면, 남은 삭제 카운트 만큼,
                // 앞에 숫자들과 경쟁해야함.
                while(index > 0
                      && answerArr[index] < c
                      && rmCnt < k) {
                    answerArr[index--] = c;
                    rmCnt++;
                }
                index++;

                continue;
            }
            
            if (c <= answerArr[index]) {
                if (index >= len - 1) {
                    rmCnt++;
                    continue;
                }
                answerArr[++index] = c;
            }
            
        }
        
        StringBuilder sb = new StringBuilder();
        for (char c : answerArr)
            sb.append(c);
        
        return sb.toString();
    }
}