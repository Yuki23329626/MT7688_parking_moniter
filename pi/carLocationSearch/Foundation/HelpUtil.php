<?php
function sendResponse($status, $body = '', $content_type = 'application/json') { //'html/text'
    $status_header = 'HTTP/1.1 ' . $status . ' ' . 'error';
    header($status_header);
    header('Content-type: ' . $content_type);
    $return = array();
    $return['message'] = $body;
    die(json_encode($return));
}
