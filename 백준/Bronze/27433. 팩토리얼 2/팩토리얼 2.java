import java.io.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());

		if (N < 0 || N > 20)
			return;

		System.out.println(factorial(N));
	}

	public static long factorial(int num) {
		return (num == 0 || num == 1) ? 1 : num*factorial(num - 1);
	}
}