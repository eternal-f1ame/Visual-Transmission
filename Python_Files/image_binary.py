from PIL import Image
import numpy as np

img = Image.open("./images/bunny.png")
img = img.convert("L").convert("1")
img.save("./images/binary_image.png")
imarr = np.asarray(img,dtype = np.int8)
f = open("imagedata.txt","w")
cur = 0
cnt = 0
for i in range(imarr.shape[0]):
    for j in range(imarr.shape[1]):
        if(imarr[i][j]==1):
            cur+=(1<<cnt)
        cnt+=1
        if(cnt==8):
            print(cur,": ",chr(cur))
            # f.write(str(chr(cur)))
            cnt = 0
            cur = 0
        f.write(str(imarr[i][j]))
f.close()
