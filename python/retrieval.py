import numpy as np
import matplotlib.pyplot as plt
import json
import serial

with open('char_map.json', 'r') as f:
    char_map = json.load(f)

char_map = {int(k): v for k, v in char_map.items()}
reverse_char_map = {v: k for k, v in char_map.items()}

huffman_codes = json.load(open('huffman_codes.json', 'r'))

class RecievedData():
    def __init__(self,string, huffman_codes):

        self.string = string
        self.huffman_codes = huffman_codes
        self.decoded_string = self.huffman_decode()
        start = self.decoded_string.find('<s>')+3
        end = start + self.decoded_string[start:].find('<e>')
        start_d = self.decoded_string.find('<l>')+3
        end_d = self.decoded_string.find('<h>')
        legth = int(self.decoded_string[start_d:end_d])
        height = int(self.decoded_string[end_d+3:end_d+5])
        self.dimension = (legth, height)
        self.decoded_string = self.decoded_string[start:end]
        self.img = self.make_image_from_string()



    def huffman_decode(self):
        reverse_huffman_codes = {code: char for char, code in self.huffman_codes.items()}
        decoded_text = ''
        current_code = ''

        for bit in self.string:
            current_code += bit
            if current_code in reverse_huffman_codes:
                char = reverse_huffman_codes[current_code]
                decoded_text += char
                current_code = ''
        return decoded_text

    def make_image_from_string(self):
        string = self.decoded_string
        image = np.zeros(self.dimension, dtype=np.uint8)
        for i in range(self.dimension[0]):
            for j in range(self.dimension[1]):
                image[i][j] = reverse_char_map[string[i*self.dimension[1]+j]]
        return image

    def show_image(self):
        plt.imshow(self.img, cmap='gray')
        plt.title("Received Image")
        plt.show()

    def recieve(self):
        switch = False
        ser = serial.Serial("/dev/tty.usbmodem11101", baudrate = 9600, timeout=3)
        data = []
        iters = 0
        while True:
            arduinoData = ser.readline()
            print(arduinoData)
            if(arduinoData == b'\xd9\n' or arduinoData ==b'\0xff\n'):
                print("Started")
            elif(arduinoData== b'' or arduinoData == b'\n'):
                iters+=1
                print("waiting")
            else:
                iters = 0
                c = arduinoData.decode('ascii')
                data.append(int(c))
            if(iters>5):
                break
        binary_data = ""
        for i in data:
            for j in range(7):
                if(i&(1<<j)):
                    binary_data+='1'
                else:
                    binary_data+='0'
        print(len(binary_data))
        return binary_data

# recieved_data = RecievedData(huffman_codes)
# recieved_data.show_image()
if __name__ == '__main__':
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
    binary_data = ""
    for i in vals:
        for j in range(7):
            if(i&(1<<j)):
                binary_data+='1'
            else:
                binary_data+='0'
    print(len(binary_data))
    recieved_data = RecievedData(binary_data,huffman_codes)
    recieved_data.show_image()


    
