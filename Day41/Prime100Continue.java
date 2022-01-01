public class Prime100Continue {

    public static void main(String[] args) {
        // print the prime from 1 to 100.
        outer: for (int i = 2; i < 100; i++) {
            for (int j = 2; j < i; j++) {
                if (i % j == 0) {
                    continue outer;     
                }
            }
            System.out.println("The Prime is: " + i);
        }
    }
}