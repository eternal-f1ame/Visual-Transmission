values = []
with open('Serial_out.txt',"r") as f:
    lines = f.readlines()
    values = [int(item) for item in lines[0].split(',')]
code = [127,126,125,124,123]
def search_subarray(arr, subarr):
    for i in range(len(arr) - len(subarr) + 1):
        if arr[i:i+len(subarr)] == subarr:
            return i
    return -1

id = search_subarray(values,code)
print(values[id+5])
with open("decoded_data.txt","w") as f:
    for i in range(id+5,len(values)-2):
        for j in range(7):
            if(values[i]&(1<<j)):
                f.write(str(1))
            else:
                f.write(str(0))
