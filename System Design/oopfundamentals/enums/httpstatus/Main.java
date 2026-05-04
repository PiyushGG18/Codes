package oopfundamentals.enums.httpstatus;

enum HttpStatus {
    OK(200, "OK"),
    BAD_REQUEST(400, "Bad Request"),
    NOT_FOUND(404, "Not Found"),
    INTERNAL_SERVER_ERROR(500, "Internal Server Error");

    private int code;
    private final String message;

    HttpStatus(int code, String message) {
        this.code = code;
        this.message = message;
    }

    public int getCode(){
        return code;
    }

    public String getMessage() {
        return message;
    }

    public boolean isSuccess() {
        return code < 400;
    }

    public void display() {
        System.out.println(code + " " + message);
    }

    public static HttpStatus fromCode(int code) {
        for(HttpStatus status : values()) {
            if(status.code == code) {
                return status;
            }
        }
        return null;
    }
}

public class Main {
    public static void main(String[] args) {
        HttpStatus.OK.display();
        HttpStatus.NOT_FOUND.display();

        System.out.println("Is 200 success? " + HttpStatus.OK.isSuccess());
        System.out.println("Is 404 success? " + HttpStatus.NOT_FOUND.isSuccess());

        HttpStatus found = HttpStatus.fromCode(500);
        if(found != null) {
            System.out.print("Found by code 500: ");
            found.display();
        }
    }
}