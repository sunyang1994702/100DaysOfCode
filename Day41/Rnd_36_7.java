public class Rnd_36_7 {

    public static void main(String[] args) {
        int a[] = new int[10];
        for (int i = 0; i < a.length; i++) {
            one_num: 
            while (true) {
                a[i] = (int)(Math.random()*36) + 1;
                for (int j = 0; j < i; j++) {
                    if (a[i] == a[j]) {
                        System.out.println("Duplicated number: " + a[j]);
                        continue one_num;
                    }
                }
                break;
            }
        }
        for (int num : a) {
            System.out.println(num);
        }
    }
}