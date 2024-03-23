# Smart Doorbell
This project has been done using a Raspberry Pi 5. The smart doorbell functions using 3 buttons: one being for ringing, the other for allowing the person to enter and the last for denying the entry. When the ring button is pressed, the red LED lights up, a buzzer rings and the camera feed pops up showing who rang at the door. If the user presses the 2nd button, the person is allowed entry, a buzzer rings and the last LED lights up, indicating that the entry was permitted. Otherwise, if the user presses the deny button, the first LED powers down and a timeout of 5 seconds is applied to the system, so that the one ringing doesn't keep pressing the button.  
  
# Software used  
-Raspberry Pi OS (This has most dev dependencies already installed) [Link](https://www.raspberrypi.com/software/)  
-Visual Studio Code with the Python dependency installed [Link](https://code.visualstudio.com/docs)  
-Optional: VNC viewer [Link](https://www.realvnc.com/en/connect/download/viewer/)  
  
# Hardware Components used  
1x Raspberry Pi 5 [Link](https://www.raspberrypi.com/products/raspberry-pi-5/)  
1x Raspberry Pi 5 case [Link](https://www.raspberrypi.com/products/raspberry-pi-5-case/)  
1x Raspberry Pi 5 27W power supply [Link](https://www.raspberrypi.com/products/27w-power-supply/)  
1x HDMI to micro HDMI adapter [Link](https://www.emag.ro/adaptor-video-ugreen-20134-micro-hdmi-tata-hdmi-mama-4k-20cm-negru-022530/pd/DD4DRDMBM/)  
1x HDMI cable [Link](https://www.emag.ro/cablu-a-ultra-high-speed-hdmi-2-0-v-18gbps-4k-hdr-3d-2160p-1080p-plug-plug-ethernet-gold-plated-1-5m-cv-uhdmi1-5/pd/DLN2CCBBM/)  
1x micro SD card [Link](https://altex.ro/card-de-memorie-sandisk-ultra-sdxc-128gb-140mb-s-clasa-10-uhs-i/cpd/CRDSDUNB128GN6IN/)  
1x keyboard [Link](https://www.emag.ro/tastatura-mecanica-gaming-ducky-one-2-sf-rgb-switch-cherry-mx-blue-dkon1967st-cuspdazt1/pd/DVVFV2MBM/)  
1x mouse [Link](https://www.pcgarage.ro/mouse-gaming/logitech/g502-hero/)  
1x computer monitor [Link](https://altex.ro/monitor-gaming-curbat-led-va-dell-s2722dgm-27-qhd-165hz-amd-freesync-premium-negru/cpd/MONS2722DGM/)  
1x 830 point breadboard [Link](https://cleste.ro/breadboard-830-puncte-mb-102-mb102.html)  
1x raspberry pi camera [Link](https://cleste.ro/camera-video-raspberry-pi.html)  
1x raspberry pi camera cable standard-mini [Link](https://cleste.ro/cablu-camera-raspberry-pi-15cm.html)  
4x 200 ohm resistors [Link](https://cleste.ro/set-rezistene-100buc-e4-3.html)  
2x piezo buzzers [Link](https://cleste.ro/modul-buzzer-pasiv.html)  
3x 4-pin push buttons [Link](https://cleste.ro/butoane-tactile-6x6x5mm.html)  
1x green LED [Link](https://cleste.ro/led-de-5-mm.html)  
1x red LED [Link](https://cleste.ro/led-de-5-mm.html)  
8x male to female jumper cables [Link](https://cleste.ro/10xfire-dupont-mama-tata-20cm.html)  
7x male to male jumper cables [Link](https://cleste.ro/10-x-fire-dupont-tata-tata-10cm.html)  
  
# The demo video can be seen here: https://www.youtube.com/watch?v=ANOm1IGOZ_o  
# Below is the schema for the project  
![Schema for the project](https://github.com/911-LucianGabriel-Bratu/IoT/blob/main/schema.png?raw=true)  
