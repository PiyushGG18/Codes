package oopfundamentals.classesandobjects.librarybook;

class Book {
    private String title;
    private String author;
    private String isbn;
    private boolean isAvailable;

    public Book(String title, String author, String isbn) {
        this.title = title;
        this.author = author;
        this.isbn = isbn;
        this.isAvailable = true;
    }

    public boolean borrowBook(){
        if(isAvailable){
            isAvailable = false;
            return true;
        }
        return false;
    }

    public void returnBook(){
        isAvailable = true;
    }

    public void displayInfo(){
        System.out.println(title + " by " + author + " (ISBN: " + isbn + ") - " + (isAvailable?"Available":"Borrowed"));
    }
}

public class Main {
    public static void main(String[] args) {
        Book book = new Book("The Pragmatic Programmer", "David Thomas", "978-0135957059");
        book.displayInfo();

        boolean success = book.borrowBook();
        System.out.println("Borrow successful: " + success);
        book.displayInfo();

        success = book.borrowBook();
        System.out.println("Borrow successful: " + success);

        book.returnBook();
        book.displayInfo();
    }
}
