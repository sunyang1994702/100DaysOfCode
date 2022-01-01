

public class LoopStatement{

    public static void main(String[] args) {
        LoopStatement loop = new LoopStatement();
        loop.forStatement();
        loop.whileStatement();
    }

    public void forStatement() {
        int result = 0;
        for(int i=1; i <= 100; i++){
            result += i;
        }

        System.out.println("For result=" + result);
    }

    public void whileStatement() { 
        int result = 0;
        int i = 1;
        while(i <= 100){
            result += 1;
            i ++;
        }
        System.out.println("While result=" + result);
    }
}