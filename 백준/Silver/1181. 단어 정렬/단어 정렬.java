import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.TreeSet;

public class Main {

	static int n;
	static TreeSet<String> ts = new TreeSet<String>(new Comparator<String>() {
		@Override
		public int compare(String o1, String o2) {
			//음수면 유지(o1 가 o2 보다 작으면)
			if(o1.length() == o2.length()) {
				return o1.compareTo(o2);
			} else {
				return o1.length() - o2.length();
			}
		}

	});

	public static void main(String[] args) throws IOException {
		input();
		print();
	}

	public static void input() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());

		// 중복제거를 위해 set 사용
		for(int i=0; i<n; i++) {
			String word = br.readLine();
			ts.add(word);
		}
	}

	public static void print() {
		StringBuilder sb = new StringBuilder();
		while (!ts.isEmpty()) {
			sb.append(ts.pollFirst()).append("\n");
		}
		System.out.println(sb);
	}
}