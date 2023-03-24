import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int A = sc.nextInt();
        int B = sc.nextInt();
        int sum = 0;
        int[] arr = new int[1002];
        int cnt = 0;
        boolean stop = false;
        for (int i=1; i<=1001; i++) {
            for (int j=0; j<i; j++) {
                cnt++;
                arr[cnt] = i;
                if (cnt >= 1001) {
                    stop = true;
                    break;
                }
            }
            if (stop) {
                break;
            }
        }

        for (int i = A; i <= B; i++) {
            sum += arr[i];
        }
        System.out.println(sum);
    }
}
