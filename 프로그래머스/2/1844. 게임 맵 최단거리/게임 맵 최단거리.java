import java.util.*;

class Solution {
    int[] dx = {1, -1, 0, 0};
    int[] dy = {0, 0, 1, -1};
    
    public int solution(int[][] maps) {
        int N = maps.length;
        int M = maps[0].length;
        int[][] visited = new int[N][M];
        
        for (int i = 0; i < N ; i++) {
            for (int j = 0; j < M; j++) {
                visited[i][j] = Integer.MAX_VALUE;
            }
        }
        
        Queue<int[]> q = new ArrayDeque<>();
        q.add(new int[] {0, 0});
        visited[0][0] = 1;
        
        while(!q.isEmpty()) {
            int[] cur = q.poll();
            int x = cur[0];
            int y = cur[1];
            int prevCnt = visited[x][y];
            
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                
                if (validate(nx, ny, N, M, maps) && cmpPrevAndCurCnt(prevCnt + 1, visited[nx][ny])) {
                    
                    visited[nx][ny] = prevCnt + 1;
                    q.add(new int[]{nx, ny});
                }
            }
        }
        
        int answer = visited[N-1][M-1] == Integer.MAX_VALUE ? -1 : visited[N-1][M-1];
        
        return answer;
        // return 0;
    }
    
    boolean validate(int x, int y, int N, int M, int[][] maps) {
        if (x < N && x >= 0 && y < M && y >= 0 && maps[x][y] == 1) return true;
        return false;
    }
    
    boolean cmpPrevAndCurCnt(int prevCnt, int curCnt) {
        if (prevCnt + 1 < curCnt) return true;
        return false;
    }
}