import heapq
import collections
import matplotlib.pyplot as plt
import json

with open('char_map.json', 'r') as f:
    char_map = json.load(f)

char_map = {int(k): v for k, v in char_map.items()}
reverse_char_map = {v: k for k, v in char_map.items()}

class TransmissionData():
    def __init__(self, img):
        self.img = img
        self.information = self.make_string_from_image()
        self.string = r'<l>'+str(img.shape[0])+r'<h>'+str(img.shape[1])+r'<s>'+self.make_string_from_image()+r'<e>'
        self.encoded_string, self.huffman_codes = self.huffman_encode()
        self.encoded_string_length = len(self.encoded_string)

    def make_string_from_image(self):
        image = self.img
        string = []
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                string.append(char_map[image[i][j]])
        return r''.join(string)
    
    def huffman_encode(self):
        text = self.string
        freq = collections.Counter(text)
        heap = [[weight, [char, r'']] for char, weight in freq.items()]
        heapq.heapify(heap)
        while len(heap) > 1:
            lo = heapq.heappop(heap)
            hi = heapq.heappop(heap)
            for pair in lo[1:]:
                pair[1] = '0' + pair[1]
            for pair in hi[1:]:
                pair[1] = '1' + pair[1]
            heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

        huffman_codes = dict(sorted(heapq.heappop(heap)[1:], key=lambda x: (len(x[-1]), x)))
        return ''.join(huffman_codes[char] for char in text), huffman_codes

    def show_image(self):
        plt.imshow(self.img, cmap='gray')
        plt.show()
