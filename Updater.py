from inverterInterface import Inverter, ConnectionException
from celery import Celery

import tasks
import subprocess

@app.task
def updateAuroraC():
    subprocess.call(["sudo", "rm", "aurora"], cwd="/usr/local/bin")
    subprocess.call(["make", "clean"], cwd="Documents/i3dea/aurora-1.9.0")
    subprocess.call(["git", "pull", "origin", "master"], cwd="Documents/i3dea/aurora-1.9.0") #need ssh key for this
    subprocess.call(["sudo", "make", "install"], cwd="Documents/i3dea/aurora-1.9.0")

def updateTasksAndInterface():
    subprocess.call(["git", "pull", "origin", "master"])
