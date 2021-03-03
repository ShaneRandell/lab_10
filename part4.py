import serial
import matplotlib.pyplot as plt
from drawnow import *

Data1 = []
Data2 = []

def PlotSignal():
    plt.ylim(0,1200)
    plt.title('Ploting in Streaming AD0 from Arduino')
    plt.grid(True)
    plt.ylabel('Analog Signal AD0')
    plt.plot(Data1, 'r', label='Digital Signal')
    plt.plot(Data2, 'b', label='Digital Signal')
    plt.legend(loc='upper right')

if __name__ == '__main__':

    ser = serial.Serial('COM3', 9600) # use your own
    plt.ion()
    Dcounter=0
    ser.flush()

    while True:
        while (ser.inWaiting()==0):
            pass # do nothing if no incoming data
        ardData = ser.readline().decode('utf-8')
        InputData = ardData.split(',')
        temp = float(InputData[0])
        P = float(InputData[1])
        Data1.append(temp)
        Data2.append(P)

        drawnow(PlotSignal)
        plt.pause(0.000001)
        Dcounter=Dcounter+1
        if(Dcounter>60):
            Dcounter=0
            Data1.pop(0)

    ser.close()