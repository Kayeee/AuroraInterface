from celery import Celery
from inverterInterface import Inverter, ConnectionException
from tasks import *

import subprocess

app = Celery('tasks', backend='amqp',
                      broker='amqp://Kevin:ASUi3dea@54.186.216.79/pi_env')

@app.task
def updateAuroraC():
    subprocess.call(["sudo", "rm", "aurora"], cwd="/usr/local/bin")
    subprocess.call(["make", "clean"], cwd="Documents/i3dea/aurora-1.9.0")
    subprocess.call(["git", "pull", "origin", "master"], cwd="Documents/i3dea/aurora-1.9.0") #need ssh key for this
    subprocess.call(["sudo", "make", "install"], cwd="Documents/i3dea/aurora-1.9.0")

def updateTasksAndInterface():
    subprocess.call(["git", "pull", "origin", "master"])
