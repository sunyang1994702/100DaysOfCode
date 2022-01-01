import java.awt.*;
import javax.swing.*;


public class Circle99Frame extends JFrame{
    public static void main(String[] args) {
        JFrame frame = new Circle99Frame();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(600, 600);
        frame.setVisible(true);
    }

    public void paint(Graphics g){
        g.drawString("circle 99", 20, 20);
        int x0 = getSize().width / 2;
        int y0 = getSize().height / 2;
        for (int i = 0; i < getSize().height/2; i+=10) {
            g.setColor(getRandomColor());
            g.drawOval(x0-i, y0-i, i*2, i*2);
        }
    }

    Color getRandomColor(){
        return new Color(
            (int) (Math.random() * 256), // type conversion
            (int) (Math.random() * 256),
            (int) (Math.random() * 256)
        );
    }

}