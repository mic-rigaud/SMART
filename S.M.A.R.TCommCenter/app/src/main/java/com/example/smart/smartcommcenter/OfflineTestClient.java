package com.example.smart.smartcommcenter;

import android.os.AsyncTask;
import android.widget.TextView;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.net.Socket;
import java.net.UnknownHostException;

/**
 * Created by Antoine on 07/05/2016.
 */
public class OfflineTestClient extends AsyncTask<Void, Void, Void> {

    int n;
    String dstAdress;
    int dstPort;
    String reponse;
    TextView textResponse;
    TextView textCoord;

    OfflineTestClient(TextView textResponse, TextView textCoord, int n) {

        String reponse = "141.2223 154.5566";
        this.textResponse = textResponse;
        this.textCoord = textCoord;
        this.n = n;
    }


    @Override
    protected Void doInBackground(Void... arg0) {



        /*
        if (reponse.charAt(0) == '1') {
            textResponse
        }
        */
        ;
        //textResponse.setText("Intrusion Drone");


        return null;
    }

    protected void onPostExecute(Void result) {
        textResponse.setText(reponse);
        super.onPostExecute(result);
    }
}



