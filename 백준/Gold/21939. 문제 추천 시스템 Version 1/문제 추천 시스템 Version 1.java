import java.io.*;
import java.util.*;

public class Main {

  static int maxLevel = Integer.MIN_VALUE;
  static int minLevel = Integer.MAX_VALUE;
  static Map<Integer, TreeSet<Integer>> probLevelAndNum = new HashMap<>();
  static Map<Integer, Integer> probNumAndLevel = new HashMap<>();


  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int N = Integer.parseInt(br.readLine());

    // 문제번호 / 난이도 입력 저장
    for (int i = 0; i < N; i++) {
      StringTokenizer st = new StringTokenizer(br.readLine());
      int num = Integer.parseInt(st.nextToken());
      int level = Integer.parseInt(st.nextToken());
      maxLevel = Math.max(maxLevel, level);
      minLevel = Math.min(minLevel, level);

      probNumAndLevel.put(num, level);
      if (probLevelAndNum.containsKey(level)) {
        Set<Integer> targetValue = probLevelAndNum.get(level);
        targetValue.add(num);
      } else {
        TreeSet<Integer> target = new TreeSet<Integer>();
        target.add(num);
        probLevelAndNum.put(level, target);
      }
    }

    int M = Integer.parseInt(br.readLine());
    String[] orderArr = new String[M];

    // 명령어 입력 저장
    for (int i = 0; i < M; i++) {
      orderArr[i] = br.readLine().strip();
    }
    
    // 메인 흐름 처리
    goToWork(orderArr);
  }

  static void goToWork(String[] orderList) {

    for (String order : orderList) {
      String[] orderSplit = order.split(" ");
      
      if (orderSplit[0].equals("recommend")) {
        // recommend 1 OR -1
        // 1이면 가장 어려운 문제 -> 여러개면 문제 번호 큰 것,
        // -1이면 가장 쉬운 문제 -> 여러개면 문제 번호 작은 것,
        if (orderSplit[1].equals("1"))  
          recommend(true);
        else 
          recommend(false);

      } else if (orderSplit[0].equals("add")){
        // add P D (문제 번호, 난이도)
        add(Integer.parseInt(orderSplit[1]), Integer.parseInt(orderSplit[2]));
      } else {
        // solved P (문제 번호)
        solved(Integer.parseInt(orderSplit[1]));
      }
    }
  }

  static void recommend(boolean upDown) {
    // upDown이 TRUE 라면, 어려운 문제 중 번호가 큰 것을 가져오기.
    if (upDown) {
      // 가장 어려운 레벨에 해당하는 문제 집합들을 가져와,
      TreeSet<Integer> targetSet = probLevelAndNum.get(maxLevel);
      int probNum = targetSet.last();

      // 번호가 가장 큰 것을 가져옴. -> 여기 순회가 문제.
      // for (int target : targetSet) {
      //   probNum = Math.max(target, probNum);
      // }
      
      System.out.println(probNum);
    } 
    // upDown이 false 라면, 어려운 문제 중 번호가 작은 것을 가져오기.
    else {
      TreeSet<Integer> targetSet = probLevelAndNum.get(minLevel);
      int probNum = targetSet.first();

      // for (int target : targetSet) {
      //   probNum = Math.min(target, probNum);
      // }
      System.out.println(probNum);
    }
  }

  static void add(int prob, int diff) {
    // add P D (문제 번호, 난이도) -> prob, diff

    // 추가할 땐, maxLevel, minLevel 검증해야함.
    maxLevel = Math.max(maxLevel, diff);
    minLevel = Math.min(minLevel, diff);

    // 레벨에 상관없이 문제 번호가 key인 해시맵에 추가해주고,
    probNumAndLevel.put(prob, diff);

    // 난이도가 key인 해시맵에 문제 추가.
    if (probLevelAndNum.containsKey(diff)) {
      TreeSet<Integer> targetValue = probLevelAndNum.get(diff);
      targetValue.add(prob);
    } else {
      TreeSet<Integer> target = new TreeSet<Integer>();
      target.add(prob);
      probLevelAndNum.put(diff, target);
    }
  }

  static void solved(int prob) {
    // solved P (문제 번호) -> prob

    // 문제를 푼다면, 두 해시맵에서 해당 key-value 관계를 삭제해줘야 함.
    // 먼저 문제 번호를 통해 레벨을 받아오고,
    int level = probNumAndLevel.get(prob);

    // 레벨을 받아왔으니, 해당 해시맵에서는 문제 번호로 삭제.
    probNumAndLevel.remove(prob);

    // 받아온 레벨로, 같은 레벨의 문제들을 받아오고,
    Set<Integer> targetSet = probLevelAndNum.get(level);
  
    // 그 중, 해당하는 번호를 제거.
    targetSet.remove(prob);
    
    // 만약에 해당하는 번호를 삭제했는데, 그 집합이 비어있다?
    // 그럼 더이상 그 key는 존재할 필요가 없어 정리해줘야 함.
    if (targetSet.isEmpty()) {
      // 레벨(key)를 해당 해시맵에서 삭제해주고
      probLevelAndNum.remove(level);
    
      // 만약에 해당 레벨이 maxlevel, minlevel 중 하나였다?
      // 그러면 둘 중 하나는 반드시 업데이트 해줘야 함.
      // (분리 가능하지만, 이건 나중에 시간 복잡도가 터지면 고쳐보겠음.)
      if (level == maxLevel || level == minLevel) {
        maxLevel = Integer.MIN_VALUE;
        minLevel = Integer.MAX_VALUE;
    
        for (int lvl : probLevelAndNum.keySet()) {
          maxLevel = Math.max(lvl, maxLevel);
          minLevel = Math.min(lvl, minLevel);
        }
      }
    }

  }

}
