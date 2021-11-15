public class GradeLevel {
    public static void main(String[] args) {
        char grade = 'u';
        switch( grade ){
            case 'A' :
                System.out.println(grade + " is 85-100");
                break;
            case 'B' :
                System.out.println(grade + " is 70-84");
                break;
            case 'C' :
                System.out.println(grade + " is 60-69");
                break;
            default :
                System.out.println("input error");
        }
    }
}
