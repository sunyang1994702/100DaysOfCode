import java.util.*;


public class ArrayDemo {

    public static void main(String[] args) {
        int[] ages = new int[10];
        for (int i = 0; i < 10; i++) {
            // adding element in array ages.
            ages[i] = i+1;
        }

        System.out.println(ages);

        for (int age : ages) {
            System.out.println(age);
        }
        // adding element in array. using ArrayList method
        List<Integer> nums = new ArrayList<Integer>();
        nums.add(24);
        nums.add(8);
        System.out.println(nums);
        
    }
}