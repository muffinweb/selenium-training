<?php

$loginUrl = 'https://account.jetbrains.com/login';

$email = $_POST['email'];
$password = $_POST['password'];

$commandToWork = 'python3 jetbrains-license-service.py ' . $email . ' ' . $password;

exec($commandToWork, $output, $result);

if(count($output) == 1){
    echo $output[0];
}
