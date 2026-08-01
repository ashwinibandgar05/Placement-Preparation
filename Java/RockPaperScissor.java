import java.util.Scanner;


public class RockPaperScissor {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter your Choice: From Rock ,Paper ,Scissor");
        String Choice=sc.next();
        System.out .println("your choice is:"+Choice);
        String computerChoice="Rock";
        System.out.println("Computer's choice is:"+computerChoice);
        if(Choice.equals(computerChoice)){
            System.out.println("It's a Tie!");      
        }else if(Choice.equals("Rock") && computerChoice.equals("Scissor")){
            System.out.println("You Win!");}

        else if(Choice.equals("Paper") && computerChoice.equals("Rock")){
            System.out.println("You Win!");}
    }       
}
