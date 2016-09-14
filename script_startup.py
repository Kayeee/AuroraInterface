import subprocess

def updateTasksAndInterface():
    subprocess.call(["git", "pull", "origin", "master"], cwd="/home/pi/Desktop/RaspberryPi_ProjectPrototype/bootup/auroraInterface")
    subprocess.call(["celery", "multi", "start", "updater", "-A", "updater", "-l", "debug"], cwd="/home/pi/Desktop/RaspberryPi_ProjectPrototype/bootup/auroraInterface")

updateTasksAndInterface()
