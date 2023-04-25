import heapq
import collections
import matplotlib.pyplot as plt
import json
import numpy as np
import PIL
import serial

with open('char_map.json', 'r') as f:
    char_map = json.load(f)

char_map = {int(k): v for k, v in char_map.items()}
reverse_char_map = {v: k for k, v in char_map.items()}

huffman_codes = json.load(open('huffman_codes.json', 'r'))

class TransmissionData():
    def __init__(self, img, huffman_codes):
        self.img = img
        self.information = self.make_string_from_image()
        self.string = '<l>'+str(img.shape[0])+'<h>'+str(img.shape[1])+'<s>'+self.make_string_from_image()+'<e>'
        self.huffman_codes = huffman_codes
        self.encoded_binary = self.huffman_encode()
        self.encoded_string = self.make_string()
        self.encoded_string_length = len(self.encoded_string)


        self.send()

    def make_string_from_image(self):
        image = self.img
        string = []
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                string.append(char_map[image[i][j]])
        return ''.join(string)
    
    def huffman_encode(self):
        text = self.string
        freq = collections.Counter(text)
        heap = [[weight, [char, '']] for char, weight in freq.items()]
        heapq.heapify(heap)
        while len(heap) > 1:
            lo = heapq.heappop(heap)
            hi = heapq.heappop(heap)
            for pair in lo[1:]:
                pair[1] = '0' + pair[1]
            for pair in hi[1:]:
                pair[1] = '1' + pair[1]
            heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
        
        return ''.join(self.huffman_codes[char] for char in text)

    def make_string(self):
        data = ""
        binary_string = self.encoded_binary
        while(len(binary_string)%7==0):
            binary_string+="0"
        cur = 0
        cnt = 0
        for i in range(len(binary_string)):
            if(binary_string[i]=='1'):
                cur+=(1<<cnt)
            cnt+=1
            if(cnt==7):
                data+=(chr(cur))
                cur = 0
                cnt = 0

        return data
        
    def show_image(self):
        plt.imshow(self.img, cmap='gray')
        plt.show()

    def send(self):
        ser = serial.Serial("/dev/tty.usbmodem11101", baudrate = 9600, timeout=3)
        # print(len(self.string))
        for _ in range(2):
            for i in range(len(self.encoded_string)):
                ser.write(bytearray(self.encoded_string[i],'ascii'))
                print(i,ser.readline().decode('ascii'))

    def gen_huffman_codes(images_dir):
        all_strings = []
        for image in os.listdir(images_dir):
            string = []
            img = PIL.Image.open(os.path.join(images_dir, image)).convert('L')
            img = np.array(img).astype(np.uint8)
            img = img//4
            for i in range(img.shape[0]):
                for j in range(img.shape[1]):
                    string.append(char_map[img[i][j]])
    
            string = '<l>'+str(img.shape[0])+'<h>'+str(img.shape[1])+'<s>'+''.join(string)+'<e>'
            all_strings.append(string)

        text = ''.join(all_strings)
        freq = collections.Counter(text)
        heap = [[weight, [char, '']] for char, weight in freq.items()]
        heapq.heapify(heap)
        while len(heap) > 1:
            lo = heapq.heappop(heap)
            hi = heapq.heappop(heap)
            for pair in lo[1:]:
                pair[1] = '0' + pair[1]
            for pair in hi[1:]:
                pair[1] = '1' + pair[1]
            heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
        huffman_codes = dict(heapq.heappop(heap)[1:])
        with open('huffman_codes.json', 'w') as f:
            json.dump(huffman_codes, f)

img = np.array(PIL.Image.open('images/amongus.png').convert('L'))
img = img//4
transmission_data = TransmissionData(img, huffman_codes)
transmission_data.show_image()
