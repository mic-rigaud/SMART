

<svg xmlns="http://www.w3.org/2000/svg" version="1.1" width=80% height=80% >
    <title>SMART: champ de capteur</title>
    <desc>
	Cette figure représente notre champ de capteur avec la detection d'un drone.
    </desc>
    
	    <?php
	    //$_POST["lat"]
	    // 1 : on ouvre le fichier
	    $monfichier = fopen('../Serveur/position', 'r');
	    
	    // 2 : on lit la première ligne du fichier
	    $ligne = fgets($monfichier);
	    
	    $x = array();
	    $y= array();
	    $z= array();
	    $angle = array();
	    $x2 = array();
	    $y2 = array();
	    $k = 0;
	    $nom = array();

	    while (!feof($monfichier)) { //on parcourt toutes les lignes
		$arr1 = str_split($ligne,1);
		$i = 0;
		$j = 0;
		
		for($i=0;$i<sizeof($arr1);$i++){
		    if(strcmp($arr1[$i]," ")!=0){
			if ($j==0){
			    $nom[$k] .= $arr1[$i];
			}
			elseif ($j==2){
			    $x[$k] .= $arr1[$i];
			}
			elseif ( $j==3){
			    $y[$k] .= $arr1[$i];
			}
			elseif ( $j==4){
			    $z[$k] .= $arr1[$i];
			}
			elseif ( $j==5){
			    $angle[$k] .= $arr1[$i];
			}
		    }
		    else{
			$j++;
		    }
		    
		}
		if($angle[$k]!=360){
		    $x2[$k] = $x[$k]+400*cos(deg2rad(intval($angle[$k]))) ;
		    $y2[$k] = $y[$k]+400*sin(deg2rad(intval($angle[$k]))) ;
		}
		else{
		    $x2[$k] = $x[$k];
		    $y2[$k] = $y[$k];
		}
		
	    ?>
    
    <text x=<?php echo ($x[$k]*100)/1600; ?>% y=<?php echo ($y[$k]*100)/800; ?>%><?php echo $nom[$k]; ?></text>
    <circle cx=<?php echo ($x[$k]*100)/1600; ?>% cy=<?php echo ($y[$k]*100)/800; ?>% r="6" fill="blue" />
    <line x1=<?php echo ($x[$k]*100)/1600; ?>% y1=<?php echo ($y[$k]*100)/800; ?>% x2=<?php echo ($x2[$k]*100)/1600; ?>% y2=<?php echo ($y2[$k]*100)/800; ?>% stroke="red" /> 



    <?php
    $ligne = fgets($monfichier);
    $k = $k+1;
    }

    fclose($monfichier);

    $x_drone = 0;
    $y_drone = 0;
    $x_intersection = array();
    $y_intersection = array();
    $k = 0;
    $i = 0;
    $j = 0;
    
    for($i=0;$i<sizeof($x);$i++){
	for($k=$i+1;$k<sizeof($x);$k++){
	    if($x[$k]!=$x2[$k] and $x[$i]!=$x2[$i]){
		$a = ($y[$i]-$y2[$i])/($x[$i]-$x2[$i]);
		$A = ($y[$k]-$y2[$k])/($x[$k]-$x2[$k]);
		$b = $y[$i]-$a*$x[$i];
		$B = $y[$k]-$A*$x[$k];
		if($a!=$A){
		    $x_intersection[$j] = ($b-$B)/($A-$a);
		    $y_intersection[$j] = $A*$x_intersection[$j]+$B;
		    $j = $j+1;
		}
	    }
	}
    }

    $x_sort = $x_intersection;
    sort($x_sort);
    $y_sort = $y_intersection;
    sort($y_sort);
    $x_mediane = $x_sort[(int)(sizeof($x_sort)/2)];
    $y_mediane = $y_sort[(int)(sizeof($y_sort)/2)];

    $x_intersectionF =[];
    $j=0;
    for($i=0;$i<sizeof($x_intersection);$i++){
	if (sqrt(pow(($x_mediane - $x_intersection[$i]),2)+pow(($y_mediane - $y_intersection[$i]),2))<50){
	    $x_intersectionF[$j]=$x_intersection[$i];
	    $y_intersectionF[$j]=$y_intersection[$i];
	    $j=$j+1;
	}
    }


    for($i=0;$i<sizeof($x_intersectionF);$i++){
	$x_drone = $x_drone + $x_intersectionF[$i];
	$y_drone = $y_drone + $y_intersectionF[$i];	
    ?>
	<circle cx=<?php echo ($x_intersectionF[$i]*100)/1600; ?>% cy=<?php echo ($y_intersectionF[$i]*100)/800; ?>% r="3" fill="green" />
	
    <?php 
    }
    $x_drone = $x_drone/sizeof($x_intersectionF);
    $y_drone = $y_drone/sizeof($y_intersectionF);





    ?>

    <text x=<?php echo ($x_drone*100)/1600; ?>% y=<?php echo ($y_drone*100)/800; ?>%>DRONE</text>
    <circle cx=<?php echo ($x_drone*100)/1600; ?>% cy=<?php echo ($y_drone*100)/800; ?>% r="6" fill="red" />

</svg>

<div id = "liste">
    <p> Liste des Raspberry Pi Connecté </p>
    <?php 
    sort($nom,SORT_NATURAL);
    for($k=0;$k<sizeof($nom);$k++){ ?>

	<br> <?php echo $nom[$k] ?> 
    <?php } ?>
</div>

<?php 
$monfichier = fopen('../Serveur/detection', 'r+');
fseek($monfichier, 0);
if(sizeof($x_intersectionF)!=0){
    $mot = "1 " . $x_drone . " " . $y_drone;
    fputs($monfichier,"                                                                       ");
    fseek($monfichier, 0);
    fputs($monfichier,$mot);
}
else{
    fputs($monfichier,"                                                                       ");
    fseek($monfichier, 0);
    fputs($monfichier,"0");
}
fclose($monfichier);
?>


