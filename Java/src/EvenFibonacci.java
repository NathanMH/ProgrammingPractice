package evenFibonacci;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class EvenFibonacci extends JFrame implements Runnable, ActionListener{
	public int sum = 2;
	
    // For multithreading
    Thread go;

    // GUI elements
    JLabel howManyFibsLabel = new JLabel("Sum of Fibs?");
    JTextField howManyFibs = new JTextField("400", 10);
    JButton start = new JButton("Start");
    JTextArea fibs = new JTextArea(8, 40);

    EvenFibonacci(){
        // Basic GUI title, size and closing
        super("Even Fibs!!");
        setSize(400, 300);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // Set layout patter
        BorderLayout bord = new BorderLayout();
        setLayout(bord);

        // Add button listener
        start.addActionListener(this);

        // Set top panel
        JPanel topPanel = new JPanel(); 
        topPanel.add(howManyFibsLabel);
        topPanel.add(howManyFibs);
        topPanel.add(start);
        add(topPanel, BorderLayout.NORTH);

        // Set Text Area
        fibs.setLineWrap(true);
        fibs.setEditable(false);
        JScrollPane textPane = new JScrollPane(fibs);
        add(textPane, BorderLayout.CENTER);

        setVisible(true);
    }

    public void actionPerformed(ActionEvent e){
        start.setEnabled(false);
        if(go == null){
            go = new Thread(this);
            go.start();
        }
    }

    // Main logic goes here
    public void run(){
        int one = 1;
        int two = 2;
        int three = 3;

        do{
            one = two + three;
            two = one + three;
            three = one + two;

            if(one%2==0){
                sum += one;
            }else if(two%2==0){
                sum += two;
            }else if (three%2==0){
                sum += three;
            }
        }while(sum < 4000000);
        System.out.println(sum);
        fibs.append(Integer.toString(sum));
    }
    
    public static void main(String[] args){
    	EvenFibonacci ef = new EvenFibonacci();
    }
}
