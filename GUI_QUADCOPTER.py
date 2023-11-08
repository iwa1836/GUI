from PyQt6 import QtCore, QtGui, QtWidgets, QtSerialPort
from PyQt6.QtCore import QThread, pyqtSignal, QObject
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 200, 600))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(192, 192, 192))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(223, 223, 223))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(96, 96, 96))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(128, 128, 128))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(192, 192, 192))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(223, 223, 223))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(192, 192, 192))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(223, 223, 223))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(96, 96, 96))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(128, 128, 128))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(192, 192, 192))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(223, 223, 223))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(96, 96, 96))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(192, 192, 192))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(223, 223, 223))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(96, 96, 96))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(128, 128, 128))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(96, 96, 96))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(96, 96, 96))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(192, 192, 192))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(192, 192, 192))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(192, 192, 192))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(96, 96, 96, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        self.frame.setPalette(palette)
        self.frame.setAutoFillBackground(True)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 201, 391))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.COMLabel = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.COMLabel.sizePolicy().hasHeightForWidth())
        self.COMLabel.setSizePolicy(sizePolicy)
        self.COMLabel.setObjectName("COMLabel")
        self.verticalLayout_3.addWidget(self.COMLabel)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.COMCombo = QtWidgets.QComboBox(parent=self.verticalLayoutWidget)
        self.COMCombo.setObjectName("COMCombo")
        self.horizontalLayout_3.addWidget(self.COMCombo)
        self.RefreshButton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RefreshButton.sizePolicy().hasHeightForWidth())
        self.RefreshButton.setSizePolicy(sizePolicy)
        self.RefreshButton.setObjectName("RefreshButton")
        self.RefreshButton.clicked.connect(self.RefreshCOM)
        self.RefreshButton.setEnabled(True)
        self.horizontalLayout_3.addWidget(self.RefreshButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.BaudLabel = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BaudLabel.sizePolicy().hasHeightForWidth())
        self.BaudLabel.setSizePolicy(sizePolicy)
        self.BaudLabel.setObjectName("BaudLabel")
        self.verticalLayout_3.addWidget(self.BaudLabel)
        self.BaudCombo = QtWidgets.QComboBox(parent=self.verticalLayoutWidget)
        self.BaudCombo.setObjectName("BaudCombo")
        self.BaudCombo.addItem("")
        self.BaudCombo.addItem("")
        self.BaudCombo.addItem("")
        self.BaudCombo.addItem("")
        self.BaudCombo.addItem("")
        self.BaudCombo.addItem("")
        self.BaudCombo.addItem("")
        self.BaudCombo.addItem("")
        self.verticalLayout_3.addWidget(self.BaudCombo)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ConnectButton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.ConnectButton.setObjectName("ConnectButton")
        self.ConnectButton.clicked.connect(self.ConnectCOM)
        self.ConnectButton.setEnabled(True)
        self.horizontalLayout_2.addWidget(self.ConnectButton)
        self.DisconnectButton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.DisconnectButton.setEnabled(True)
        self.DisconnectButton.setObjectName("DisconnectButton")
        self.DisconnectButton.clicked.connect(self.DisconnectCOM)
        self.DisconnectButton.setEnabled(False)
        self.horizontalLayout_2.addWidget(self.DisconnectButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.SerialInLabel = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.SerialInLabel.setObjectName("SerialInLabel")
        self.verticalLayout_3.addWidget(self.SerialInLabel)
        self.SerialInTB = QtWidgets.QTextBrowser(parent=self.verticalLayoutWidget)
        self.SerialInTB.setObjectName("SerialInTB")
        self.verticalLayout_3.addWidget(self.SerialInTB)
        self.SerialOutLabel = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.SerialOutLabel.setObjectName("SerialOutLabel")
        self.verticalLayout_3.addWidget(self.SerialOutLabel)
        self.SerialOutTB = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.SerialOutTB.setObjectName("SerialOutTB")
        self.SerialOutTB.returnPressed.connect(self.SendCOM)
        self.verticalLayout_3.addWidget(self.SerialOutTB)
        self.SendButton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.SendButton.setObjectName("SendButton")
        self.SendButton.clicked.connect(self.SendCOM)
        self.SendButton.setEnabled(False)
        self.verticalLayout_3.addWidget(self.SendButton)
        self.COMStatus = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.COMStatus.setText("")
        self.COMStatus.setObjectName("COMStatus")
        self.verticalLayout_3.addWidget(self.COMStatus)
        self.frame_3 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(200, 0, 600, 600))
        self.frame_3.setAutoFillBackground(True)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_2 = QtWidgets.QFrame(parent=self.frame_3)
        self.frame_2.setGeometry(QtCore.QRect(30, 30, 540, 540))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.PFD_Background = QtWidgets.QLabel(parent=self.frame_2)
        self.PFD_Background.setGeometry(QtCore.QRect(0, -540, 540, 1620))
        self.PFD_Background.setText("")
        self.PFD_Background.setPixmap(QtGui.QPixmap("Images/PFD_Background.png"))
        self.PFD_Background.setScaledContents(True)
        self.PFD_Background.setObjectName("PFD_Background")
        self.frame_4 = QtWidgets.QFrame(parent=self.frame_2)
        self.frame_4.setGeometry(QtCore.QRect(70, 70, 400, 400))
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.PFD_Pitch = QtWidgets.QLabel(parent=self.frame_4)
        self.PFD_Pitch.setGeometry(QtCore.QRect(-70, -610, 540, 1620))
        self.PFD_Pitch.setText("")
        self.PFD_Pitch.setPixmap(QtGui.QPixmap("Images/PFD_Pitch.png"))
        self.PFD_Pitch.setScaledContents(True)
        self.PFD_Pitch.setObjectName("PFD_Pitch")
        self.PFD_Roll = QtWidgets.QLabel(parent=self.frame_2)
        self.PFD_Roll.setGeometry(QtCore.QRect(0, 0, 540, 540))
        self.PFD_Roll.setText("")
        self.PFD_Roll.setPixmap(QtGui.QPixmap("Images/PFD_Roll.png"))
        self.PFD_Roll.setScaledContents(True)
        self.PFD_Roll.setObjectName("PFD_Roll")
        self.PFD_RollDial = QtWidgets.QLabel(parent=self.frame_2)
        self.PFD_RollDial.setGeometry(QtCore.QRect(0, 0, 540, 540))
        self.PFD_RollDial.setText("")
        self.PFD_RollDial.setPixmap(QtGui.QPixmap("Images/PFD_Roll Dial.png"))
        self.PFD_RollDial.setScaledContents(True)
        self.PFD_RollDial.setObjectName("PFD_RollDial")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.serial_connection = QtSerialPort.QSerialPort()
        self.serial_connection.readyRead.connect(self.ReceiveCOM)

        self.RefreshCOM()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GCS Quadcopter"))
        self.COMLabel.setText(_translate("MainWindow", "COM Port:"))
        self.RefreshButton.setText(_translate("MainWindow", "Refresh"))
        self.BaudLabel.setText(_translate("MainWindow", "Baud Rate:"))
        self.BaudCombo.setItemText(0, _translate("MainWindow", "4800"))
        self.BaudCombo.setItemText(1, _translate("MainWindow", "9600"))
        self.BaudCombo.setItemText(2, _translate("MainWindow", "19200"))
        self.BaudCombo.setItemText(3, _translate("MainWindow", "38400"))
        self.BaudCombo.setItemText(4, _translate("MainWindow", "57600"))
        self.BaudCombo.setItemText(5, _translate("MainWindow", "115200"))
        self.BaudCombo.setItemText(6, _translate("MainWindow", "256000"))
        self.BaudCombo.setItemText(7, _translate("MainWindow", "921600"))
        self.ConnectButton.setText(_translate("MainWindow", "Connect"))
        self.DisconnectButton.setText(_translate("MainWindow", "Disconnect"))
        self.SerialInLabel.setText(_translate("MainWindow", "Serial In:"))
        self.SerialOutLabel.setText(_translate("MainWindow", "Serial Out:"))
        self.SendButton.setText(_translate("MainWindow", "Send"))

    def ConnectCOM(self):
        COMPort = self.COMCombo.currentText()
        BaudRate = int(self.BaudCombo.currentText())

        self.serial_connection.setPortName(COMPort)
        self.serial_connection.setBaudRate(BaudRate)
        if self.serial_connection.open(QtSerialPort.QSerialPort.OpenModeFlag.ReadWrite):
            self.COMStatus.setText(f"Connected to {COMPort} at {BaudRate} bps.")
            self.ConnectButton.setEnabled(False)
            self.DisconnectButton.setEnabled(True)
            self.RefreshButton.setEnabled(False)
            self.SendButton.setEnabled(True)
        else:
            self.COMStatus.setText(f"Failed to connect to {COMPort}")
    
    def DisconnectCOM(self):
        if self.serial_connection.isOpen():
            self.serial_connection.close()
            self.COMStatus.setText(f"Disconnected from COM.")
            self.ConnectButton.setEnabled(True)
            self.DisconnectButton.setEnabled(False)
            self.RefreshButton.setEnabled(True)
            self.SendButton.setEnabled(False)

    def RefreshCOM(self):
        self.COMCombo.clear()
        available_port = QtSerialPort.QSerialPortInfo.availablePorts()
        for port in available_port:
            self.COMCombo.addItem(port.portName())

    def ReceiveCOM(self):
        while self.serial_connection.canReadLine():
            received_data = self.serial_connection.readLine().data().decode()
            received_data = received_data.rstrip('\r\n')
            self.SerialInTB.append(received_data)

    def SendCOM(self):
        if self.serial_connection.isOpen():
            send_data = self.SerialOutTB.text().encode()
            self.serial_connection.write(send_data)
            self.SerialOutTB.clear()
            self.COMStatus.setText(f"Data sent: {send_data.decode()}")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
