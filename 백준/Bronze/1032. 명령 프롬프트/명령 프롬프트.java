import java.util.*;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
//        System.out.println(N);

        char[] pattern = sc.next().toCharArray();
//        System.out.println(pattern);
        for(int i=0; i<N-1; i++) {
            char[] fileName = sc.next().toCharArray();
            for(int j=0; j<fileName.length; j++ ) {
                if (pattern[j] != fileName[j]) {
                    pattern[j] = '?';
                }
            }
        }
        System.out.println(pattern);



    }
}
