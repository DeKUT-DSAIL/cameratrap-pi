import machine, time, pyb, sensor, image, time
from pyb import RTC

rtc = RTC() # Real Time Clock
# Will set the clock, only need to uncomment and run once to set real time clock
rtc.datetime((2019, 10, 8, 3, 28, 0, 0, 0))

RED_LED_PIN = 1
BLUE_LED_PIN = 3

sensor.reset() # Initialize the camera sensor.
sensor.set_pixformat(sensor.GRAYSCALE) # or sensor.GRAYSCALE
sensor.set_framesize(sensor.VGA) # or sensor.QQVGA (or others)
sensor.skip_frames(time = 2000) # Let new settings take affect.
img = sensor.snapshot() # Take a picture and return the image.

adc = pyb.ADC(pyb.Pin('P6'))
external_led= pyb.Pin("P0", pyb.Pin.OUT_PP)
while (True):
    pyb.delay(1000) 
    button_adc = (((adc.read() * 3.3) + 2047.5) / 4095)
    if button_adc > 3.1:
        print('Motion detected!')
        external_led.high() # or p.value(1) to make the pin high (3.3V)
        dt=rtc.datetime()
        dtfilename = 'snapshot_'
        for item in dt:
            dtfilename = dtfilename+str(item)
        dtfilename = dtfilename+".jpg"
        pyb.LED(RED_LED_PIN).on()
        sensor.snapshot().save(dtfilename) # or "example.bmp" (or others)
        print(dtfilename+" saved to SD card")
        pyb.LED(RED_LED_PIN).off()
    elif button_adc < 3.1:
        print('No Motion!')
        external_led.low()