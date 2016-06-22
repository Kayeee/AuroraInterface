from inverterInterface import Inverter, ConnectionException
from celery import Celery

app = Celery('tasks', backend='amqp',
                      broker='amqp://Kevin:ASUi3dea@54.186.216.79/pi_env')
inverter = Inverter()
inverters = {inverter}

@app.task
def add(x, y):
    return x+y

@app.task
def initInverter(address, port):
    #for tests, address = "2" and port = "/dev/ttyUSB0"
    if address not in inverters:
        inverter = Inverter(address, port)
        inverters[address] = inverter
        return "Success"
    else:
        return "Error: Inverter is already initialized."

@app.task
def getAll(address, stringNum = "0"):
    inverter = Inverter()
    result = inverter.getAll("0")
    # try:
    #     result = JSONify(inverters[address].getAll(stringNum))
    #     return result
    # except ConnectionException:
    #     return "Error: Cannot connect to inverter."
    # except KeyError:
    #     return "Error: Address not found."

def JSONify(data):
    return "{" + data + "}"
