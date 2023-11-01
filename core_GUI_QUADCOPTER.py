import serial
from serial.tools import list_ports

def ConnectCOM(self):
    COMPort = self.COMCombo.currentText()
    BaudRate = int(self.BaudCombo.currentText())

    try:
        self.serial_connection = serial.Serial(port=COMPort, baudrate=BaudRate)
        self.COMStatus.setText(f"Connected to {COMPort} at {BaudRate} bps.")
        self.ConnectButton.setEnabled(False)
        self.DisconnectButton.setEnabled(True)
        self.RefreshButton.setEnabled(False)
        self.SendButton.setEnabled(True)
    except serial.SerialException as e:
        self.SerialInTB.setText(f"Failed to connect to {COMPort}: {e}")

def DisconnectCOM(self):
    if self.serial_connection is not None:
        self.serial_connection.close()
        self.COMStatus.setText(f"Disconnected from COM.")
        self.ConnectButton.setEnabled(True)
        self.DisconnectButton.setEnabled(False)
        self.RefreshButton.setEnabled(True)
        self.SendButton.setEnabled(False)

def RefreshCOM(self):
    self.COMCombo.clear()
    available_port = [port.device for port in list_ports.comports()]
    self.COMCombo.addItems(available_port)