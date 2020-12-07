# MT7688 Duo parking moniter

## 讓 7688 同時開啟 wifi station mode 與 wifi ap mode

1. 將 firmware 刷成 0.93 的版本  
2. 複製 wireless/ralink.sh 取代 /lib/netifd/wireless/ralink.sh  

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
