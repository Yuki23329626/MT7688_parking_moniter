# pi parking monitor
停車場車輛監控應用  

## Requirements
1. opencv  
pip install opencv-python 可能會遇到問題  
解決方法是直接去官網下載 source code 依照步驟進行編譯  
[opencv編譯方式](https://docs.opencv.org/4.5.0/db/df5/tutorial_linux_gcc_cmake.html)  
cmake 那邊可能有點難以理解  
總之就是在根目錄建一個資料夾 "build"，進入 "build" 資料夾後，執行  
```bash
cmake ../../opencv-master
make
```

2. python version  
python 版本使用 3 的最新版應該就好了  

3. aws cli  
記得設定 aws 相關的 configuration，同時 IAM 上的 user 要設定權限 "administratorAccess" 等等  
aws educate 可能沒辦法完成一些需要權限的操作  

### 抓取即時影像片段 & 進行文字偵測
目前只有抓單一 chunk 的實作，之後要考慮如何組合成影片後上傳到 s3  
每秒最多 5 個 chunk 的樣子  
如果以兩分鐘上傳一次的話，大概是收集 600 chunks 集合成影片  
也許可以寫第二支程式負責上傳的部分，也許要考慮刪除的部分，s3 免費的容量上限好像是 5G  
#### [update 2020/12/19 13:03]  
改成使用 HLS 的方式讀取 stream，應該可以用 opencv 的方式讀取 frame 來存成影片
#### [update 2020/12/19 15:44]  
突然發現一件事，也許可以不用 s3，因為 opencv 可以直接從 HLS 中擷取 frame  
直接用 frame 來做 text detection 就好了  
不行，結果還是只能透過 s3 來做 text detection，因為 function 中必須要有 s3 object  
而且文字辨識的部分只能辨識單一的相片而已  
#### [update 2020/12/19 17:08]  
目前的做法是每秒擷取一張照片上傳到 s3  
然後一樣每秒使用 rekognition api 做文字偵測  
可以正常的取得 response  
#### [update 2020/12/19 18:18]  
我發現 rekognition 的收費貴得誇張，1000 張就要 1.3 美元了  
改成 100 秒呼叫一次好了  

下面兩個程式可以考慮背景執行  
```bash
python stream_to_s3.py
python text_detect.py
```

### 在 pi 上進行影像串流到 kinesis video stream  
```bash
gst-launch-1.0 v4l2src device=/dev/video0 ! videoconvert ! video/x-raw,format=I420,width=640,height=480 ! omxh264enc control-rate=2 target-bitrate=512000 periodicity-idr=45 inline-header=FALSE ! h264parse ! video/x-h264,stream-format=avc,alignment=au,profile=baseline ! kvssink stream-name="MyKinesisVideoStream" access-key="AKIAYUIP3VGJ6HR5HSK4" secret-key="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" aws-region="ap-northeast-1"
```

## 筆記
1. rekognition  
要使用 api call 的方式使用，依照 api call 來計費  
基本上目前考慮的作法是存在 s3 上，用 rekognition 的 api 來抓影片上的車牌資料  
可以先把影片上傳到 s3 上使用 api 試試看結果怎麼樣  
記得好像會回傳物件的字串、在畫面上的位置、範圍、時間等等，可以做為車牌辨識的資料  
關於 response 回來的 json 格式可以參考  
[PYTHON-BOTO3官方文件](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.detect_text)  
2. s3  
就是一個儲存空間  
5G 是免費的，嘛可以先不考慮容量上限，大不了再開就是了  
要考慮上限的話可能要另外寫一支程式來刪除容量  
3. RDS  
mysql 的資料庫  
也有免費額度，選這個只是因為我比較熟悉 mysql  
4. kinesisvideo  
大坑，api 跟相關文件寫得有夠稀爛  
使用 get_media() 要先設甚麼 get_data_endpoint 但是文件沒告訴你要怎麼用  
python library 有兩個 class 分別是 kinesisvideo 跟 kinesis-video-media  
結果網路上的做法是要先去 kinesisvideo 去抓 data_endpoint  
再回來 kinesis-video-media 上把拿到的 url 給他的 client 端用  
他X為什麼不要一開始寫在一起就好了  
而且用 aws-cli 也是 kinesisvideo 可以用 kinesis-video-media 不能用  
這他X是在銃三小  
[解決方法](https://stackoverflow.com/questions/49746612/boto3-kinesis-video-stream-error-when-calling-the-getmedia-operation)  
5. 前端  
打算直接開個 EC2 架一個 apache 的網站在上面  
網頁的前端應該會比較好寫，目前打算就直接用傳統的做法  
用 php 連後端抓資料，前端顯示結果  
[有現成的環境可以用](https://github.com/Yuki23329626/apache-docker)  
#### [update 2020/12/19 21:01]  
雖然上面這樣說了，不過 aws 也是有提供集成的版本  
大致做法上就是結合 Elastic Beanstalk, DynamoDB, 還有 SNS  
大概會是比較符合全靠 AWS 的做法，缺點大概是收費會很可寬  
不過目前還沒調查收費的部分  

# 改用 pi 進行實作，以下是舊版本的資訊

## 一、讓 7688 同時開啟 wifi station mode 與 wifi ap mode

1. 將 firmware 刷成 0.93 的版本  
- 0.94 版本可能出現各種未知錯誤
2. 複製 wireless/ralink.sh 取代 /lib/netifd/wireless/ralink.sh  
- 請根據各自需求更改 \<SSID> 跟 \<KEY>  
例如：'uci set wireless.sta.ssid="\<SSID>"'，  
可以更改成 'uci set wireless.sta.ssid="HSNG-A2.4"'  
也就是你想讓你的 7688 連線過去的基地台的 SSID  
另外 wireless.ap.ssid  則是你想讓你的 7688 作為 AP 時想要叫的 SSID  
其他依此類推

```bash
cp wireless/ralink.sh /lib/netifd/wireless/
chmod +x /lib/netifd/wireless/ralink.sh
uci set wireless.sta.ssid="HSNG-A2.4"
uci set wireless.sta.key="hsng@root"
uci set wireless.ap.ssid="nxshen_7688"
uci set wireless.ap.key="123123123"
uci set wireless.sta.encryption="psk"
uci set wireless.sta.disabled="0"
uci commit wireless
wifi
```

## 二、擴充 7688 容量(將系統 Mount 在 SD card 上)

一些好處，例如下載大容量的 library 或套件不會炸裂  

1. 登入 linkit smart 7688  
2. 接下來會對 sd card 進行格式化為 ext4 檔案系統的動作  
記得將 SD card 中重要資料移出

```bash
opkg update
opkg install block-mount kmod-fs-ext4 kmod-usb-storage-extras e2fsprogs fdisk
# /dev/mmcblk0p1 為 7688 上 sd card 裝置的檔案代號  
umount /dev/mmcblk0p1
mkfs.ext4 /dev/mmcblk0p1
# 將 root FS 移至 SD 中
mount /dev/mmcblk0p1 /mnt
tar -C /overlay -cvf - . | tar -C /mnt -xf -
umount /mnt
# 建立 fstab 樣板
block detect > /etc/config/fstab
# 修改 fstab 設定檔
vi /etc/config/fstab
```

3. 修改相關設定並重啟7688

- 輸入【 i 】進入編輯模式
- 修改相關設定
- - 將 mount mmcblk0p1 區域中的 target 修改成【 /overlay 】
- - 將 mount mmcblk0p1 區域中的 enabled 修改成【 1 】
- 按 【 ESC 】再輸入【 :wq! 】存檔離開
- 重新啟動 LinkIt Smart 7688

4. 察看結果

```bash
df -h
```

## 三、個人偏好的套件

```bash
opkg update
opkg install git
opkg install vim
```
