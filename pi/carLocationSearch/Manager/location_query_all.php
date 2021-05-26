<?php

// required headers
header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json; charset=UTF-8");


require_once $_SERVER['DOCUMENT_ROOT'] . '/pi/carLocationSearch/Foundation/HelpUtil.php';
require_once $_SERVER['DOCUMENT_ROOT'] . '/pi/carLocationSearch/Foundation/HttpReq.php';
// require_once $_SERVER['DOCUMENT_ROOT'] . '/../../dbConfig/DatabaseConfig.php';
// require_once $_SERVER['DOCUMENT_ROOT'] . '/dbConfig/DatabaseConfig.php';

// $username = DatabaseConfig::$account;
// $password = DatabaseConfig::$password;
$username = 'root';
$password = $_ENV["MYSQL_ROOT_PASSWORD"];
$host = "db";
$db_name = "pi_parking_monitor";
$conn = mysqli_connect($host, $username, $password, $db_name);
mysqli_query($conn,"SET NAMES 'UTF8'");

//query database
$query = "SELECT * FROM `parking_space`";
$result = mysqli_query($conn,$query) or die ('MySQL query 1 error');
$rowNum = $result->num_rows;
mysqli_close($conn);
$message = array();
$idx = 0;
if($rowNum>0){
    while($row = $result->fetch_assoc()){
        $message[$idx]["status"] = 200;
        $message[$idx]["first"] = $row["lisence_plate_head"];
        $message[$idx]["last"] = $row["lisence_plate_tail"];
        $message[$idx]["time"] = $row["update_time"];
        $message[$idx]["location"] = $row["camera_id"];
        $idx = $idx + 1;
    }
}
else{
    $message[$idx]["status"] = 400;
}
$message = json_encode($message);
echo $message;