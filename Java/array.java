public class array {
    public static void main(String[] args){
        System.out.println("Array in Java");
        // Array declaration 
        int []array;
        //array memmory allocation
        array=new int[5];//5 is size of array
        for(int i=0;i<array.length;i++){
            array[i]=i+1;
            System.out.println("Array element " + (i+1) + ": " + array[i]);
        }



        //Array daclaration and memory allocation
        System.out.println("\nArray daclaration and memory allocation");
        int []arr=new int[5];
        arr[0]=10;
        arr[1]=20;
        arr[2]=30;
        arr[3]=40;
        arr[4]=50;
        for(int i=0;i<arr.length;i++){
            System.out.println("Array element " + (i+1) + ": " + arr[i]);
        }


        //Array declaration , memory allocation and initialization together
        System.out.println("\nArray declaration , memory allocation and initialization together");
        int []arr1={100,200,300,400,500};
        for(int i=0;i<arr1.length;i++){
            System.out.println("Array element " + (i+1) + ": " + arr1[i]);
        }


        System.out.println("\nArray of float values in array");
        float []arr2={1.1f,2.2f,3.3f,4.4f,5.5f};
        for(int i=0;i<arr2.length;i++){
            System.out.println("Array element " + (i+1) + ": " + arr2[i]);
        }

        System.out.println("\nArray of String values in array");
        String []arr3={"Hello","World","Java","Array"};
        for(int i=0;i<arr3.length;i++){
            System.out.println("Array element " + (i+1) + ": " + arr3[i]);
        }


        //Operation on array
        System.out.println("\nOperation on array");
        int []arr4={1,2,3,4,5};
        int sum=0;  
        System.out.println("Length of array: "+arr4.length);
        System.out.println("Elements of array in reverse order: ");
        for(int i=arr4.length-1;i>=0;i--){
            System.out.println("Array element " + (i+1) + ": " + arr4[i]);
        }

        //for each loop method
        System.out.println("\nfor each loop method");
        for(int i:arr4){
            System.out.println("Array element: " + i);
        }
    }
}
