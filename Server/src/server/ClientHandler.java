package server;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.*;
import java.text.*;
import java.net.*;
import java.util.concurrent.TimeUnit;

class ClientHandler extends Thread
{

    final DataInputStream dis;
    final DataOutputStream dos;
    final Socket s;
    public JSONObject virtualJSON;


    // Constructor
    public ClientHandler(Socket s, DataInputStream dis, DataOutputStream dos, JSONObject virtualWorldJSON)
    {
        this.s = s;
        this.dis = dis;
        this.dos = dos;
        this.virtualJSON = virtualWorldJSON;
    }

    @Override
    public void run()
    {

        if(this.virtualJSON != null) {
            System.out.println(virtualJSON.get("clientType"));
            AlertManager alertManager = new AlertManager();
            if (virtualJSON.get("clientType").equals("Compilador")) {
                int inputLength = virtualJSON.length() - 1;
                int keyCounter = 1;
                while (keyCounter <= inputLength) {
                    try {
                        JSONObject serverJSON = alertManager.generateResponse((JSONObject) virtualJSON.get(Integer.toString(keyCounter)));
                        String serverJSONString = serverJSON.toString();
                        BufferedWriter out = new BufferedWriter(new OutputStreamWriter(s.getOutputStream()));
                        System.out.println("Sending Response...");
                        System.out.println(serverJSONString);
                        out.write(serverJSONString + "\n");
                        out.flush();
                        System.out.println("Message sent");
                        TimeUnit.SECONDS.sleep(1);
                        keyCounter++;
                    } catch (IOException e) {
                        e.printStackTrace();
                    } catch (JSONException e) {
                        e.printStackTrace();
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
            }
        } else {
            AlertManager alertManager = new AlertManager();
            try {
                s.setKeepAlive(true);
            } catch (SocketException e) {
                e.printStackTrace();
            }
            System.out.println("Client Connected");
            while(true) {
                try {
                    BufferedReader in = new BufferedReader(new InputStreamReader(s.getInputStream()));
                    String clientMessage = in.readLine();
                    if(clientMessage == "Exit") {
                        s.close();
                        System.out.println("Socket closed");
                        break;
                    } else {
                        JSONObject clientJSON = new JSONObject(clientMessage);
                        System.out.println("Client message: " + clientJSON);
                        JSONObject serverJSON = alertManager.generateResponse(clientJSON);
                        String serverJSONString = serverJSON.toString();
                        BufferedWriter out = new BufferedWriter(new OutputStreamWriter(s.getOutputStream()));
                        System.out.println("Sending Response...");
                        System.out.println(serverJSONString);
                        out.write(serverJSONString);
                        out.flush();
                        System.out.println("Message sent");
                    }
                } catch (IOException e) {
                    e.printStackTrace();
                } catch (JSONException e) {
                    e.printStackTrace();
                }
            }
        }
        try {
            // closing resources
            this.dis.close();
            this.dos.close();
        } catch(IOException e){
            e.printStackTrace();
        }
    }
}
