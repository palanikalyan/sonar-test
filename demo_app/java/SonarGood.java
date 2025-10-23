public class SonarGood {

    private static final String ERROR_FILE_NOT_FOUND = "Error: file not found";

    public static void main(String[] args) {
        System.out.println(ERROR_FILE_NOT_FOUND);
        doSomething();

        // Removed commented out code and unused variables
        int usedValue = compute();
        System.out.println("Computed:" + usedValue);
    }

    private static void doSomething() {
        System.out.println("doing something");
    }

    private static int compute() {
        return 99;
    }
}
