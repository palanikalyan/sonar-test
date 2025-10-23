public class SonarBad {

    public static void main(String[] args) {
        // S1192: duplicated string literal
        System.out.println("Error: file not found");
        doSomething();
        System.out.println("Error: file not found");

        // S125: commented out code should be removed
        // int oldValue = computeOld();

        // S1481: unused local variable
        int unused = 42;

        // S1854: assigned value is never used
        int neverUsed = 0;
        neverUsed = compute();

        // Bug: add dead code
        if (false) {
            System.out.println("This code is commented out / dead and should be removed");
        }
    }

    private static void doSomething() {
        // pretend work
        System.out.println("doing something");
    }

    private static int compute() {
        return 99;
    }
}
