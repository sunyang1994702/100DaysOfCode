import java.awt.*;
import javax.swing.*;
import java.awt.List;

/**
 *  creat a small frame demo for auto-score via Java
 *  1, press the button of "出题", it will show a simple calculation question
 *  2, write the right number that you think. It will show the answer in the dialog. 
 * 
 */


public class AutoScore extends JFrame{

    public AutoScore(){
        init(); 
        setSize(400, 350); // set size of frame
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setVisible(true);
    }
    
    // Declare controls of frame
    JButton btnNew = new JButton("出题");
    JButton btnJudge = new JButton("判分");
    JLabel lalA = new JLabel("text");
    JLabel lblOp = new JLabel("text");
    JLabel lalB = new JLabel("text");
    JLabel label5 = new JLabel("=");
    JTextField txtAnswer = new JTextField();
    List listDisp = new List(0);

    public void init(){
        // define some parameters for frame
        setLayout(null);
        btnNew.setBackground(java.awt.Color.lightGray);
        btnNew.setBounds(36, 96, 98, 26);
        btnJudge.setBackground(java.awt.Color.lightGray);
        btnJudge.setBounds(216, 96, 94, 25);
        getContentPane().add(btnNew);
        getContentPane().add(btnJudge);
        lalA.setFont(new Font("Dialog", Font.PLAIN, 24));
        lalA.setBounds(36, 24, 36, 36);
        lblOp.setFont(new Font("Dialog", Font.PLAIN, 24));
        lblOp.setBounds(72, 24, 36, 36);
        lalB.setFont(new Font("Dialog", Font.PLAIN, 24));
        lalB.setBounds(108, 24, 33, 36);
        label5.setFont(new Font("Dialog", Font.PLAIN, 24));
        label5.setBounds(168, 24, 36, 36);
        getContentPane().add(lalA);
        getContentPane().add(lblOp);
        getContentPane().add(lalB);
        getContentPane().add(label5);
        txtAnswer.setFont(new Font("Dialog", Font.PLAIN, 24));
        txtAnswer.setBounds(216, 24, 85, 42);
        listDisp.setFont(new Font("Dialog", Font.PLAIN, 16));
        listDisp.setBounds(36, 144, 272, 106);
        getContentPane().add(txtAnswer);
        getContentPane().add(listDisp);

        // add button action listener event for btnNew 
        btnNew.addActionListener( e->{
            btnNew_ActionPerformed();
        });
        // add button action listener event for btnJudge 
        btnJudge.addActionListener( e->{
            btnJudge_ActionPerformed();
        });
    }

    int a = 0, b = 0;
    String op = "";
    double result = 0;

    public void btnJudge_ActionPerformed(){
        String str = txtAnswer.getText();
        double d = Double.valueOf(str).doubleValue();
        String disp = "" + a + op + b + "=" + str + " ";
        if (d == result){
            disp += "True";
        } else {
            disp += "False";
        }

        listDisp.add(disp);
    }

    public void btnNew_ActionPerformed(){
        a = (int)(Math.random() * 9 + 1);
        b = (int)(Math.random() * 9 + 1);
        int c = (int)(Math.random()*4);
        switch(c){
            case 0: op = "+"; result = a + b; break;
            case 1: op = "-"; result = a - b; break;
            case 2: op = "*"; result = a * b; break;
            case 3: op = "/"; result = a / b; break;
        }

        lalA.setText(""+a);
        lalB.setText(""+b);
        lblOp.setText(""+op);
        txtAnswer.setText("");
    }
    
    public static void main(String[] args) {
        new AutoScore();
    }

}