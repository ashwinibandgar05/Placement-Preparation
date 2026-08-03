public class varargs {
    // Method with variable number of arguments
    static void sum(int... numbers) {
        int total = 0;
        for (int num : numbers) {
            total += num;
        }
        System.out.println("Sum: " + total);
    }

    public static void main(String[] args) {
        // Calling the method with different number of arguments
        sum(1, 2, 3);
        sum(4, 5);
        sum(6);
        sum(); // No arguments
    }
}