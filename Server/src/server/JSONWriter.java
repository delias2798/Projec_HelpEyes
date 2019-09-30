package server;

import org.json.JSONObject;

public class JSONWriter {

    public JSONWriter() {
    }

    public JSONObject writeResponse(Response response) {
        JSONObject responseJSON = new JSONObject();

        responseJSON.put("distance", response.distance);
        responseJSON.put("temperature", response.temperature);
        responseJSON.put("humidity", response.humidity);
        responseJSON.put("brightness", response.brightness);
        responseJSON.put("inclination", response.inclination);
        responseJSON.put("sound", response.sound);
        responseJSON.put("vibration", response.vibration);
        responseJSON.put("speed", response.speed);


        return responseJSON;
    }
}
