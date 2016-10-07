from celery import Celery
#from inverterInterface import Inverter, ConnectionException
#from tasks import *

import sys
import subprocess

app = Celery('updater_worker', backend='amqp',
                      broker='amqp://Kevin:ASUi3dea@52.87.223.187/pi_env')


@app.task(name="updater.recordlog")
def recordlog(result, filename):
    print filename
    subprocess.check_output(["rm","-rf", filename], cwd="/home/pi/ASUi3dea/logs")
    subprocess.check_output(["touch", filename], cwd="/home/pi/ASUi3dea/logs")
    file = open('/home/pi/ASUi3dea/logs/'+filename,'w')
    file.write(result)
    file.close()

@app.task(name="updater.reboot_pi")
def reboot_pi():
    subprocess.check_output(["sudo","reboot"], cwd="/home/pi/ASUi3dea")

@app.task(name="updater.updateAuroraC")
def updateAuroraC():
    result = subprocess.check_output(["sudo", "rm", "aurora"], cwd="/usr/local/bin")
    result += subprocess.check_output(["make", "clean"], cwd="/home/pi/Documents/i3dea/aurora-1.9.0")
    result += subprocess.check_output(["git", "pull", "origin", "master"], cwd="/home/pi/Documents/i3dea/aurora-1.9.0") #need ssh key for this
    result += subprocess.check_output(["sudo", "make", "install"], cwd="/home/pi/Documents/i3dea/aurora-1.9.0")
    filename = sys._getframe().f_code.co_name + '.log'
    recordlog(result, filename)
    

@app.task(name="updater.updateTasksAndInterface")
def updateTasksAndInterface():
    result = subprocess.check_output(["git", "pull", "origin", "master"], cwd="/home/pi/ASUi3dea")
    result += subprocess.check_output(["celery", "multi", "stop", "interface_worker", "-A", "tasks", "-Q", "interface"], cwd="/home/pi/ASUi3dea")
    result += subprocess.check_output(["celery", "multi", "start", "interface_worker", "-A", "tasks","-l", "info", "-Q", "interface"], cwd="/home/pi/ASUi3dea")
    filename = sys._getframe().f_code.co_name + '.log'
    recordlog(result, filename)
