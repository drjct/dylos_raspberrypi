import serial
from ubidots import ApiClient

#Dylos Serial Port Setup
#https://www.sylvane.com/media/documents/products/dc1100-com-port-option.pdf
ser = serial.Serial(
        port='/dev/ttyUSB0',
        baudrate = 9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=60)

ser.flushInput() #buffer input to make sure everything is cleared before uploading

print(ser) #diagnostic, make sure everything works


#The serial output format is small counts, comma, large counts, carriage return, line feed:
#Example:
#675,19<CR><LF>
#Units are particles/.01 cubic foot
#A reading of 2 means 200 particles per cubic foot


while True:
    data = ser.readline().decode('utf-8')
    small, large = data.split(',') #place the outputs into separate variables
    small = float(small)
    large = float(large)

    #https://raspi-temp-rep.readthedocs.io/en/master/ubidots/#ubidots-python-api-client
    ######Create an "API" object
    api = ApiClient("A1E-3f71cbb44ff5809eca0c202dbac40221cf44") #API Key goes here
    ######Create a "Variable" object
    small_var = api.get_variable("5b80d8b5c03f9755676f791b")
    large_var = api.get_variable("5b7e25f5c03f973ef812404f") #Variable API ID goes here
    ######Here is where you usually put the code to capture the data, either through your GPIO pins or as a calculation. We'll simply put a random value here:
    #PPM 2.5 = (small - large)/100 micrograms per cubic meters
    #PPM 10 = (large/3) + PM2.5 (micrograms per cubic meters)
    small_calc = (small - large)/100
    large_calc = (large/3) + small_calc

    ######Write the value to your variable in Ubidots
    small_var.save_value({'value':small_calc})
    large_var.save_value({'value':large_calc})

#https://app.ubidots.com/ubi/getchart/page/D2D3POf_hx-xN2s5ljrVWFStD7k