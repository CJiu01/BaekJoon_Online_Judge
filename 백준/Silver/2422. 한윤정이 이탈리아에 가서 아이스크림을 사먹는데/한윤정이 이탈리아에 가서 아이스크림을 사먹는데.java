import java.util.*;
import java.io.*;

public class Main {
	static int N, M;
	static boolean comb[][];
	static int arr[];
	static boolean visit[];
	
	static int ans[];
	static int result = 0;
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		arr = new int[N+1];
		visit = new boolean[N+1];
		
		comb = new boolean[N+1][N+1]; 
		ans = new int[3]; 
		
		for(int i=1; i<=N; i++) arr[i-1] = i;
		
		for(int i=0; i<M; i++) {
			st = new StringTokenizer(br.readLine());
			int num = Integer.parseInt(st.nextToken());
			int num2 = Integer.parseInt(st.nextToken());
			
			comb[num][num2] = true;
			comb[num2][num] = true;
		}		

		DFS(0, 0);
		
		System.out.println(result);
	} // End of main
	
	private static void DFS(int idx, int depth) { // 백트래킹
		
        if(depth == 3) {
			for(int i=0; i<3; i++) {
				for(int j=0; j<3; j++) {
					if(comb[ans[i]][ans[j]]) {
						return;
					}
				}
			}
			result++;
			return;
		}
		
		for(int i=idx; i<N; i++) {
			if(visit[i]) continue;
			visit[i] = true;
			ans[depth] = arr[i];
			DFS(i+1, depth+1);
			visit[i] = false;
		}
	} 
}