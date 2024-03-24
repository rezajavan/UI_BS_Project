import numpy as np
from matplotlib import pyplot as plt
import struct
from scipy import signal
from tkinter import messagebox

def Time_view(fs):
    try:
        file = open('float_d.bin','rb')
        buffer = file.read()
        len_file = int(len(buffer)/4)
        data = struct.unpack('f' * len_file, buffer)
        file.close()
        data_time = []
        x_t = []
        Ts = (1/fs)*(10**-6)
        for index in range(0,len(data),2):
            data_W = (data[index]**2) + (data[index+1]**2)
            data_W = data_W**(1/2)
            data_time.append(data_W)
        for index in range(0, int(len(data)/2)):
            x_t.append(index*Ts)



        plt.figure()
        plt.title('Time')
        plt.xlabel('second')
        plt.ylabel('abs')
        plt.plot(x_t,data_time)

        plt.show()
    except:
        messagebox.showerror('Time view', 'Please restart program.')

def PSD_view(fs):
    try:
        fs = fs*(10**6)
        file = open('float_d.bin','rb')
        buffer = file.read()
        len_file = int(len(buffer)/4)
        data = struct.unpack('f' * len_file, buffer)
        data_Fr = []
        for index in range(0, len(data), 2):
            data_Fr.append(np.complex(data[index],data[index+1]))

        f, PSD = signal.welch(data_Fr,fs=fs,window='flattop',nperseg=1024,scaling='spectrum',return_onesided=False)
        plt.figure()
        f = f / (10 ** 6)
        plt.semilogy(f,np.sqrt(PSD))

        plt.xlabel('frequency[MHz]')
        plt.ylabel('liniear specrtum [RMS]')
        plt.title('PSD')
        plt.show()
    except:
        messagebox.showerror('PSD view', 'Please restart program.')

