import numpy as np
from PIL import Image
imarr = np.zeros((16,16),dtype = np.int8)
with open('decoded_data.txt' ,"r") as f:
    lines = f.readlines()
    print(lines[0],len(lines[0]))
    cnt = 0
    for i in lines[0]:
        y = cnt%16
        x = int(cnt/16)
        print(x,y)
        if(i=='1'):
            imarr[x,y] = 1
        else:
            imarr[x,y] = 0
        cnt+=1
        if(cnt==256):
            break
print(imarr)

img = Image.new('1', (16, 16))
pixels  =img.load()
for i in range(16):
    for j in range(16):
        # print(imarr[i,j])
        pixels[i,j] = int(imarr[j,i])

img.save("./images/output.png")