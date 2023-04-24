import serial

ser = serial.Serial("/dev/tty.usbmodem11101", baudrate = 9600, timeout=1)
iters = 0
with open("Serial_out.txt", 'w') as f:
    while 1:
        arduinoData = ser.readline().decode('ascii')
        # print(arduinoData)
        f.writelines(arduinoData)
        iters+=1
        print(iters)
        if(iters>10):
    
    



    