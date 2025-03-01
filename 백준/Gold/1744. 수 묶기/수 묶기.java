import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        PriorityQueue<Integer> plus = new PriorityQueue<>(Collections.reverseOrder());
        PriorityQueue<Integer> minus = new PriorityQueue<>();
        int one = 0;
        int zero = 0;

        for(int i=0; i<n; i++) {
            int num = Integer.parseInt(br.readLine());

            if(num>1) plus.add(num);
            else if(num==1) one++;
            else if(num==0) zero++;
            else minus.add(num);
        }

        int res = 0;

        // plus는 최댓값부터 곱해줌
        while(plus.size() > 1) {
            res += plus.poll() * plus.poll();
        }
        if(plus.size()>0) res += plus.poll();

        // 1은 개수만큼 더해줌
        res += one;

        // minus는 최솟값부터 곱해줌
        while(minus.size() > 1) {
            res += minus.poll() * minus.poll();
        }
        if(minus.size()>0) {
            if(zero<=0) res += minus.poll();
        }
        System.out.println(res);
    }
}