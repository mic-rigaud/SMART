package com.example.smart.smartcommcenter;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.net.Socket;
import java.io.Reader;
import java.net.SocketAddress;
import java.net.UnknownHostException;
import android.os.AsyncTask;
import android.widget.TextView;
import java.io.Writer;

import android.app.Activity;
import android.content.Intent;
import android.os.AsyncTask;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;

/**
 * Created by Antoine on 26/04/2016.
 */
public class Client extends AsyncTask<Void, Void, Void>  {
    String dstAdress;
    int dstPort;
    String reponse;
    TextView textResponse;

    Client(String addr, int port, TextView textResponse) {

        dstAdress = addr;
        dstPort = port;
        String reponse = "";
        this.textResponse = textResponse;

    }


    @Override
    protected Void doInBackground(Void... arg0) {

        Socket socket = null;
        BufferedReader input;


        try{

            socket = new Socket(dstAdress, dstPort);

            System.out.println("Demande de connexion");
            input = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            String message_distant = input.readLine();
            System.out.println(message_distant);

            input = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            String message_distant2 = input.readLine();
            System.out.println(message_distant2);




            OutputStream os = socket.getOutputStream();
            OutputStreamWriter osw = new OutputStreamWriter(os);
            BufferedWriter bw = new BufferedWriter(osw);
            System.out.println("Weeeeeee");
            bw.write("Fin");
            bw.flush();


            input.close();
            socket.close();




        } catch (UnknownHostException e) {
            e.printStackTrace();
            reponse = "UnknownHostException : " + e.toString();
        } catch (IOException e){
            e.printStackTrace();
            reponse = "IOException "+ e.toString();
        } finally {
            if (socket != null){
                try {
                    socket.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
        /*
        if (reponse.charAt(0) == '1') {
            textResponse
        }
        */
       ;
        //textResponse.setText("Intrusion Drone");


        return null;
    }
}
