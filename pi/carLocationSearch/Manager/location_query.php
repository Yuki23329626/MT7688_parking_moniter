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
    $firstNumber = $input->firstNumber;
    $lastNumber = $input->lastNumber;

    // $username = DatabaseConfig::$account;
    // $password = DatabaseConfig::$password;
    $username = 'root';
    $password = $_ENV["MYSQL_ROOT_PASSWORD"];
    $host = "db";
    $db_name = "pi_parking_monitor";
    $conn = mysqli_connect($host, $username, $password, $db_name);
    mysqli_query($conn,"SET NAMES 'UTF8'");

    //query database
    $query = "SELECT * FROM `parking_space` WHERE `lisence_plate_head`='$firstNumber' AND `lisence_plate_tail`='$lastNumber'";
    $result = mysqli_query($conn,$query) or die ('MySQL query 1 error');
    $rowNum = $result->num_rows;
    mysqli_close($conn);
    if($rowNum>0){
        $row = $result->fetch_assoc();
        $message = array(
            "status" => "200",
            "first" => $firstNumber,
            "last" => $lastNumber,
            "time" => $row['update_time'],
            "location" => $row['camera_id']
        );
    }
    else{
        $message = array(
            "status" => "400",
            "first" => $firstNumber,
            "last" => $lastNumber,
            "location" => "No car"
        );
    }
    $message = json_encode($message);
    echo $message;
}
else{
    sendResponse(400,'Failed to get parameters');
}