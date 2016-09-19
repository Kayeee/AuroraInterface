import subprocess
import sys
file = None

def setup_file():
   global file 
   subprocess.call(["touch", "output.log"], cwd="/home/pi/ASUi3dea")
   try:
      if file is None:
         print "file is None"
         file = open('output.log','w')
         return file
      else:
         return file
   except OSError:
      return None


def updateTasksAndInterface():
   subprocess.call(["rm", "-rf", "output.log"], cwd="/home/pi/ASUi3dea")
   subprocess.call(["touch", "output.log"], cwd="/home/pi/ASUi3dea")
   file = setup_file()
   if file is None:
      return
   file.write(sys._getframe().f_code.co_name)
   result = subprocess.check_output(["celery", "multi", "stop", "interface_worker"], cwd="/home/pi/ASUi3dea")
   print result
   result += subprocess.check_output(["celery", "multi", "stop", "updater_worker" ], cwd="/home/pi/ASUi3dea")
   print result
   file.write(result)
   start_interface()
   start_updater()
   file.close()
      
   
def start_interface():
    file = setup_file()
    file.write(sys._getframe().f_code.co_name)
    result = subprocess.check_output(["rm", "-rf", "interface_worker.pid"], cwd="/home/pi/ASUi3dea") 
    result = subprocess.check_output(["rm", "-rf", "interface_worker.log"], cwd="/home/pi/ASUi3dea") 
    print result
    result += subprocess.check_output(["celery", "multi", "start", "interface_worker", "-A", "tasks", "-l", "debug", "-Q", "interface"], cwd="/home/pi/ASUi3dea")
    print result
    file.write(result)

def start_updater():
    file = setup_file()
    file.write(sys._getframe().f_code.co_name)
    result = subprocess.check_output(["rm", "-rf", "updater_worker.pid"], cwd="/home/pi/ASUi3dea") 
    print result
    result = subprocess.check_output(["rm", "-rf", "updater_worker.log"], cwd="/home/pi/ASUi3dea") 
    print result
    result += subprocess.check_output(["celery", "multi", "start", "updater_worker", "-A", "updater", "-l", "debug", "-Q", "updater"], cwd="/home/pi/ASUi3dea")
    print result
    file.write(result)

updateTasksAndInterface()
