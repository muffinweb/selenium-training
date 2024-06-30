<?php

$url = $_GET['url'];

exec('python3 scrape.py ' . $url, $output, $result);

if(count($output) == 1){
    $title = $output[0];

    print($url.' sitesinin title değeri: ' . $title);
}

?>