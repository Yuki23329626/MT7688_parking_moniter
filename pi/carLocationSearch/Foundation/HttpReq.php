<?php

class HttpReq {


    //用curl傳post or get並取回傳值
    //一定要傳絕對路徑
    public static function httpPost($url,$post)
    {
        //新增header
        $header = array();
        $header[] = 'Content-Type:application/json;charset=UTF-8';
        //設定
        $curl = curl_init();
        curl_setopt($curl, CURLOPT_URL, $url);
        curl_setopt($curl, CURLOPT_POST,true);
        curl_setopt($curl, CURLOPT_CUSTOMREQUEST,'POST');
        curl_setopt($curl, CURLOPT_HTTPHEADER, $header);
        curl_setopt($curl, CURLOPT_POSTFIELDS, $post);
        curl_setopt($curl, CURLOPT_RETURNTRANSFER,true);
        //發送post
        $result = curl_exec($curl);
        //關閉
        curl_close ($curl);
        return $result;
    }

    public static function httpGet($url){
        //新增header
        $header = array();
        $header[] = 'Content-Type:application/json;charset=UTF-8';
        //設定
        $curl = curl_init();
        curl_setopt($curl, CURLOPT_URL, $url);
        curl_setopt($curl, CURLOPT_HTTPHEADER, $header);
        curl_setopt($curl, CURLOPT_RETURNTRANSFER,true);
        //發送get
        $result = curl_exec($curl);
        //關閉
        curl_close ($curl);
        return $result;
    }
}
