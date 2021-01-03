from PyQt5.QtCore import *
from forms.IVTracer_Value import IVTracer_Value

class IVTracer_Signals(QObject): 
    Error = pyqtSignal(str)
    Finished = pyqtSignal()
    Value = pyqtSignal(IVTracer_Value,  int)
