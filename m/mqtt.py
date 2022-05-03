# -*-coding:utf-8-*-
from umqtt.simple import MQTTClient
from machine import Pin
import network
import time
import machine
import dht
from machine import Timer
import json


# ---以下的参数值都需要根据自己的环境修改-----------------------------------------------
led = Pin(2, Pin.OUT)  # ESP32的引脚2接了LED灯，可根据自己的ESP32板子的LED引脚来设置

SSID = "doudou"  # 填写自己的WIFI名称
PASSWORD = "88395050"  # 填写自己的WIFI密码

SERVER = "iot-06z00b6asx24jbl.mqtt.iothub.aliyuncs.com"  # mqttHostUrl
CLIENT_ID = "h28gD4YFQGW.esp32_001|securemode=2,signmethod=hmacsha256,timestamp=1650161622651|"  # clientId
username = "esp32_001&h28gD4YFQGW"  # username
password = "c3b5c167ae8c578f461822a9630786f5a682d5d388de7cfad4cdb79333aac0ef"  # 密码
publish_TOPIC = "/h28gD4YFQGW/esp32_001/user/update"
subscribe_TOPIC = "/h28gD4YFQGW/esp32_001/user/get"
# ---以上的参数值都需要根据自己的环境修改-----------------------------------------------

client = None
mydht = None
wlan = None


def ConnectWifi(ssid, passwd):
    global wlan
    wlan = network.WLAN(network.STA_IF)  # create a wlan object
    wlan.active(True)  # Activate the network interface
    wlan.disconnect()  # Disconnect the last connected WiFi
    wlan.connect(ssid, passwd)  # connect wifi
    while wlan.ifconfig()[0] == "0.0.0.0":
        time.sleep(1)
    print(wlan.ifconfig())


def sub_cb(topic, msg):
    global led
    print((topic, msg))
    # msg = str(msg)
    print(type(msg))
    print(msg)
    msg = json.loads(msg)
    print(msg)
    if msg["lightStatus"] == "ON":
        print("receive ON")
        for i in range(5):
            led.value(0)
            time.sleep_ms(300)
            led.value(1)
            time.sleep_ms(300)
        
        
        print("led ON")
    if msg["lightStatus"] == "OFF":
        print("receive OFF")
        led.value(0)
        print("led OFF")


def heartbeatTimer(mytimer):
    global client
    global led
    led.value(1)
    try:
        mymessage = '{"heartbeat":"esp32_001"}'
        print("============================")
        print(mymessage)
        client.publish(topic=publish_TOPIC, msg=mymessage, retain=False, qos=0)
    except Exception as ex_results2:
        print("exception", ex_results2)
        print("this is error")
        mytimer.deinit()


#     finally:
#         machine.reset()


def run():
    global client
    global led
    global wlan
    print("start to connect mqtt ali")
    try:
        # mydht = dht.DHT11(machine.Pin(4))
        ConnectWifi(SSID, PASSWORD)
        client = MQTTClient(
            CLIENT_ID, SERVER, 0, username, password, 60
        )  # create a mqtt client
        print("client:%s" % str(client))
        led.value(1)
        client.set_callback(sub_cb)  # set callback
        client.connect()  # connect mqtt
        client.subscribe(subscribe_TOPIC)  # client subscribes to a topic
        mytimer = Timer(0)
        mytimer.init(mode=Timer.PERIODIC, period=50000, callback=heartbeatTimer)
        while True:
            client.wait_msg()  # wait message

    except Exception as ex_results:
        print("exception1", ex_results)
    finally:
        if client is not None:
            led.value(0)
            client.disconnect()
        wlan.disconnect()
        wlan.active(False)
        return "FAILED"
