
from ast import While
from ctypes import sizeof
from email.mime import image
from ppadb.client import Client as AdbClient
client = AdbClient(host="127.0.0.1", port=5037)

# dthoai
adb = client.device("BAG00072893")



adb.push("icon.png", "/document/downloads:icon.png")