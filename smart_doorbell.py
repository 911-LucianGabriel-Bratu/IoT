import time
from picamera2 import Picamera2, Preview
from gpiozero import LED, Button, Buzzer

ring_led = LED(4)
ring_button = Button(17)
ring_buzzer = Buzzer(27)

open_led = LED(24)
open_buzzer = Buzzer(16)
open_button = Button(25)
camera = Picamera2()
camera_config = camera.create_still_configuration(main={"size": (1920, 1080)}, lores={"size": (640, 480)}, display="lores")
camera.configure(camera_config)

decline_button = Button(5)

is_ringing = False

while True:
      if not is_ringing:
          if ring_button.is_pressed:
            ring_led.on()
            ring_buzzer.on()
            is_ringing = True
            camera.start_preview(Preview.QTGL)
            camera.start()
      else:    
            if open_button.is_pressed:
                  ring_led.off()
                  ring_buzzer.off()
                  open_led.on()
                  open_buzzer.on()
                  camera.stop()
                  camera.stop_preview()
                  is_ringing = False
                  time.sleep(5)
                  open_led.off()
                  open_buzzer.off()
            if decline_button.is_pressed:
                  ring_led.off()
                  ring_buzzer.off()
                  camera.stop()
                  camera.stop_preview()
                  is_ringing = False
                  time.sleep(5)
      time.sleep(0.1)