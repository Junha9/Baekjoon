import java.util.*;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        String word = sc.nextLine();
        int length = word.length();
        List result = new ArrayList<>();
        for (int i=1; i<length-1; i++) {
            for (int j=1; j<length-i; j++) {
//                int[] array = {i, j, length-i-j};
//                System.out.println(Arrays.toString(array));
                String word1 = word.substring(0,i);
                String word2 = word.substring(i,i+j);
                String word3 = word.substring(i+j, length);
                StringBuffer sb1 = new StringBuffer(word1);
                StringBuffer sb2 = new StringBuffer(word2);
                StringBuffer sb3 = new StringBuffer(word3);
                String reversed = sb1.reverse().toString() + sb2.reverse().toString() + sb3.reverse().toString();
                result.add(reversed);

            }
        }
        Collections.sort(result);
        System.out.println(result.get(0));
    }
}
