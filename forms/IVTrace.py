import numpy as numpy
from  forms.deviceTypes import deviceTypes

class IVTrace(object):
    values = []
    NPN = []
    PNP = []
    Diode = []
    deviceType = deviceTypes.Diode
    baseCurrent = 0.0

    def __init__(self, deviceType,  baseCurrent):
        self.deviceType = deviceType
        self.clear()
        self.baseCurrent = baseCurrent
    
    def clear(self):
        self.values = []
        self.NPN = []
        self.PNP = []
        self.Diode = []
        
    def update(self, IVTracer_value):
        self.values.append(IVTracer_value)
        self.NPN.append([IVTracer_value.NPN_VCollector, IVTracer_value.NPN_ICollector])
        self.PNP.append([IVTracer_value.PNP_VCollector, IVTracer_value.PNP_ICollector])
        self.Diode.append([IVTracer_value.VBase , IVTracer_value.IBase ])
    
    def getPlotData(self):
        if self.deviceType == deviceTypes.Diode:
            return self._getArrayFromList(self.Diode)
        if self.deviceType == deviceTypes.PNP:
            return self._getArrayFromList(self.PNP)
        if self.deviceType == deviceTypes.NPN:
            return self._getArrayFromList(self.NPN)
        
    def _getArrayFromList(self, dataList):
        data = numpy.array(dataList)
        data = data[data[:,0].argsort()]
        return data
