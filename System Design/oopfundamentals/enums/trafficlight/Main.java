package oopfundamentals.enums.trafficlight;

enum TrafficLight {
    RED(30),
    YELLOW(5),
    GREEN(25);

    private final int duration;

    TrafficLight(int duration) {
        this.duration = duration;
    }

    public int getDuration() {
        return duration;
    }

    public TrafficLight next() {
        switch (this) {
            case RED: return GREEN;
            case GREEN: return YELLOW;
            case YELLOW: return RED;
            default: return this;
        }
    }

    public void display() {
        System.out.println(this.name() + " (" + duration + "s)");
    }
}

public class Main{
    public static void main(String[] args) {
        TrafficLight light = TrafficLight.RED;
        for(int i=0; i < 6; i++){
            light.display();
            light = light.next();
        }
    }
}