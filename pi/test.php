<?php
  $server = "mariadb";    # MySQL/MariaDB 伺服器
  $dbuser = "root";       # 使用者帳號
  $dbpassword = $_ENV["MYSQL_ROOT_PASSWORD"]; # 使用者密碼
  $dbname = "pi_parking_monitor";             # 資料庫名稱
  

  // connection
  $mysqli = mysqli_connect($server, $dbuser, $dbpassword, $dbname);

  if(mysqli_connect_errno($mysqli)){
      echo "Failed to connect to MySql: ".mysqli_connect_error();
      return;
  }
  else{
    echo "Successfully connect to MySql";
  }

  $res = mysqli_query($mysqli,"select * as _msg from parking_space");
  $row = mysqli_fetch_assoc($res);
  echo $row["_msg"]."<br>";

  $mysqli = mysqli_connect($server, $dbuser, $dbpassword, $dbname);
  # 查詢資料
  $select_result = $mysqli->query("select * from parking_space");
  print_r($select_result);
  echo "<br>";

  # 遍歷結果,第一種遍歷方法
  echo "<p>第一種遍歷方法：</p>";
  for( $row_no=0; $row_no<$select_result->num_rows; $row_no++)
  {
      $select_result->data_seek($row_no);
      $rows = $select_result->fetch_assoc();

      foreach($rows as $key=>$value)
      {
          echo "$key: $value, ";
      }
      echo "<br>";
  }

  # 遍歷查詢結果，第二種遍歷方法
  $select_result->data_seek(0);
  echo "<p>第二種遍歷方法：</p>";

  while( $row=$select_result->fetch_assoc())
  {
      echo " camera_id: ".$row["camera_id"].", lisence_plate_head: ".$row["lisence_plate_head"].", lisence_plate_tail: ".$row["lisence_plate_tail"];
      echo "<br>";
  }
  echo "<br>";

  # 關閉連線
  $mysqli->close();
    
?>
