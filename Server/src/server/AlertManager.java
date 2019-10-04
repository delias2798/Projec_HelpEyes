package server;

import org.json.JSONArray;
import org.json.JSONObject;
import java.util.concurrent.TimeUnit;

public class AlertManager {

    public JSONObject responseJSON;
    public Read read;
    public Response response;
    public JSONWriter jsonWriter;
    public JSONReader jsonReader;

    public AlertManager() {

        this.responseJSON = new JSONObject();
        this.response = new Response(0,0,0,0,0,0,0, 0);
        this.jsonWriter = new JSONWriter();
        this.jsonReader = new JSONReader();
    }

    public JSONObject generateResponse(JSONObject input) {
        this.read = jsonReader.readMeasures(input);
        if(this.read.distance > 1000) {
            this.response.distance = 0;
        }
        else if(this.read.distance >= 151) {
            this.response.distance = 1;
        }
        else if(this.read.distance >= 51) {
            this.response.distance = 2;
        }
        else if(this.read.distance >= 5) {
            this.response.distance = 3;
        }
        if(this.read.temperature <= 25) {
            this.response.temperature = 0;
        }
        else if(this.read.temperature <= 35) {
            this.response.temperature = 1;
        }
        else if(this.read.temperature <= 50) {
            this.response.temperature = 2;
        }
        else {
            this.response.temperature = 3;
        }
        if(this.read.humidity <= 20) {
            this.response.humidity = 0;
        }
        else if(this.read.humidity <= 45) {
            this.response.humidity = 1;
        }
        else if(this.read.humidity <= 60) {
            this.response.humidity = 2;
        }
        else {
            this.response.humidity = 3;
        }
        if(this.read.sound <= 10) {
            this.response.sound = 0;
        }
        else if(this.read.sound <= 30) {
            this.response.sound = 1;
        }
        else if(this.read.sound <= 50) {
            this.response.sound = 2;
        }
        else {
            this.response.sound = 3;
        }
        if(this.read.brightness > 50) {
            this.response.brightness = 0;
        }
        else {
            this.response.brightness = 1;
        }
        if(this.read.inclination <= 10) {
            this.response.inclination = 0;
        }
        else if(this.read.inclination <= 20) {
            this.response.inclination = 1;
        }
        else if(this.read.inclination <= 50) {
            this.response.inclination = 2;
        }
        else if(this.read.inclination <= 90) {
            this.response.inclination = 3;
        }
        if(this.read.vibration <= 100) {
            this.response.vibration = 0;
        }
        else if(this.read.vibration <= 300) {
            this.response.vibration = 1;
        }
        else if(this.read.vibration <= 500) {
            this.response.vibration = 2;
        }
        else {
            this.response.vibration = 3;
        }
        if(this.read.speed == 0) {
            this.response.speed = 0;
        }
        else if(this.read.speed >= 1 && this.read.speed <= 10) {
            this.response.speed = 1;
        }
        else if(this.read.speed >= 11 && this.read.speed <= 20) {
            this.response.speed = 2;
        }
        else if(this.read.speed >= 21) {
            this.response.speed = 3;
        }
        this.responseJSON = this.jsonWriter.writeResponse(this.response);
        return responseJSON;
    }




}
