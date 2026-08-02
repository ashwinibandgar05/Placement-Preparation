public class break_continue {
    public static void main(String[] args){
        for(int i=0;i<=10;i++){
            if(i==5){
                break;
            }
            System.out.println("Break Loop "+i);
        }

        for(int i=0;i<=10;i++){
            if(i==5){
                continue;
            }
            System.out.println("Continue Loop "+i);
        }
    }
}
