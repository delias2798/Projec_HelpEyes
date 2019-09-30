package server;

import org.json.JSONObject;

import java.io.*;
import java.net.*;

public class Server {


    public static void main(String[] args) throws IOException {

        boolean realWorld = false;
        JSONObject virtualWorldJSON = null;

        if(realWorld) {
            ServerSocket serverSocketWemos = new ServerSocket(9595);
            // running infinite loop for getting
            // client request
            while (true) {
                Socket s = null;

                try {


                    // socket object to receive incoming client requests
                    s = serverSocketWemos.accept();

                    System.out.println("A new wemos is connected : " + s);

                    // obtaining input and out streams
                    DataInputStream dis = new DataInputStream(s.getInputStream());
                    DataOutputStream dos = new DataOutputStream(s.getOutputStream());

                    System.out.println("Assigning new thread for this wemos");

                    // create a new thread object
                    Thread t = new ClientHandler(s, dis, dos, virtualWorldJSON);

                    // Invoking the start() method
                    t.start();

                } catch (Exception e) {
                    s.close();
                    e.printStackTrace();
                }
            }
        } else {
            ServerSocket serverSocketComp = new ServerSocket(8787);
            try{
                while(true){
                    Socket socket = serverSocketComp.accept();
                    socket.setKeepAlive(true);
                    System.out.println("Client Connected");
                    try{
                        BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                        String clientMessage = in.readLine();
                        System.out.println("Client message: " + clientMessage);
                        virtualWorldJSON = new JSONObject(clientMessage);
                        System.out.println("Virtual JSON: " + virtualWorldJSON.toString());

                        BufferedWriter out = new BufferedWriter(new OutputStreamWriter(socket.getOutputStream()));
                        System.out.println("Sending Response...");
                        out.write("Got it");
                        out.flush();
                        System.out.println("Message sent");

                    } finally {
                        socket.close();
                        System.out.println("Socket closed");
                        ServerSocket serverSocketWemos = new ServerSocket(9595);
                        // running infinite loop for getting
                        // client request
                        while (true) {
                            Socket s = null;
                            try {


                                // socket object to receive incoming client requests
                                s = serverSocketWemos.accept();

                                System.out.println("A new wemos is connected : " + s);

                                // obtaining input and out streams
                                DataInputStream dis = new DataInputStream(s.getInputStream());
                                DataOutputStream dos = new DataOutputStream(s.getOutputStream());

                                System.out.println("Assigning new thread for this wemos");

                                // create a new thread object
                                Thread t = new ClientHandler(s, dis, dos, virtualWorldJSON);

                                // Invoking the start() method
                                t.start();

                            } catch (Exception e) {
                                s.close();
                                e.printStackTrace();
                            }
                        }
                    }
                }
            } finally {
                serverSocketComp.close();
            }
        }
    }
}