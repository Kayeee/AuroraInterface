import subprocess

#subprocess.call(["ls", "-l"])
class ConnectionException(Exception):
    pass

class Inverter:
    address = "0"
    serialPort = "/dev/ttyUSB0"

    def __init__(self, address, serialPort):
        self.address = address
        self.serialPort = serialPort

    def getCumulatedEnergies(self):
        result = subprocess.call(["aurora", "-a", self.address, "-e", "-J", self.serialPort])
        return result

    def getDSP(self, stringNum = "0"):
        result = subprocess.call(["aurora", "-a", self.address, "-d", stringNum, "-J", self.serialPort])
        return result

    def getPartNum(self):
        result = subprocess.call(["aurora", "-a", self.address, "-p", "-J", self.serialPort])
        return result

    def getSerialNum(self):
        result = subprocess.call(["aurora", "-a", self.address, "-n", "-J", self.serialPort])
        return result

    def getFirmWare(self):
        result = subprocess.call(["aurora", "-a", self.address, "-f", "-J", self.serialPort])
        return result

    def getManufacturingDate(self):
        result = subprocess.call(["aurora", "-a", self.address, "-m", "-J", self.serialPort])
        return result

    def getVersion(self):
        result = subprocess.call(["aurora", "-a", self.address, "-v", "-J", self.serialPort])
        return result

    def getAll(self, stringNum = "0"):
        result = subprocess.call(["aurora", "-a", self.address, "-e", "-d", stringNum, "-p", "-n", "-f", "-m", "-v", "-J", self.serialPort])
        return result

    def getData(self, stringNum = "0"):
        result = subprocess.call(["aurora", "-a", self.address, "-e", "-d", stringNum, "-J", self.serialPort])
        return result

    def getInfo(self):
        result = subprocess.call(["aurora", "-a", self.address,  "-p", "-n", "-f", "-m", "-v", "-J", self.serialPort])
        return result

    def checkException(self, result):
        if "ERROR:" in result:
            raise ConnectionException("Error: Cannot connect to inverter.")

    def runErrorCheck(self):
        raise ConnectionException("Error: Testing")
