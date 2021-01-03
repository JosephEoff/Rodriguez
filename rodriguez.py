from PyQt5 import QtWidgets
from PyQt5.QtCore import QCoreApplication
from forms.mainWindow import mainWindow
    
if __name__ == "__main__":
    QCoreApplication.setOrganizationName("JRE")
    QCoreApplication.setApplicationName("Rodriguez")
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = mainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
