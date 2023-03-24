import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String color1 = sc.next();
        String color2 = sc.next();
        String color3 = sc.next();

        Map<String, Integer> dict = new HashMap<String, Integer>();
        dict.put("black", 0);
        dict.put("brown", 1);
        dict.put("red", 2);
        dict.put("orange", 3);
        dict.put("yellow", 4);
        dict.put("green", 5);
        dict.put("blue", 6);
        dict.put("violet",7);
        dict.put("grey", 8);
        dict.put("white", 9);
        Long answer = (dict.get(color1) * 10 + dict.get(color2)) * (long) Math.pow(10.0, dict.get(color3));
        System.out.println(answer);

    }
}