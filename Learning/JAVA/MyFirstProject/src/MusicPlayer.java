import javax.sound.sampled.*;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Random;
import java.util.Scanner;

public class MusicPlayer {
    public static void main(String[] args) {

        // How to PLAY AUDIO with JAVA (.wav, .au, .aiff)
        // Kriss ka ganna sunega??

        String filePath = getPath();
        Clip clip = getClip(filePath);
        if (clip == null) {
            System.out.println("Failed to load audio clip");
            return;
        }
        startPlayer(clip);
        System.out.println("Thank you for listening!");
    }

    static void startPlayer(Clip clip){
        Scanner scanner = new Scanner(System.in);
        String response = "";
        while(!response.equals("Q")) {
            System.out.println("P = Play");
            System.out.println("N = Next");
            System.out.println("S = Stop");
            System.out.println("R = Reset");
            System.out.println("Q = Quit");
            System.out.print("Enter your choice: ");

            response = scanner.next().toUpperCase();

            switch (response){
                case "P" -> clip.start();
                case "N" -> {
                    clip.stop();
                    clip = getClip(getPath());
                    if (clip == null) {
                        System.out.println("Failed to load audio clip");
                        return;
                    }
                    clip.start();
                }
                case "S" -> clip.stop();
                case "R" -> clip.setMicrosecondPosition(0);
                case "Q" -> clip.close();
                default -> System.out.println("Invalid choice.");
            }
        }
        scanner.close();
    }

    static Clip getClip(String filePath) {
        File file = new File(filePath);
        try (AudioInputStream audioStream = AudioSystem.getAudioInputStream(file)){
            Clip clip = AudioSystem.getClip();
            clip.open(audioStream);

            return clip;
        } catch (FileNotFoundException e){
            System.out.println("Could not locate file");
        } catch (LineUnavailableException e){
            System.out.println("Unable to access audio source");
        } catch (UnsupportedAudioFileException e) {
            System.out.println("Audio file is not supported");
        } catch (IOException e){
            System.out.println("Something went wrong");
        }

        return null;
    }

    static String getPath(){
        Random random = new Random();
        return "src\\songs\\music" + random.nextInt(1, 6) + ".wav";
    }
}
