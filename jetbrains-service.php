<?php

$loginUrl = 'https://account.jetbrains.com/login';

$email = $_POST['email'];
$password = $_POST['password'];

$commandToWork = 'python3 jetbrains-license-service.py ' . $email . ' ' . $password;

exec($commandToWork, $output, $resultErr);

if(count($output) == 1){

    if($resultErr == 0){
        echo $output[0];
    }else{
        echo 'Veri Alinamadi';
        exit(1);
    }
}else {
    echo 'Veri Alinamadi';
    exit(1);
}
