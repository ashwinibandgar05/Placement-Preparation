public class forLoop {
    public static void main(String[] args){
        // for (int i=0;i<=6;i++){
        //     System.out.println(i);
        // }

        //First n odd numbers
        int n=5;
        System.out.println("Odd Numbers:");
        for(int i=0;i<n;i++){
            
            System.out.println(2*i+1);
        }

        System.out.println("Even Numbers:");
        for(int i=0;i<n;i++){
            System.out.println(2*i);
        }
    }
}
