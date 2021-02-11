import numpy as numpy
from collections import OrderedDict
from  forms.deviceTypes import deviceTypes
from forms.IVTrace import IVTrace



class IVTracer_Collector(object):
    traces = OrderedDict()
    deviceType = deviceTypes.Diode
    title = ""
    
    def __init__(self, deviceType,  title):
        self.deviceType = deviceType
        self.title = title
        self.clear()
    
    def clear(self):
        self.traces = OrderedDict()

    def updateTrace(self, IVTracer_value,  traceNumber):
        if not traceNumber in self.traces:
            newtrace = IVTrace(self.deviceType,  IVTracer_value.IBase_Intended )
            self.traces[traceNumber] = newtrace
        self.traces[traceNumber].update(IVTracer_value)
        
    def getPlotData(self,  traceNumber):
        if traceNumber in self.traces:
            return self.traces[traceNumber].getPlotData()
        
        return numpy.zeros(shape=(1,2))

    def getBaseCurrentForTrace(self,  traceNumber):
        if traceNumber in self.traces:
            baseCurrent = self.traces[traceNumber].baseCurrent
            return "{:10.2f}".format(baseCurrent*1000000 ) + "µA"
