package server;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.net.ServerSocket;
import java.net.Socket;
import org.json.JSONObject;
import server.AlertManager;

public class Server {

    public static void main(String[] args) throws IOException {

        ServerSocket listener = new ServerSocket(9595);
        AlertManager alertManager = new AlertManager();

        try{
            while(true){
                Socket socket = listener.accept();
                socket.setKeepAlive(true);
                System.out.println("Client Connected");
                try{
                    BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                    String clientMessage = in.readLine();
                    System.out.println("Client message: " + clientMessage);
                    JSONObject clientJSON = new JSONObject(clientMessage);
                    System.out.println("Client JSON: " + clientJSON);
                    System.out.println(clientJSON.get("temperature"));

                    JSONObject serverJSON = alertManager.jsonBuilder();
                    String serverJSONString = serverJSON.toString();

                    BufferedWriter out = new BufferedWriter(new OutputStreamWriter(socket.getOutputStream()));
                    System.out.println("Sending Message...");
                    out.write(serverJSONString);
                    out.flush();
                    System.out.println("Message sent");

                } finally {
                    socket.close();
                    System.out.println("Socket closed");
                }
            }
        } finally {
            listener.close();
        }
    }

}