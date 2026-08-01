import java.util.Scanner;

public class MarkPercentage {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        
        System.out.print("Enter Marks of Subject 1: ");
        int s1=sc.nextInt();
        System.out.print("Enter marks of subject 2:");
        int s2=sc.nextInt();
        System.out.print("Enter marks of subject 3:");
        int s3=sc.nextInt();
        System.out.print("Enter marks of subject 4:");
        int s4=sc.nextInt();
        int total=s1+s2+s3+s4;

        float percentage=(total/400.0f)*100;
        System.out.print("Marks Percentage obtained In exam:" +percentage+" %");


    }
    
}
