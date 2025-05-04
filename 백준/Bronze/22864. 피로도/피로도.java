import java.io.*;
import java.util.*;

public class Main {

	public static int A, B, C, M;
	public static int result = 0;
	public static int x, y;
    
    public static void simulate() {
    	int currentWorkAmount = 0;
    	int currentTired = 0;
    	
    	for(int i=1;i<=24;i++) {
    		if(currentTired + A <= M) {
    			currentWorkAmount += B;
    			currentTired += A;
    		}
    		else {
    			currentTired -= C;
    			if(currentTired < 0 ) currentTired = 0;
    		}
    	}
    	result = currentWorkAmount;
    }
	
    public static void main(String[] args) throws IOException {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	
    	StringTokenizer st = new StringTokenizer(br.readLine());
    	A = Integer.parseInt(st.nextToken());
    	B = Integer.parseInt(st.nextToken());
    	C = Integer.parseInt(st.nextToken());
    	M = Integer.parseInt(st.nextToken());
    	
    	simulate();
    	System.out.println(result);
    }
}