import serial

ser = serial.Serial("/dev/tty.usbmodem11201", baudrate = 9600, timeout=1)
# temp = ""
iters = 0
vals = []
print("Started Receiving")
while 1:
    arduinoData = ser.readline()
    # temp+=arduinoData
    # print(arduinoData)
    if(arduinoData == b'\xd9\n' or arduinoData ==b'\0xff\n'):
        print("Started")
    elif(arduinoData== b''):
        iters+=1
        print("waiting")
    # elif(arduinoData==b'\r\n'):
    #     print("")
    else:
        iters =0
        c = arduinoData.decode('ascii')
        print(type(c),len(c),c)
        vals.append(int(c))
    # f.writelines(arduinoData)
    if(iters>5):
        break
# print(len(temp))
with open("Serial_out.txt","w") as f:
    f.write(",".join(str(item) for item in vals))
print("Finished Receiving")

    



    