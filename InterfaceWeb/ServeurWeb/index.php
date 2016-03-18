<!DOCTYPE php>
<html>
    <head>
	<title>Interface SMART</title>
	<meta charset="utf-8">
	<META HTTP-EQUIV="Refresh" CONTENT="1; URL=http://localhost/smart/index.php"> 
	<link href="css/style.css" rel="stylesheet" />     <!-- type="text/css" /> -->
    </head>
    <body bgcolor=white>

	<header>
	    <div id="banniere">
		<img src="./img/Smart.png" alt="Smart" id="logo"/>
		
	    </div>
	</header>

	
	<svg xmlns="http://www.w3.org/2000/svg" version="1.1" width=80% height=80%>
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
		$j = 0;
		$nom = "";
		$x = "";
		$y="";
		$z="";
		$angle="";
		
		for($i=0;$i<sizeof($arr1);$i++){
		    if(strcmp($arr1[$i]," ")!=0){
			if ($j==0){
			    $nom .= $arr1[$i];
			}
			elseif ($j==2){
			    $x .= $arr1[$i];
			}
			elseif ( $j==3){
			    $y .= $arr1[$i];
			}
			elseif ( $j==4){
			    $z .= $arr1[$i];
			}
			elseif ( $j==5){
			    $angle .= $arr1[$i];
			}
		    }
		    else{
			$j++;
		    }
		    
		}
		
		$x2 = $x+10000*cos(deg2rad(intval($angle))) ;
		$y2 = $y+10000*sin(deg2rad(intval($angle))) ;
		
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