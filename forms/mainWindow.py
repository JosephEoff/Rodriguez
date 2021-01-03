from  forms.Ui_main import Ui_MainWindow 
from  forms.deviceTypes import deviceTypes
from forms.IVTracer import IVTracer
from forms.IVTracer_Collector import IVTracer_Collector
import serial
import serial.tools.list_ports
from PyQt5.QtWidgets import  QMessageBox
from PyQt5.QtCore import QThreadPool,  QSettings
from pyqtgraph import intColor,  mkPen

class mainWindow(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.settings = QSettings()
        self.fillComboBoxes()
        self.connectButtonEvents()
        self.connectLineEditEvents()
        self.tracer = None
        self.threadpool = QThreadPool()
        self.show_Stopped()
        self.collector = IVTracer_Collector(deviceTypes.Diode, "")
        self.currentPlotNumber = -1
        self.plotterView.setBackground('w')
        self.plotterView.addLegend(offset = (-1, 1))
        self.plotterView.getPlotItem().setLabel('left',"ICollector",  units = "A")
        self.plotterView.getPlotItem().setLabel('bottom' ,  "VCollector",  units = "V")   
        self.plotterView.showGrid(x=True, y=True, alpha=1.0)
        self.plotterView.setMouseTracking(True)
        self.plotterView.scene().sigMouseMoved.connect(self.mouseMoved)
        self.loadSettings()

    def  loadSettings(self):
        comport = self.settings.value('ComPort', type=str)
        itemIndex =  self.comboBox_ComPort.findText(comport)
        if itemIndex>=0:
            self.comboBox_ComPort.setCurrentIndex(itemIndex)
    
    def saveSettings(self):
        self.settings.setValue('ComPort', self.comboBox_ComPort.currentText())
    
    def mouseMoved(self,evt):
        pos = evt
        if self.plotterView.sceneBoundingRect().contains(pos):
            mousePoint = self.plotterView.plotItem.vb.mapSceneToView(pos)
            self.label_Voltage.setText ("{:10.3f}".format(mousePoint.x()))
            self.label_Current.setText ("{:10.3f}".format(mousePoint.y()*1000 ))
        
    def fillComboBoxes(self):
        i=0
        for deviceType in deviceTypes:
            self.comboBox_DeviceType.insertItem(i, deviceType.name,  deviceType)
            i = i + 1
        
        self.fillComboBox_ComPort()
        
    def fillComboBox_ComPort(self):
        self.comboBox_ComPort.clear()
        self.comboBox_ComPort.addItems(self.getComportList())
        
    def getComportList(self):
        available_ports = serial.tools.list_ports.comports()
        portnames = []
        for port in available_ports:
                portnames.append(port[0])
                
        return portnames
            
    def connectLineEditEvents(self):
        self.lineEditDeviceName.textChanged.connect(self.updatePlotTitle)
    
    def updatePlotTitle(self,  text):
        self.plotterView.getPlotItem().setTitle(text)
    
    def connectButtonEvents(self):
        self.pushButtonRun.clicked.connect(self.on_ButtonRunClicked)
        self.pushButtonStop.clicked.connect(self.on_ButtonStopClicked)
        
    def on_ButtonRunClicked(self):
        if not self.tracer is None:
            return
        self.saveSettings()
        self.currentPlotNumber = -1
        self.show_Running()
        self.plotterView.clear()
        self.plotterView.getPlotItem().legend.clear()
        self.collector =  IVTracer_Collector(self.comboBox_DeviceType.currentData(), self.lineEditDeviceName.text() )
        if self.comboBox_DeviceType.currentData() == deviceTypes.Diode:
            self.plotterView.getPlotItem().setLabel('left',"I_forward",  units = "A")
            self.plotterView.getPlotItem().setLabel('bottom' ,  "V_forward",  units = "V")    
        else:
            self.plotterView.getPlotItem().setLabel('left',"ICollector",  units = "A")
            self.plotterView.getPlotItem().setLabel('bottom' ,  "VCollector",  units = "V")    
              
        self.tracer = IVTracer(self.comboBox_ComPort.currentText(),  self.comboBox_DeviceType.currentData(), self.doubleSpinBoxMinimumBaseCurrent.value()/1000,  self.spinBoxTraceCount.value())
        self.tracer.signals.Error.connect(self.on_TracerError)
        self.tracer.signals.Finished.connect(self.on_TracerFinished)
        self.tracer.signals.Value.connect(self.on_TracerValue)
        self.threadpool.start(self.tracer)
        
    def on_ButtonStopClicked(self):
        if not self.tracer is None:
            self.tracer.stop()

    def on_TracerFinished(self):
        self.tracer.signals.Error.disconnect()
        self.tracer.signals.Finished.disconnect()
        self.tracer.signals.Value.disconnect()
        self.tracer = None
        self.show_Stopped()
        
    def show_Running(self):
        self.pushButtonRun.setEnabled(False)
        self.comboBox_DeviceType.setEnabled(False)
        self.pushButtonStop.setEnabled(True)
        
    def show_Stopped(self):
        self.pushButtonRun.setEnabled(True)
        self.comboBox_DeviceType.setEnabled(True)
        self.pushButtonStop.setEnabled(False)
    
    def on_TracerError(self, errorMessage):
        QMessageBox.critical(self.centralWidget, 'IVTracer Error', errorMessage, QMessageBox.Ok, QMessageBox.Ok)
    
    def on_TracerValue(self, value,  plotNumber):
        self.collector.updateTrace(value,  plotNumber)
        self.updatePlot(plotNumber)
        
    def updatePlot(self,  plotNumber):
        if not plotNumber == self.currentPlotNumber:
            color = intColor(plotNumber, hues=self.tracer.numberOfPlots +1, values=1, maxValue=255, minValue=150, maxHue=360, minHue=0, sat=255, alpha=255)
            if self.collector.deviceType == deviceTypes.Diode:
                self.traceplot = self.plotterView.plot([0], [0],  pen=mkPen(color, width = 1))    
            else:
                self.traceplot = self.plotterView.plot([0], [0] , pen=mkPen(color, width = 1) ,  name = self.collector.getBaseCurrentForTrace(plotNumber))
            self.currentPlotNumber = plotNumber

        self.traceplot.setData(self.collector.getPlotData(plotNumber))

