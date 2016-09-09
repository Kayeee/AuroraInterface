import subprocess

def updateTasksAndInterface():
    subprocess.call(["git", "pull", "origin", "master"], cwd="/home/pi/ASUi3dea")
    subprocess.call(["celery", "multi", "start", "updater", "-A", "updater"], cwd="/home/pi/ASUi3dea")

updateTasksAndInterface()
