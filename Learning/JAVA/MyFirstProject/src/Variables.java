public class Variables {
    public static void main(String[] args) {

        // ❎ variable = a reusable container for a value
        //               a variable behaves as if it was the value it contains

        // 🔴 Primitive = simple value stored directly in memory (stack)
        // 🔵 Reference = memory address (stack) that points to the (heap)

        // 🔴 Primitive  vs  🔵 Reference
        //    ---------         --------
        //    int               string
        //    double            array
        //    char              object
        //    boolean

        // 2 steps to creating a variable
        // ------------------------------
        // 1. declaration
        // 2. assignment

        int age = 30;
        int year = 2025;
        int quantity = 1;

        double price = 19999.99;
        double gpa = 3.5;
        double temperature = -12.5;

        char grade = 'A';
        char symbol = '!';
        char currency = '$';

        boolean isStudent = true;
        boolean forSale = true;
        boolean isOnline = true;

        String name = "Chandler Bing";
        String food = "pizza";
        String email = "fake123@gmail.com";
        String car = "Mustang";
        String color = "red";

        System.out.println("Your choice is a " + color + " " + year + " " + car);
        System.out.println("The price is: " + currency + price);

        if(forSale){
            System.out.println("There is a " + car + " for sale.");
        }
        else {
            System.out.println("The " + car + " not for sale.");
        }
    }
}
