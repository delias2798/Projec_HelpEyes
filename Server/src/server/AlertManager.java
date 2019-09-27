package server;

import org.json.JSONArray;
import org.json.JSONObject;

public class AlertManager {

    public JSONObject entry;

    public AlertManager() {
        entry = new JSONObject();
    }

    public JSONObject jsonBuilder() {
        JSONObject object = new JSONObject();
        object.put("distance", 0);
        object.put("temperature", 2);
        object.put("brightness", 1);
        object.put("inclination", 3);
        object.put("sound", 3);

        return object;
    }


}
