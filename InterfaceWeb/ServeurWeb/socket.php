
<?php

$socket = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
if ($socket === false) {
    echo "socket_create() a échoué : raison :  " . socket_strerror(socket_last_error()) . "\n";
} else {
    echo "OK.\n";
}
$address = "192.168.1.56";
$service_port = 5000;
$result = 0;
$result = socket_connect($socket, $address, $service_port);
if ($socket === false or $result == 0) {
    echo "socket_connect() a échoué : raison : ($result) " . socket_strerror(socket_last_error($socket)) . "\n";
} else {
    echo "OK.\n";

    $msg = 'tata';
    socket_write($socket, $msg, strlen($msg));
    //on ferme la socket
    socket_close($socket);
}
?> 
