import java.io.*;
import java.util.ArrayList;
import java.util.Random;
import java.util.Scanner;

public class HangmanGame {
    public static void main(String[] args) {

        // JAVA HANGMAN GAME

        String filePath = "src\\words.txt";
        ArrayList<String> words = new ArrayList<>();

        try (BufferedReader bufferedReader = new BufferedReader(new FileReader(filePath))){
            String line;
            while ((line = bufferedReader.readLine()) != null) {
                words.add(line.trim());
            }
        } catch (FileNotFoundException e){
            System.out.println("Could not find file");
        } catch (IOException e){
            System.out.println("Something went wrong");
        }

        Random random = new Random();

        String word = words.get(random.nextInt(words.size()));


        Scanner scanner = new Scanner(System.in);
        ArrayList<Character> wordState = new ArrayList<>();
        int wrongGuesses = 0;

        for (int i = 0; i < word.length(); i++) {
            wordState.add('_');
        }

        System.out.println("************************");
        System.out.println("Welcome to Java Hangman!");
        System.out.println("************************");

        while (wrongGuesses < 6){
            System.out.print(getHangmanArt(wrongGuesses));
            System.out.print("Word: ");
            for (char c : wordState){
                System.out.print(c + " ");
            }
            System.out.println();

            System.out.print("Guess a letter: ");
            char guess = scanner.next().toLowerCase().charAt(0);

            if(word.indexOf(guess) >= 0){
                System.out.println("Correct guess!");
                for (int i = 0; i < word.length(); i++) {
                    if(word.charAt(i) == guess){
                        wordState.set(i, guess);
                    }
                }
                if(!wordState.contains('_')){
                    System.out.print(getHangmanArt(wrongGuesses));
                    System.out.println("YOU WIN!");
                    System.out.println("The word was: " + word);
                    break;
                }
            } else {
                wrongGuesses++;
                System.out.println("Wrong guess!");
            }
        }

        if(wrongGuesses >= 6){
            System.out.print(getHangmanArt(6));
            System.out.println("GAME OVER!");
            System.out.println("The word was: " + word);
        }

        scanner.close();

    }
    static String getHangmanArt(int wrongGuesses){
        return switch (wrongGuesses) {
            case 0 -> """
                      
                      
                      
                      """;
            case 1 -> """
                       O
                      
                      
                      """;
            case 2 -> """
                       O
                       |
                      
                      """;
            case 3 -> """
                       O
                      /|
                      
                      """;
            case 4 -> """
                       O
                      /|\\
                      
                      """;
            case 5 -> """
                       O
                      /|\\
                      /
                      """;
            case 6 -> """
                       O
                      /|\\
                      / \\
                      """;
            default -> "";
        };
    }
}
