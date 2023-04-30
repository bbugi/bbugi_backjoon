import java.util.*;
import java.io.*;

public class Main {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		HashSet<Integer> arr = new HashSet<Integer>();
		
		for (int i = 0; i < 10; i++) {
			int n = Integer.parseInt(br.readLine());
			arr.add(n%42);
		}
//		System.out.println(arr);
		System.out.println(arr.size());

	}

}