from PyQt5.QtCore import *
import serial
import time
import math
from forms.IVTracer_Value import IVTracer_Value
from forms.IVTracer_Signals import IVTracer_Signals
from  forms.deviceTypes import deviceTypes

class IVTracer(QRunnable):
    maximumCount = 1023
    R_base = float(3300.0)
    R_collector = float(1000.0)
    V_ref = float(5.0)
    Oversampling = int(256)
    BaseCurrentSamplingCount = int(256)
    
    def __init__(self, comport,  deviceType, numberOfPlots,  R_base,  R_collector,  V_ref ):
        super(IVTracer, self).__init__()
        self.comport = comport
        self.serialport = None
        self.keepRunning = False
        self.signals = IVTracer_Signals()
        self.deviceType = deviceTypes.Diode
        self.deviceType  = deviceType

        self.numberOfPlots = numberOfPlots
        self.R_base = R_base
        self.R_collector = R_collector
        self.V_ref = V_ref

    @pyqtSlot()
    def run(self):
        try:
            self.openComport()
            self.keepRunning = True
            if self.deviceType == deviceTypes.Diode:
               self.traceDiodeIV() 
            if self.deviceType == deviceTypes.NPN :
                self.traceNPNTransistor()
            if self.deviceType == deviceTypes.PNP:
                self.tracePNPTransistor()
            
        except Exception as ex:
            self.signals.Error.emit("Error while tracing: " + str(ex))
        
        self.signals.Finished.emit()
        
    def openComport(self):
        portspeed=1000000
        self.serialport=serial.Serial(self.comport,portspeed) 
        self.serialport.timeout = 5
        time.sleep(2)
    
    def traceDiodeIV(self):
        #Set the output to zero volts.  Read and discard the first values.
        self.serialport.write(("0B"+chr(13)).encode())
        valuestring = self.readFromSerialPort()
        self.serialport.write(("0C"+chr(13)).encode())
        valuestring = self.readFromSerialPort()
        for counter in range(0 , self.maximumCount):
            if not self.keepRunning:
                break
            value = IVTracer_Value()
            self.serialport.write((str(counter)+"C"+chr(13)).encode())
            valuestring = self.readFromSerialPort()
            stringvalues = valuestring.split(('\t').encode())
            value.V_Intended = counter/self.maximumCount * self.V_ref
            value.NPN_VCollector = (float(stringvalues[2])/self.maximumCount) * self.V_ref / self.Oversampling
            value.NPN_VCollectorBias = (float(stringvalues[3])/self.maximumCount) * self.V_ref / self.Oversampling
            value.NPN_ICollector = ((value.NPN_VCollectorBias-value.NPN_VCollector)/self.R_collector) 

            self.signals.Value.emit(value,  0)

    def traceNPNTransistor(self):
        #Set the output to zero volts.  Read and discard the first values.
        self.serialport.write(("0B"+chr(13)).encode())
        valuestring = self.readFromSerialPort()
        self.serialport.write((str(self.maximumCount) + "C"+chr(13)).encode())
        valuestring = self.readFromSerialPort()
        stepSize = int(self.maximumCount/self.numberOfPlots)
        
        count = 0
        for counter in range(stepSize  ,self.maximumCount,  stepSize):
            if not self.keepRunning:
                break
            value = IVTracer_Value()
            self.serialport.write((str(counter)+"B"+chr(13)).encode())
            valuestring = self.readFromSerialPort()
            IBase_Intended = self.getBaseCurrent(counter)
            
            for collectorCounts in range(0, self.maximumCount):
                if not self.keepRunning:
                    break
                value = IVTracer_Value()
                self.serialport.write((str(collectorCounts)+"C"+chr(13)).encode())
                valuestring = self.readFromSerialPort()
                stringvalues = valuestring.split(('\t').encode())
               
                value.V_Intended = collectorCounts/self.maximumCount * self.V_ref
                value.IBase_Intended  = IBase_Intended 
                value.VBias = (float(stringvalues[0])/self.maximumCount) * self.V_ref / self.Oversampling
                value.VBase = (float(stringvalues[1])/self.maximumCount) * self.V_ref / self.Oversampling
                value.NPN_VCollector = (float(stringvalues[2])/self.maximumCount) * self.V_ref / self.Oversampling
                value.NPN_VCollectorBias = (float(stringvalues[3])/self.maximumCount) * self.V_ref / self.Oversampling
                value.IBase = ((value.VBias-value.VBase)/self.R_base) 
                value.NPN_ICollector = ((value.NPN_VCollectorBias-value.NPN_VCollector)/self.R_collector) 
                self.signals.Value.emit(value,  count)
            count = count +1
    
    def tracePNPTransistor(self):
         #Set the output to full output volts.  Read and discard the first values.
        self.serialport.write((str(self.maximumCount) +"B"+chr(13)).encode())
        valuestring = self.readFromSerialPort()
        self.serialport.write((str(self.maximumCount) +"C"+chr(13)).encode())
        valuestring = self.readFromSerialPort()
              
        stepSize = int(self.maximumCount/(self.numberOfPlots))

        count = 0
        stepSize = -1 * stepSize
        for counter in range( self.maximumCount + stepSize , 0,  stepSize ):
            if not self.keepRunning:
                break
            value = IVTracer_Value()
            self.serialport.write((str(counter)+"B"+chr(13)).encode())
            valuestring = self.readFromSerialPort()
            IBase_Intended = self.getBaseCurrent(counter)
            
            for collectorCounts in range(self.maximumCount,  0, -1):
                if not self.keepRunning:
                    break
                value = IVTracer_Value()
                self.serialport.write((str(collectorCounts)+"C"+chr(13)).encode())
                valuestring = self.readFromSerialPort()
                stringvalues = valuestring.split(('\t').encode())
               
                value.V_Intended = collectorCounts/self.maximumCount * self.V_ref
                value.IBase_Intended  = IBase_Intended 
                value.VBias = (float(stringvalues[0])/self.maximumCount) * self.V_ref / self.Oversampling
                value.VBase = (float(stringvalues[1])/self.maximumCount) * self.V_ref / self.Oversampling
                value.PNP_VCollector = (float(stringvalues[2])/self.maximumCount) * self.V_ref / self.Oversampling
                value.PNP_VCollectorBias =  (float(stringvalues[3])/self.maximumCount) * self.V_ref / self.Oversampling
                value.IBase = ((value.VBase - value.VBias)/self.R_base) 
                value.PNP_ICollector = ((value.PNP_VCollector - value.PNP_VCollectorBias)/self.R_collector) 
                #VCollector means "VCE" - that's the voltage difference between the emitter and the collector
                value.PNP_VCollector = self.V_ref - value.PNP_VCollector
                self.signals.Value.emit(value,  count)
            count = count +1
        
    def getBaseCurrent(self, DACount):
        collectorCounts = int(self.maximumCount/6)
        self.serialport.write((str(collectorCounts)+"C"+chr(13)).encode())
        valuestring = self.readFromSerialPort()
        IBase = 0.0
        for count in range (0, self.BaseCurrentSamplingCount):
            if not self.keepRunning:
                break
            self.serialport.write((str(DACount)+"B"+chr(13)).encode())
            valuestring = self.readFromSerialPort()
            stringvalues = valuestring.split(('\t').encode())    
            VBias = (float(stringvalues[0])/self.maximumCount) * self.V_ref / self.Oversampling
            VBase = (float(stringvalues[1])/self.maximumCount) * self.V_ref / self.Oversampling
            IBase = IBase + math.fabs((VBias-VBase)/self.R_base) 
        return IBase/self.BaseCurrentSamplingCount


    def readFromSerialPort(self):
        valuestring = self.serialport.readline()
        if not valuestring:
            raise Exception("Empty response from serial port.","Is the Arduino connected?")
        
        return valuestring
        
    @pyqtSlot()
    def stop(self):
        self.keepRunning = False
