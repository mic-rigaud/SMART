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
import android.widget.ImageView;
import android.widget.TextView;

/*
 * Created by Antoine d'ACREMONT on 19/04/2016.
 */
public class TrackActivity extends Activity {

    TextView reponse;
    TextView position;
    ImageView warning;

    @Override
    protected void onCreate(Bundle savedInstanceState){
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_track);

        String addr = "192.168.9.30";
        int port = 6666;

        warning = ((ImageView)findViewById(R.id.imageWarning));
        warning.setVisibility(View.INVISIBLE);

        reponse = ((TextView)findViewById(R.id.textPosition));
        reponse.setText("R.A.S");

        position = ((TextView)findViewById(R.id.textCoord));
        position.setText("Aucune donnée");

        /*
        Client monClient = new Client(addr, port, reponse);
        monClient.execute();
        */

        OfflineTestClient monClientOffline = new OfflineTestClient(reponse, position, 1);
        monClientOffline.execute();


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

                /*
                // Cette portion de code est uniquement utile si on cherche à donner un apperçu de
                // l'affichage des données


                reponse = ((TextView)findViewById(R.id.textPosition));
                reponse.setText("Intrusion Drone");

                position = ((TextView)findViewById(R.id.textCoord));
                position.setText("X=... / Y=...");

                warning = ((ImageView)findViewById(R.id.imageWarning));
                warning.setVisibility(View.
                        VISIBLE);
                */


                OfflineTestClient monClientOffline = new OfflineTestClient(reponse, position, 2);
                monClientOffline.execute();


                /*

                String addr = "192.168.9.30";
                int port = 6666;

                Client monClient = new Client(addr, port, reponse);
                monClient.execute();
                */
            }
        });
    }


}
