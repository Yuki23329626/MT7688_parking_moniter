<?php

// required headers
header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json; charset=UTF-8");


require_once $_SERVER['DOCUMENT_ROOT'] . '/pi/carLocationSearch/Foundation/HelpUtil.php';
require_once $_SERVER['DOCUMENT_ROOT'] . '/pi/carLocationSearch/Foundation/HttpReq.php';
// require_once $_SERVER['DOCUMENT_ROOT'] . '/../../dbConfig/DatabaseConfig.php';
// require_once $_SERVER['DOCUMENT_ROOT'] . '/dbConfig/DatabaseConfig.php';

// get post body
$inputJSON = file_get_contents('php://input');
$input= json_decode( $inputJSON );

if( isset($input) ) {
    $firstNumber = $input->lisence_plate_head;
    $lastNumber = $input->lisence_plate_tail;
    $location = $input->camera_id;

    // $username = DatabaseConfig::$account;
    // $password = DatabaseConfig::$password;
    $username = 'root';
    $password = $_ENV["MYSQL_ROOT_PASSWORD"];
    $host = "db";
    $db_name = "pi_parking_monitor";
    $conn = mysqli_connect($host, $username, $password, $db_name);
    mysqli_query($conn,"SET NAMES 'UTF8'");

    //query database
    $query = "UPDATE `parking_space` SET `lisence_plate_head`='$firstNumber', `lisence_plate_tail`='$lastNumber' WHERE `camera_id`='$location'";
    $result = mysqli_query($conn,$query) or die ('MySQL query 2 error');

    if(mysqli_affected_rows($conn)>0){
        $message = array(
            "status" => "200",
            "comment"  => "update successful.",
            "first" => $firstNumber,
            "last" => $lastNumber,
            "location" => $location
        );
    }
    else{
        $message = array(
            "status" => "400",
            "comment" => "update error, the same license plate.",
            "first" => $firstNumber,
            "last" => $lastNumber,
            "location" => $location
        );
    }
    mysqli_close($conn);
    $message = json_encode($message);
    echo $message;
}
else{
    sendResponse(400,'Failed to get parameters');
}