public class MultidimArray {
    public static void main(String[] args){
        // Declaring a 2D array
        int[][] arr = new int[3][4];

        // Initializing the 2D array
        for(int i=0; i<3; i++){
            for(int j=0; j<4; j++){
                arr[i][j] = i  + j*2;
            }
        }

        // Printing the 2D array
        for(int i=0; i<3; i++){
            for(int j=0; j<4; j++){
                System.out.print(arr[i][j] + "  ");
            }
            System.out.println();
        }


        //declaration ,memory alocation and initialization
        System.out.println("\n 2D Array with declaration, memory allocation and initialization");
        int [][]arr2={
            {1,2,3},
            {4,5,6},
            {7,8,9}
        };
        //Printing 2d array
        for(int i=0; i<3; i++){
            for(int j=0; j<3; j++){
                System.out.print(arr2[i][j] + "  ");
            }
            System.out.println();
        }
    }
}
