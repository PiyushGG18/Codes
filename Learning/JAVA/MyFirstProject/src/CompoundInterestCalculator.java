import java.util.Scanner;

public class CompoundInterestCalculator {
    public static void main(String[] args) {

        //Compound Interest Calculator
        Scanner scanner = new Scanner(System.in);

        double principal;
        double rate;
        int timesCompounded;
        int years;
        double amount;

        System.out.print("Enter the principal amount: ");
        principal = scanner.nextDouble();

        System.out.print("Enter the interest rate (in %): ");
        rate = scanner.nextDouble() / 100;

        System.out.print("Enter the no. of times compounded per year; ");
        timesCompounded = scanner.nextInt();

        System.out.print("Enter the no. of years: ");
        years = scanner.nextInt();

        amount = principal * Math.pow(1 + rate / timesCompounded, years * timesCompounded);

        System.out.printf("The amount after %d is: $%.2f", years, amount);

        scanner.close();
    }
}
