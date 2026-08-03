public class fibonacci {
    static int fibonacciOfN(int n) {
        if (n<=1){
            return n;
        }
        else{
            return fibonacciOfN(n-1) + fibonacciOfN(n-2);
        }
    }

    public static void main(String[] args){
        int x=8;
        System.out.println("Fibonacci of " + x + " is " + fibonacciOfN(x)); // Output: 21
    }
}
