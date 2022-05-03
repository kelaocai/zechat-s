import machine
from ssd1306 import SSD1306_I2C
i2c = machine.SoftI2C(sda=machine.Pin(4), scl=machine.Pin(5))
screen=SSD1306_I2C(128, 64, i2c)

def oled(txt):

    screen.fill(0)
    screen.text(txt,0,0)
    screen.show()
     
