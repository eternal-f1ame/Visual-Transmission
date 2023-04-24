import serial
from PIL import Image

ser = serial.Serial("/dev/tty.usbmodem11101", baudrate = 9600, timeout=3)
data = [127,126,125,124,123]
with open("imagedata.txt","r") as f:
    lines = f.readlines()
    print(len(lines[0]))
    while(len(lines[0])%7==0):
        lines[0]+="0"
    cur = 0
    cnt = 0
    for i in range(len(lines[0])):
        if(lines[0][i]=='1'):
            cur+=(1<<cnt)
        cnt+=1
        if(cnt==7):
            data.append(cur)
            cur = 0
            cnt = 0
data.extend([125,126,127])
with open("encoded_data.txt","w") as f:
    f.write(",".join(str(item) for item in data))
temp = ""
for i in data:
    temp+=(chr(i))
# for i in range(len(temp)):
#     print(i,temp[i])

print(data)
print(len(data))
arr = "Rev"


for _ in range(2):
    # userinput = input('What data you want to send: ')
    for i in range(len(temp)):
        ser.write(bytearray(temp[i],'ascii'))
        print(i,ser.readline().decode('ascii'))
    