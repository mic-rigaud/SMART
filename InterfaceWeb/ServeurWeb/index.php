<!DOCTYPE php>
<html>
    <head>
	<title>Interface SMART</title>
	<meta charset="utf-8">
	<link href="css/style.css" rel="stylesheet" />     <!-- type="text/css" /> -->
    </head>
    <body bgcolor=white>
	
	<header>
	    <div id="banniere">
		<img src="./img/Smart.png" alt="Smart" id="logo"/>
		
	    </div>
	</header>

	<div id="message"></div>
	
	<script src="http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js"></script>
	<script>
	    $(function(){
	    affiche();

	    function affiche(){
		$('#message').load('drone.php');
	    }
	    
	    setInterval(affiche,4000);
	    });
	</script>
	
    </body>
</html>
