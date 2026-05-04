package oopfundamentals.classesandobjects.bankaccount;

class BankAccount {
    private String accountNumber, ownerName;
    private double balance;

    public BankAccount(String accountNumber, String ownerName){
        this.accountNumber = accountNumber;
        this.ownerName = ownerName;
        this.balance = 0;
    }

    public void deposit(double amount) {
        if(amount > 0) {
            balance += amount;
        }
    }

    public boolean withdraw(double amount) {
        if(amount != 0 && amount <= balance) {
            balance -= amount;
            return true;
        }

        return false;
    }

    public double getBalance() {
        return balance;
    }
}

public class Main {
    public static void main(String[] args){
        BankAccount account = new BankAccount("123456", "John Doe");
        account.deposit(1000);
        System.out.println(account.getBalance());

        boolean success = account.withdraw(500);
        System.out.println(success);
        System.out.println(account.getBalance());

        success = account.withdraw(1000);
        System.out.println(success);
    }
}