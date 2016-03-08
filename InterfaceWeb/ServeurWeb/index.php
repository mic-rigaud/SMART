<!DOCTYPE html>
<html>
  <head>
    <title>Interface SMART</title>
    <meta charset="utf-8">
  </head>
  <body bgcolor=white>
    
    
    <svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="2000" height="2000">
      <title>Exemple simple de figure SVG</title>
      <desc>
	Cette figure est constituée d'un rectangle,
	d'un segment de droite et d'un cercle.
      </desc>
      
      <!-- <rect width="100" height="80" x="0" y="70" fill="green" /> -->
      <!-- <line x1="5" y1="5" x2="250" y2="95" stroke="red" /> -->
      <!-- <circle cx="90" cy="80" r="50" fill="blue" /> -->


    <?php
       // 1 : on ouvre le fichier
       $monfichier = fopen('../Serveur/position', 'r');
       
       // 2 : on lit la première ligne du fichier
       $ligne = fgets($monfichier);


       while (!feof($monfichier)) { //on parcourt toutes les lignes
       $arr1 = str_split($ligne,1);
       $i = 0;
       $nom = "";
       $x = "";
       $y="";
       $z="";
       $angle="";
       


       while (strcmp($arr1[$i]," ")!=0){
       $nom .= $arr1[$i];
       $i++;
       }
       $i++;
       $i++;
       $i++;
       
       while (strcmp($arr1[$i]," ")!=0){
       $x .= $arr1[$i];
       $i++;
       }
       $i++;

       while (strcmp($arr1[$i]," ")!=0){
       $y .= $arr1[$i];
       $i++;
       }
       $i++;

       while (strcmp($arr1[$i]," ")!=0){
       $z .= $arr1[$i];
       $i++;
       }
       $i++;
       
       while (strcmp($arr1[$i]," ")!=0 AND $i!=sizeof($arr1)){
       $angle .= $arr1[$i];
       $i++;
       }
       
       $x2 = $x+1000*cos(deg2rad($angle)) ;
       $y2 = $y+1000*sin(deg2rad($angle)) ;

       ?>
    
    <text x="<?php echo $x; ?>" y="<?php echo $y; ?>"><?php echo $nom; ?></text>
    <circle cx="<?php echo $x; ?>" cy="<?php echo $y; ?>" r="6" fill="blue" />
    <line x1="<?php echo $x; ?>" y1="<?php echo $y; ?>" x2="<?php echo $x2; ?>" y2="<?php echo $y2; ?>" stroke="red" /> 


    <?php
       $ligne = fgets($monfichier);
       }
       fclose($monfichier);
       ?>
    </svg>


  </body>
</html>
