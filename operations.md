# fucking aws cli commands

## get_media() need to set get-data-endpoint with --endpoint-url
```bash
aws kinesisvideo get-data-endpoint --stream-name MyKinesisVideoStream --api-name GET_MEDIA --endpoint-url https://kinesisvideo.ap-northeast-1.amazonaws.com
aws kinesis-video-media get-media --stream-name MyKinesisVideoStream --start-selector=file:///root/pi_parking_monitor/selector.json file:///root/pi_parking_monitor/output.temp --endpoint-url https://kinesisvideo.ap-northeast-1.amazonaws.com
```
