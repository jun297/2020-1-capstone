from pynq import Overlay
import pickle, struct, time, math
import numpy as np
import matplotlib.pyplot as plt


convAddress = dict()
convAddress["ifMap"] = 0x100
convAddress["ofMap"] = 0x200
convAddress["_filter"] = 0x280


class CNN:
    def __init__(self):
        self.overlay = None
        self.overlay = Overlay("/home/xilinx/jupyter_notebooks/test/ws_1d/ws_ofmap25_filter25.bit")
        t2 = t1 = time.time()       
        while 1:
            t2 = time.time()
            if t2 - t1 > 20:
                print("Time out(20s).")
                break
            try:
                self.conv_ip = self.overlay.ws_0

                break
            except:
                continue

    def convWrite(self, ifMap, _filter, bias, H, M, C, R, U):
        pass

    def convRead(self, M, E):
        pass

def conv(self, ifMap, _filter, H, R):
    E = int((H - R) / 1) + 1
    self.convWrite(ifMap, _filter, H, R)
    return self.convRead(E)

CNN.conv = conv


# In[5]:


def convWrite(self, ifMap, _filter, H, R):
    self.conv_ip.register_map.H = H
    self.conv_ip.register_map.R = R

    ifMap = np.array(ifMap, dtype=np.float32).flatten()
    self.conv_ip.write(convAddress["ifMap"], struct.pack(f"{ifMap.size}f", *ifMap))

    _filter = np.array(_filter, dtype=np.float32).flatten()
    self.conv_ip.write(convAddress["_filter"], struct.pack(f"{_filter.size}f", *_filter))

def convRead(self, E):
    ofMap = [0 for _ in range(E)]

    for y in range(E):
        readedFloat = self.conv_ip.read(convAddress["ofMap"] + y * 4)
        readedByte = readedFloat.to_bytes(4, byteorder="little")
        ofMap[y] = struct.unpack('f', readedByte)[0]
    return ofMap

CNN.convWrite = convWrite
CNN.convRead = convRead


model = CNN()


t = 0
for i in range(1000):
    ifMap = np.random.rand(49)
    weight = np.random.rand(25)
    tic = time.time()
    C = model.conv(ifMap, weight, len(ifMap), len(weight))
    toc = time.time()
    t += (toc - tic)

print(t/1000)


print(C)

