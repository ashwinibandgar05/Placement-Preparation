public class factorial {
    static int factorialOfN(int n) {
        if (n == 0 || n == 1) {
            return 1;
        } else {
            return n * factorialOfN(n - 1);
        }
    }

    public static void main(String[] args) {
        System.out.println(factorialOfN(5)); // Output: 120
    }
}
