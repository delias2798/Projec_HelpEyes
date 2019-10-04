package server;

public class Response {

    public int distance;
    public int temperature;
    public int humidity;
    public int sound;
    public int brightness;
    public int inclination;
    public int vibration;
    public int speed;

    public Response(int distance, int temperature, int humidity, int sound, int brightness, int inclination, int vibration, int speed) {
        this.distance = distance;
        this.temperature = temperature;
        this.humidity = humidity;
        this.sound = sound;
        this.brightness = brightness;
        this.inclination = inclination;
        this.vibration = vibration;
        this.speed = speed;
    }
}
