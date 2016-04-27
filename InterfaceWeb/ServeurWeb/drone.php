

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
    
    <text x="<?php echo $x[$k]; ?>" y="<?php echo $y[$k]; ?>"><?php echo $nom[$k]; ?></text>
    <circle cx="<?php echo $x[$k]; ?>" cy="<?php echo $y[$k]; ?>" r="6" fill="blue" />
    <line x1="<?php echo $x[$k]; ?>" y1="<?php echo $y[$k]; ?>" x2="<?php echo $x2[$k]; ?>" y2="<?php echo $y2[$k]; ?>" stroke="red" /> 



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
		$x_intersection[$j] = ($b-$B)/($A-$a);
		$y_intersection[$j] = $A*$x_intersection[$j]+$B;
		$j = $j+1;
	    }
	}
    }

    for($i=0;$i<sizeof($x_intersection);$i++){
	$x_drone = $x_drone + $x_intersection[$i];
	$y_drone = $y_drone + $y_intersection[$i];	
    }
    $x_drone = $x_drone/sizeof($x_intersection);
    $y_drone = $y_drone/sizeof($y_intersection);

    ?>

    <text x="<?php echo $x_drone; ?>" y="<?php echo $y_drone; ?>">DRONE</text>
    <circle cx="<?php echo $x_drone; ?>" cy="<?php echo $y_drone; ?>" r="6" fill="red" />


</svg>

<div id = "liste">
    <p> Liste des Raspberry Pi Connecté </p>
<?php for($k=0;$k<sizeof($nom);$k++){ ?>
	<br> <?php echo $nom[$k] ?> 
<?php } ?>
</div>




<div id="test"></div>
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js"></script>
<script>
 
 $.post("socket.php", function(data){
     /* alert(data); */
    }); 
</script>
