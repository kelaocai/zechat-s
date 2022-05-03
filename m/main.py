import wifimgr
from mqtt import *
from display import oled




wlan = wifimgr.get_connection()
if wlan is None:
    print("Could not initialize the network connection.")
    oled('network error!')

    while True:
        pass  # you shall not pass :D


# Main Code goes here, wlan is a working network.WLAN(STA_IF) instance.

# print("ESP OK")


# while True:
#     if run() == "FAILED":
#         print("FAILED,retry to connect")
#         time.sleep(5)