import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());

        List<String>[] member = new List[201];
        for(int i=0; i<201; i++) member[i] = new ArrayList<>();

        for(int i=0;i<n;i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int age = Integer.parseInt(st.nextToken());
            String name = st.nextToken();
            member[age].add(name);
        }

        for(int i=0; i<member.length; i++) {
            if(member[i].size() > 0) {
                for(String name: member[i]) {
                    sb.append(i+" "+name+"\n");
                }
            }
        }
        System.out.println(sb);
    }
}