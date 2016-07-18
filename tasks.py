from inverterInterface import Inverter, ConnectionException
from celery import Celery

import subprocess

app = Celery('tasks', backend='amqp', broker='amqp://Kevin:ASUi3dea@54.224.107.102/pi_env')

Inverter

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
    return result
    # try:
    #     result = JSONify(inverters[address].getAll(stringNum))
    #     return result
    # except ConnectionException:
    #     return "Error: Cannot connect to inverter."
    # except KeyError:
    #     return "Error: Address not found."

@app.task
def updateAuroraC():
    subprocess.call(["sudo", "rm", "aurora"], cwd="/usr/local/bin")
    subprocess.call(["make", "clean"], cwd="Documents/i3dea/aurora-1.9.0")
    subprocess.call(["git", "pull", "origin", "master"], cwd="Documents/i3dea/aurora-1.9.0") #need ssh key for this
    subprocess.call(["sudo", "make", "install"], cwd="Documents/i3dea/aurora-1.9.0")

@app.task
def updateTasksAndInterface():
    subprocess.call(["git", "pull", "origin", "master"])

def JSONify(data):
    return "{" + data + "}"
