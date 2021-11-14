import java.util.Scanner;

public class ScannerTest {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Please input a number:");
        int a = scanner.nextInt();
        System.out.printf("%d square is %d\n", a, a*a);
    }
}