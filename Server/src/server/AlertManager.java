package server;

import org.json.JSONArray;
import org.json.JSONObject;

public class AlertManager {

    JSONObject response;

    public AlertManager() {
        response = new JSONObject();
    }

    public JSONObject generateResponse(JSONObject input) {
        System.out.println(input.get("clientType"));
        if (input.get("clientType").equals("compilador")) {
            int inputLength = input.length();
            int keyCounter = 1;
            JSONObject response = new JSONObject();

            response.put("distance", 100);
            response.put("temperature", 3);
            response.put("brightness", 3);
            response.put("inclination", 3);
            response.put("sound", 3);


            return response;
        } else {
            JSONObject response = new JSONObject();

            response.put("distance", 3);
            response.put("temperature", 3);
            response.put("brightness", 3);
            response.put("inclination", 3);
            response.put("sound", 3);

            return response;
        }
    }




}
