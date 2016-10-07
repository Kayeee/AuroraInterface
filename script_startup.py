import subprocess

def updateTasksAndInterface():
    subprocess.call(["git", "pull", "origin", "master"], cwd="/home/pi/ASUi3dea")
    subprocess.call(["celery", "multi", "start", "updater_worker", "-A", "updater", "-Q", "updater"], cwd="/home/pi/ASUi3dea")
    subprocess.call(["celery", "multi", "start", "interface_worker", "-A", "tasks", "-Q", "interface"], cwd="/home/pi/ASUi3dea")
    subprocess.call(["python", "request_sender.py", "&"], cwd="/home/pi/ASUi3dea")
updateTasksAndInterface()
