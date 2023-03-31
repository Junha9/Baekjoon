import java.util.*;

public class Main {

    static int[] dayArray(int year) {
        int[] day = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        if (((year % 4 == 0) && (year % 100 != 0)) || (year % 400 == 0)) {
            day[1] = 29;
        }
        return day;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int sy = sc.nextInt();
        int sm = sc.nextInt();
        int sd = sc.nextInt();
        int ey = sc.nextInt();
        int em = sc.nextInt();
        int ed = sc.nextInt();

        int dday = 0;

        if ((ey-sy > 1000) || (ey - sy == 1000 && em > sm) || (ey-sy == 1000 && em == sm && ed >= sd)) {
            System.out.println("gg");
        }
        else {
            for (int i = sy; i < ey; i++) {
                dday += Arrays.stream(dayArray(i)).sum();
            }
            for (int i = 0; i < sm-1; i++) {
                dday -= (dayArray(sy)[i]);
            }
            for (int i = 0; i < em-1; i++) {
                dday += (dayArray(ey)[i]);
            }
            dday = dday + ed - sd;
            System.out.println("D-" + dday);
        }

    }
}
