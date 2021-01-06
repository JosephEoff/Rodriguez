import serial
import time
import io

portname="/dev/ttyUSB0"
portspeed=1000000
serialport=serial.Serial(portname,portspeed) 
time.sleep(2)

with open('IV.csv', 'w') as IVFile:
    #Set the output to zero volts.  Read and discard the first values.
    serialport.write(("0B"+chr(13)).encode())
    valuestring = serialport.readline()
    for counter in range(0 , 1023):
       
        serialport.write((str(counter)+"B"+chr(13)).encode())
        #serialport.write(("M\r\n").encode())
        valuestring = serialport.readline()
        stringvalues = valuestring.split(('\t').encode())
       
        vBias = (float(stringvalues[0])/1023) * 5 / 256
        vBase = (float(stringvalues[1])/1023) * 5 / 256
        vCollector = (float(stringvalues[2])/1023) * 5 / 256
        
        print("Count: " + str(counter) + " VBias= " + str(vBias) + " VBase= " + str(vBase) + " VCollector= " + str(vCollector))
        
        
        V = counter/1023 * 5
        IBase = ((vBias-vBase)/1000) 
        ICollector = (5.0-vCollector)/1000.0
        #Amperes to milliamperes
        IBase = IBase * 1000.0
        ICollector = ICollector * 1000.0
        IVFile.write( str(V) + "\t" + str(vBias) + "\t" + str(vBase) + "\t" + str(IBase) + "\t" + str(ICollector) + "\r\n")
        
