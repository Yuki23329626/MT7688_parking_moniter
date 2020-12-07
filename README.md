# MT7688 Duo parking moniter

## 一、讓 7688 同時開啟 wifi station mode 與 wifi ap mode

1. 將 firmware 刷成 0.93 的版本  
- 0.94 版本可能出現各種未知錯誤
2. 複製 wireless/ralink.sh 取代 /lib/netifd/wireless/ralink.sh  
- 請根據各自需求更改 \<SSID> 跟 \<KEY>  
例如：'uci set wireless.sta.ssid="\<SSID>"'，  
可以更改成 'uci set wireless.sta.ssid="HSNG-A2.4"'  
也就是你想讓你的 7688 連線過去的基地台 SSID  

```bash
cp wireless/ralink.sh /lib/netifd/wireless/
chmod +x /lib/netifd/wireless/ralink.sh
uci set wireless.sta.ssid="<SSID>"
uci set wireless.sta.key="<KEY>"
uci set wireless.ap.ssid="<SSID>"
uci set wireless.ap.key="<KEY>"
uci set wireless.sta.encryption="psk"
uci set wireless.sta.disabled="0"
uci commit wireless
wifi
```

## 二、擴充 7688 容量(將系統 Mount 在 SD card 上)