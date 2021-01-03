# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/dev/EricProjects/IV/forms/plotter.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Plotter(object):
    def setupUi(self, Plotter):
        Plotter.setObjectName("Plotter")
        Plotter.resize(258, 191)
        self.plotterView = PlotWidget(Plotter)
        self.plotterView.setGeometry(QtCore.QRect(0, 0, 256, 192))
        self.plotterView.setObjectName("plotterView")

        self.retranslateUi(Plotter)
        QtCore.QMetaObject.connectSlotsByName(Plotter)

    def retranslateUi(self, Plotter):
        _translate = QtCore.QCoreApplication.translate
        Plotter.setWindowTitle(_translate("Plotter", "Form"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Plotter = QtWidgets.QWidget()
    ui = Ui_Plotter()
    ui.setupUi(Plotter)
    Plotter.show()
    sys.exit(app.exec_())
