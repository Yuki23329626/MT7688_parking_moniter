<!DOCTYPE html>
<html lang="en">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <title>停車位置查詢</title>
    <style>
        body, html{
            width: 99%;
            height: 98%;
            font-family: "Times New Roman",標楷體;
        }
        /*Header*/
        .header {
            width: 100%;
            height: 10%;
            text-align: center;
            background: white;
        }
        .row{
            height: 90%;
        }
        /* Create columns*/
        .leftcolumn {
            float: left;
            width: 24%;
            text-align: center;
            border-width: 2px;
            border-color: #000000;
            border-style: solid;
            height: inherit;
        }
        /* Right column */
        .rightcolumn {
            float: left;
            width: 75%;
            height: inherit;
            text-align: center;
            border-width: 2px;
            border-color: #000000;
            border-style: solid;
        }
        /* car map*/
        .peripheral_up {
            width: 100%;
            border-color: #000000;
            border-style: solid;
            border-width: 2px;
            border-bottom-color: #ffffff;
        }
        .peripheral_down{
            width: 100%;
            border-color: #000000;
            border-style: solid;
            border-width: 2px;
            border-top-color: #ffffff;
        }
        .parking_grid {
            width: 100%;
            height: 200px;
        }
        .lane {
            width: 100%;
            height: 50px;
        }
        .car_map{
            margin-left: auto;
            margin-right: auto;
            height: inherit;
            padding-top: 10px;
            padding-bottom: 10px;
            width: 60%;
        }
        .icon{
            height: 100%;
            width: 33.33%;
            float: left;
        }
        .icon_table{
            height: inherit;
            width: 100%;
            table-layout: fixed;
            font-size: 10px;
        }
    </style>
</head>
<body>
<div class="header">
    <table style="height: 100%; width: 100%">
        <tr>
            <td style="width: 72px; height: 100% text-align: center;">
                <a href="../index.html" style="width: 100%; height: 100%">
                    <img src="img/home_icon.png" border="0" width="72">
                </a>
            </td>
            <td style="text-align: center; height: 100%; font-size: 40px;">停車位置查詢系統</td>
        </tr>
    </table>
</div>
<div class="row">
    <div class="leftcolumn">
        <table style="height: 100%; width: 100%;">
            <tr style="height: 15%; width: 100%;">
                <td style="font-size: 36px">
                    <?php
                    if (!isset($_POST['submitButton'])){
                        echo "請輸入您的車牌";
                    }
                    else{
                        echo "您的停車位置";
                    }
                    ?>
                </td>
            </tr>
            <tr style="height: 45%; width: 100%;">
                <td colspan="6" style="font-size: 60px">
                    <?php

                    require_once $_SERVER['DOCUMENT_ROOT'] . '/pi/carLocationSearch/Foundation/HttpReq.php';
                    require_once $_SERVER['DOCUMENT_ROOT'] . '/pi/carLocationSearch/Foundation/Config.php';

                    if (isset($_POST['submitButton'])){

                        $firstNumber = $_POST['firstNumber'];
                        $lastNumber = $_POST['lastNumber'];

                        if (!empty($firstNumber) and !empty($lastNumber)){
                            //post to query
                            $url = Config::$ipUrl.'pi/carLocationSearch/Manager/location_query.php';
                            $message = array(
                                "firstNumber" => $firstNumber,
                                "lastNumber" => $lastNumber,
                            );

                            $message = json_encode($message);
                            $result = HttpReq::httpPost($url, $message);

                            $decodeMessage = json_decode($result);

                            echo $decodeMessage->location;
                        }
                    }
                    ?>
                </td>
            </tr>
            <tr style="height: 15%; width: 100%;">
                <td>
                    <div class="icon">
                        <table class="icon_table" border="1">
                            <tr>
                                <td bgcolor="red"></td>
                                <td >車<br>輛</td>
                            </tr>
                        </table>
                    </div>
                    <div class="icon">
                        <table class="icon_table" border="1">
                            <tr>
                                <td bgcolor="white"></td>
                                <td>空<br>車<br>位</td>
                            </tr>
                        </table>
                    </div>
                    <div class="icon">
                        <table class="icon_table" border="1">
                            <tr>
                                <td bgcolor="green"></td>
                                <td>您<br>的<br>愛<br>車</td>
                            </tr>
                        </table>
                    </div>
                </td>
            </tr>
            <tr style="height: 5%; width: 100%;">
                <td colspan="6">
                    <hr size="2px" color="black">
                </td>
            </tr>
            <tr style="height: 20%; width: 100%;">
                <td colspan="6">
                    <?php
                    if (isset($_POST['submitButton'])){
                        $firstNumber = $_POST['firstNumber'];
                        $lastNumber = $_POST['lastNumber'];
                    }
                    else{
                        $firstNumber = "";
                        $lastNumber = "";
                    }
                    echo "<form id='query' method='post' style='font-size: 20px'>
                        車牌號碼：<input type='text' name='firstNumber' value='".$firstNumber."'
                                    style='width:65px; font-size: 20px; padding: 2px;' maxlength='4'> -
                        <input type='text' name='lastNumber' value='".$lastNumber."'
                               style='width:65px; font-size: 20px; padding: 2px;' maxlength='4'>
                        <input type='submit' name='submitButton' value='查詢' style='font-size: 20px'>
                    </form>";
                    ?>
                </td>
            </tr>
        </table>
    </div>
    <div class="rightcolumn">
        <div class="car_map">
            <table class="peripheral_up">
                <tr>
                    <td style="width: 60px">&dArr;</td>
                    <td>
                        <table class="lane">
                            <tr>
                                <td>&lArr; 遵行方向 &lArr;</td>
                            </tr>
                        </table>
                        <?php

                        require_once $_SERVER['DOCUMENT_ROOT'] . '/pi/carLocationSearch/Foundation/Config.php';

                        $url = Config::$ipUrl.'pi/carLocationSearch/Manager/location_query_all.php';

                        $result = HttpReq::httpGet($url);

                        $decodeMessage = json_decode($result);

                        $parkingColer = array();

                        if ($decodeMessage[0]->status == "200"){
                            if (isset($_POST['submitButton'])){
                                $firstNumber = $_POST['firstNumber'];
                                $lastNumber = $_POST['lastNumber'];

                                for ($i=0;$i<16;$i++){
                                    if (empty($decodeMessage[$i]->first)){
                                        $parkingColer[$i] = "white";
                                    }
                                    elseif ($decodeMessage[$i]->first == $firstNumber && $decodeMessage[$i]->last == $lastNumber){
                                        $parkingColer[$i] = "green";
                                    }
                                    else{
                                        $parkingColer[$i] = "red";
                                    }
                                }
                            }
                            else{
                                for ($i=0;$i<16;$i++){
                                    if (empty($decodeMessage[$i]->first)){
                                        $parkingColer[$i] = "white";
                                    }
                                    else{
                                        $parkingColer[$i] = "red";
                                    }
                                }
                            }
                        }
                        else{
                            for ($i=0;$i<16;$i++){
                                $parkingColer[$i] = "white";
                            }
                        }

                        echo "<table class='parking_grid' cellpadding='5' border='1'>
                            <tr>
                                <td bgcolor='".$parkingColer[0]."'>A01</td>
                                <td bgcolor='".$parkingColer[1]."'>A02</td>
                                <td bgcolor='".$parkingColer[2]."'>A03</td>
                                <td bgcolor='".$parkingColer[3]."'>A04</td>
                                <td bgcolor='".$parkingColer[4]."'>A05</td>
                                <td bgcolor='".$parkingColer[5]."'>A06</td>
                                <td bgcolor='".$parkingColer[6]."'>A07</td>
                                <td bgcolor='".$parkingColer[7]."'>A08</td>
                            </tr>
                            <tr>
                                <td bgcolor='".$parkingColer[8]."'>A09</td>
                                <td bgcolor='".$parkingColer[9]."'>A10</td>
                                <td bgcolor='".$parkingColer[10]."'>A11</td>
                                <td bgcolor='".$parkingColer[11]."'>A12</td>
                                <td bgcolor='".$parkingColer[12]."'>A13</td>
                                <td bgcolor='".$parkingColer[13]."'>A14</td>
                                <td bgcolor='".$parkingColer[14]."'>A15</td>
                                <td bgcolor='".$parkingColer[15]."'>A16</td>
                            </tr>
                        </table>";
                        ?>
                    </td>
                    <td style="width: 60px">&uArr;</td>
                </tr>
            </table>
            <table class="lane">
                <tr>
                    <td style="text-align: left">入口&nbsp;&nbsp;&rArr;</td>
                    <td>&rArr; 遵行方向 &rArr;</td>
                    <td style="text-align: right">出口&nbsp;&nbsp;&rArr;</td>
                </tr>
            </table>
            <table class="peripheral_down">
                <tr>
                    <td style="width: 60px">&uArr;</td>
                    <td>
                        <?php

                        require_once $_SERVER['DOCUMENT_ROOT'] . '/pi/carLocationSearch/Foundation/Config.php';

                        $url = Config::$ipUrl.'pi/carLocationSearch/Manager/location_query_all.php';

                        $result = HttpReq::httpGet($url);

                        $decodeMessage = json_decode($result);

                        $parkingColer = array();

                        if ($decodeMessage[0]->status == "200"){
                            if (isset($_POST['submitButton'])){
                                $firstNumber = $_POST['firstNumber'];
                                $lastNumber = $_POST['lastNumber'];

                                for ($i=0;$i<16;$i++){
                                    if (empty($decodeMessage[$i+16]->first)){
                                        $parkingColer[$i] = "white";
                                    }
                                    elseif ($decodeMessage[$i+16]->first == $firstNumber && $decodeMessage[$i+16]->last == $lastNumber){
                                        $parkingColer[$i] = "green";
                                    }
                                    else{
                                        $parkingColer[$i] = "red";
                                    }
                                }
                            }
                            else{
                                for ($i=0;$i<16;$i++){
                                    if (empty($decodeMessage[$i+16]->first)){
                                        $parkingColer[$i] = "white";
                                    }
                                    else{
                                        $parkingColer[$i] = "red";
                                    }
                                }
                            }
                        }
                        else{
                            for ($i=0;$i<16;$i++){
                                $parkingColer[$i] = "white";
                            }
                        }

                        echo "<table class='parking_grid' cellpadding='5' border='1'>
                            <tr>
                                <td bgcolor='".$parkingColer[0]."'>B01</td>
                                <td bgcolor='".$parkingColer[1]."'>B02</td>
                                <td bgcolor='".$parkingColer[2]."'>B03</td>
                                <td bgcolor='".$parkingColer[3]."'>B04</td>
                                <td bgcolor='".$parkingColer[4]."'>B05</td>
                                <td bgcolor='".$parkingColer[5]."'>B06</td>
                                <td bgcolor='".$parkingColer[6]."'>B07</td>
                                <td bgcolor='".$parkingColer[7]."'>B08</td>
                            </tr>
                            <tr>
                                <td bgcolor='".$parkingColer[8]."'>B09</td>
                                <td bgcolor='".$parkingColer[9]."'>B10</td>
                                <td bgcolor='".$parkingColer[10]."'>B11</td>
                                <td bgcolor='".$parkingColer[11]."'>B12</td>
                                <td bgcolor='".$parkingColer[12]."'>B13</td>
                                <td bgcolor='".$parkingColer[13]."'>B14</td>
                                <td bgcolor='".$parkingColer[14]."'>B15</td>
                                <td bgcolor='".$parkingColer[15]."'>B16</td>
                            </tr>
                        </table>";
                        ?>
                        <table class="lane">
                            <tr>
                                <td>&lArr; 遵行方向 &lArr;</td>
                            </tr>
                        </table>
                    </td>
                    <td style="width: 60px">&dArr;</td>
                </tr>
            </table>
        </div>
    </div>
</div>
</body>
</html>
