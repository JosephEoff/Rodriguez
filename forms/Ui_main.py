# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/dev/EricProjects/Qt-IV-Plotter/forms/main.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(563, 574)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/IV.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAnimated(False)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBoxControls = QtWidgets.QGroupBox(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxControls.sizePolicy().hasHeightForWidth())
        self.groupBoxControls.setSizePolicy(sizePolicy)
        self.groupBoxControls.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBoxControls.setTitle("")
        self.groupBoxControls.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.groupBoxControls.setObjectName("groupBoxControls")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBoxControls)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.groupBoxControls)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEditDeviceName = QtWidgets.QLineEdit(self.groupBoxControls)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditDeviceName.sizePolicy().hasHeightForWidth())
        self.lineEditDeviceName.setSizePolicy(sizePolicy)
        self.lineEditDeviceName.setObjectName("lineEditDeviceName")
        self.verticalLayout.addWidget(self.lineEditDeviceName)
        self.label_2 = QtWidgets.QLabel(self.groupBoxControls)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.doubleSpinBoxMinimumBaseCurrent = QtWidgets.QDoubleSpinBox(self.groupBoxControls)
        self.doubleSpinBoxMinimumBaseCurrent.setDecimals(3)
        self.doubleSpinBoxMinimumBaseCurrent.setMinimum(0.001)
        self.doubleSpinBoxMinimumBaseCurrent.setMaximum(1.0)
        self.doubleSpinBoxMinimumBaseCurrent.setSingleStep(0.001)
        self.doubleSpinBoxMinimumBaseCurrent.setProperty("value", 0.001)
        self.doubleSpinBoxMinimumBaseCurrent.setObjectName("doubleSpinBoxMinimumBaseCurrent")
        self.verticalLayout.addWidget(self.doubleSpinBoxMinimumBaseCurrent)
        self.label_3 = QtWidgets.QLabel(self.groupBoxControls)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.spinBoxTraceCount = QtWidgets.QSpinBox(self.groupBoxControls)
        self.spinBoxTraceCount.setMinimum(2)
        self.spinBoxTraceCount.setMaximum(20)
        self.spinBoxTraceCount.setObjectName("spinBoxTraceCount")
        self.verticalLayout.addWidget(self.spinBoxTraceCount)
        self.comboBox_DeviceType = QtWidgets.QComboBox(self.groupBoxControls)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_DeviceType.sizePolicy().hasHeightForWidth())
        self.comboBox_DeviceType.setSizePolicy(sizePolicy)
        self.comboBox_DeviceType.setObjectName("comboBox_DeviceType")
        self.verticalLayout.addWidget(self.comboBox_DeviceType)
        self.pushButtonRun = QtWidgets.QPushButton(self.groupBoxControls)
        self.pushButtonRun.setObjectName("pushButtonRun")
        self.verticalLayout.addWidget(self.pushButtonRun)
        self.pushButtonStop = QtWidgets.QPushButton(self.groupBoxControls)
        self.pushButtonStop.setObjectName("pushButtonStop")
        self.verticalLayout.addWidget(self.pushButtonStop)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label_4 = QtWidgets.QLabel(self.groupBoxControls)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_Current = QtWidgets.QLabel(self.groupBoxControls)
        self.label_Current.setObjectName("label_Current")
        self.verticalLayout.addWidget(self.label_Current)
        self.label_5 = QtWidgets.QLabel(self.groupBoxControls)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_Voltage = QtWidgets.QLabel(self.groupBoxControls)
        self.label_Voltage.setObjectName("label_Voltage")
        self.verticalLayout.addWidget(self.label_Voltage)
        self.comboBox_ComPort = QtWidgets.QComboBox(self.groupBoxControls)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_ComPort.sizePolicy().hasHeightForWidth())
        self.comboBox_ComPort.setSizePolicy(sizePolicy)
        self.comboBox_ComPort.setObjectName("comboBox_ComPort")
        self.verticalLayout.addWidget(self.comboBox_ComPort)
        self.horizontalLayout.addWidget(self.groupBoxControls)
        self.plotterView = PlotWidget(self.centralWidget)
        self.plotterView.setObjectName("plotterView")
        self.horizontalLayout.addWidget(self.plotterView)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Rodriquez"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p>Device name:</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Minimum base current (mA)"))
        self.label_3.setText(_translate("MainWindow", "Number of traces:"))
        self.pushButtonRun.setText(_translate("MainWindow", "Run"))
        self.pushButtonStop.setText(_translate("MainWindow", "Stop"))
        self.label_4.setText(_translate("MainWindow", "Current (mA):"))
        self.label_Current.setText(_translate("MainWindow", "0"))
        self.label_5.setText(_translate("MainWindow", "Voltage (V):"))
        self.label_Voltage.setText(_translate("MainWindow", "0"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
