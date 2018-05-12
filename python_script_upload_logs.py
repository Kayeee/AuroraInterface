import subprocess
import datetime
import threading

class File_logs(object):

    def __init__(self, path, filename):
        self.filename = filename
        self.path = path

    def get_path(self):
        return self.path

    def get_name(self):
        return self.filename

    def get_absolute_path(self):
        return self.path + self.filename

files = [
    
    File_logs("/home/pi/ASUi3dea/","interface_worker.log"),
    File_logs("/home/pi/ASUi3dea/","updater_worker.log"),
    File_logs("/var/log/celerydp/","celerydupdater.err"),
    File_logs("/var/log/celerydp/","celerydupdater.log"),
]

def upload_file_logs():
    file_log_scp = open("/home/pi/ASUi3dea/file_log_scp.log", 'w')
    for i in range(0,len(files)):
        now = str(datetime.datetime.today())[:-3].replace('.',"_").replace(':','_').replace(' ',"_")
        file_new = open(files[i].get_absolute_path(),'r')
        file_old = open("/home/pi/ASUi3dea/tmp/tmp_" + files[i].get_name(),'r')
        newfile = files[i].get_name()[:-4] + "_" + now + files[i].get_name()[-4:]
        result =  subprocess.call(["sudo","cp",files[i].get_absolute_path(),newfile], cwd="/home/pi/ASUi3dea")
        result =  subprocess.call(["sudo","cp", "-rf",files[i].get_absolute_path(),"./tmp/tmp_" + files[i].get_name()], cwd="/home/pi/ASUi3dea")
        #if len(file_new.readlines()!=len(file_old.readlines()):
        result =  subprocess.call(["scp", "-i", "Pi.pem", newfile, "ubuntu@ec2-52-87-223-187.compute-1.amazonaws.com:/home/ubuntu/Projects/Verizon/ASUi3dea/logs"], cwd="/home/pi/ASUi3dea")
        if result != 0:
            file_log_scp.write(newfile + " " + now + " " + str(result))
        result =  subprocess.call(["sudo","rm", "-rf",newfile], cwd="/home/pi/ASUi3dea")
    file_log_scp.close()
    threading.Timer(60 * 60, upload_file_logs).start()

upload_file_logs()
