# DIY Wi-Fi Streaming Air Quality Monitor

Analyze the air quality around you and live-stream the data automatically via Internet of Things (IoT) using Ubidots as a platform.

### Materials
- Raspberry Pi with Wi-Fi and USB to Serial Port
- Dylos DC1100 Air Sensor
- Ubidots account (Free for education purposes : http://things.ubidots.com/)

### Methods
1) Set up your Raspberry Pi (https://www.raspberrypi.org/documentation/setup/)
2) Set up a free Ubidots Education account and install Ubidots for python (See https://raspi-temp-rep.readthedocs.io/en/master/ubidots/#ubidots-python-api-client)
3) In Ubidots, set your device name and create two variables. Take note of your API key found by clicking on your username at the top-right corner and going to API Credentials, as well as the API ID of each of your variables.
3) Place the `main.py` Python script into your Raspberry Pi. Verify that the port is connected to '/dev/ttyUSB0'. Make sure you change the API label and API Variable IDs to the ones you obtained on the Ubidots website or it will not work.
3) Run main.py in the Python 3 Shell within your Raspberry Pi.
4) Play around with Ubidots Dashboard settings and visualize the data however you want. See http://things.ubidots.com/ubi/getchart/page/D2D3POf_hx-xN2s5ljrVWFStD7k for an example output.

### Troubleshooting
**How do I know what port my Raspberry Pi's USB to Serial is connected to?**
- In your Raspberry Pi's terminal, run `dmesg | grep tty` to return the following:
```
[    0.000000] Kernel command line: 8250.nr_uarts=1 bcm2708_fb.fbwidth=640 bcm2708_fb.fbheight=480 bcm2708_fb.fbswap=1 smsc95xx.macaddr=B8:27:EB:0F:BA:25 vc_mem.mem_base=0x1ec00000 vc_mem.mem_size=0x20000000  dwc_otg.lpm_enable=0 console=tty1 root=/dev/mmcblk0p7 rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait
[    0.001308] console [tty1] enabled
[    1.021810] 20201000.serial: ttyAMA0 at MMIO 0x20201000 (irq = 81, base_baud = 0) is a PL011 rev2
[    1.030841] 20215040.serial: ttyS0 at MMIO 0x0 (irq = 160, base_baud = 31250000) is a 16550
[   11.838199] usb 1-1: pl2303 converter now attached to ttyUSB0
```
which means that the USB to Serial converter is attached to ttyUSB0, which is what we label our port in `main.py`.

**I can't find my API ID**

Click your Ubidots username and click API Credentials and your API key should pop out

![API Credentials](https://i.imgur.com/PcgEHHl.png)

![API Key](https://i.imgur.com/O3Vz6z9.png)

**I can't find my API Variable IDs**

Click on a specific variable that you created in your device and it should show up on the left-hand side.

![PPM 2.5 API ID](https://i.imgur.com/C0Tx7i9.png)

![PPM 10 API ID](https://i.imgur.com/ElFT2ko.png)





