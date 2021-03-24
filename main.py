from machine import Pin, ADC
from time import sleep

def main():
    led_rgb_1 = Pin(15, Pin.OUT)
    led_rgb_2 = Pin(14, Pin.OUT)
    led_rgb_3 = Pin(13, Pin.OUT)
    
    temp_sensor = ADC(4)
    convert = 3.3 / (65535)
    
    while True:
        curr_voltage = temp_sensor.read_u16() * convert
        temp_c = 27 - ((curr_voltage - 0.706) / 0.001721)
        temp_f = ((temp_c * 9 / 5) + 32)
        print(str(temp_f))
        sleep(1.0)
        
        if temp_f >= 87:
            led_rgb_3.value(1)
            led_rgb_1.value(0)
            led_rgb_2.value(0)
            
        elif temp_f == 80:
            led_rgb_3.value(0)
            led_rgb_1.value(0)
            led_rgb_2.value(1)
            
        elif temp_f < 75:
            led_rgb_3.value(0)
            led_rgb_1.value(1)
            led_rgb_2.value(0)
            
        else:
            led_rgb_3.value(0)
            led_rgb_1.value(0)
            led_rgb_2.value(1)
    
main()

