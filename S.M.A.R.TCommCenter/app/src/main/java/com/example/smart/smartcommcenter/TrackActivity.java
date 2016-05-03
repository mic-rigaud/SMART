package com.example.smart.smartcommcenter;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.MalformedURLException;
import java.net.URL;
import java.net.URLEncoder;

import android.app.Activity;
import android.content.Intent;
import android.os.AsyncTask;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

/**
 * Created by Antoine d'ACREMONT on 19/04/2016.
 */
public class TrackActivity extends Activity {

    TextView reponse;

    @Override
    protected void onCreate(Bundle savedInstanceState){
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_track);

        String addr = "192.168.9.30";
        int port = 5000;

        reponse = ((TextView)findViewById(R.id.textPosition));
        reponse.setText("NO DATA");

        Client monClient = new Client(addr, port, reponse);
        monClient.execute();

        Button buttonStop = (Button) findViewById(R.id.buttonStop);
        buttonStop.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(TrackActivity.this, MainActivity.class);
                startActivity(intent);
            }
        });

        Button buttonLoc = (Button) findViewById(R.id.buttonLoc);
        buttonLoc.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                reponse = ((TextView)findViewById(R.id.textPosition));
                reponse.setText("DRONE DETECTE ! x=24, y=17");


        /*        String addr = "";
                int port = 0000;

                Client monClient = new Client(addr, port, reponse);
                monClient.execute();
        */
            }
        });
    }


}
