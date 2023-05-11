import java.util.*;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner sc = new Scanner(System.in);
		ArrayList arr = new ArrayList();
		
		int n = sc.nextInt();
		for (int i=0; i<n; i++) {
			arr.add(sc.nextDouble());
		}
        
		double maxNum = (double) Collections.max(arr);
		double sum = 0.0;
		
		for (int i=0; i<n; i++) {
			sum += (double) arr.get(i) / maxNum * 100;
	    }
		double average = sum / n;
		System.out.println(average);
	}

}