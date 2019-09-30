package server;

import org.json.JSONObject;

public class JSONReader {

    public JSONReader() {
    }

    public Read readMeasures(JSONObject input) {
        Read read = new Read(0,0,0,0,0,0,0, 0);
        if (input.has("distance")) {
            read.distance = Integer.parseInt((String) input.get(("distance")));
        }
        else if (input.has("temperature")) {
            read.temperature = Integer.parseInt((String) input.get(("temperature")));
        }
        else if (input.has("humidity")) {
            read.humidity = Integer.parseInt((String) input.get(("humidity")));
        }
        else if (input.has("sound")) {
            read.sound = Integer.parseInt((String) input.get(("sound")));
        }
        else if (input.has("brightness")) {
            read.brightness = Integer.parseInt((String) input.get(("brightness")));
        }
        else if (input.has("inclination")) {
            read.inclination = Integer.parseInt((String) input.get(("inclination")));
        }
        else if (input.has("vibration")) {
            read.vibration = Integer.parseInt((String) input.get(("vibration")));
        }
        else if (input.has("speed")) {
            read.speed = Integer.parseInt((String) input.get(("speed")));
        }
        return read;
    }
}
