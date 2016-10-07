from inverterInterface import Inverter, ConnectionException
from threading import Thread

import json
import requests

from apscheduler.schedulers.blocking import BlockingScheduler

inverter = Inverter()

def send_data():
    url = "http://52.87.223.187:8000/ASUi3dea/recieve_data/"
    #url = "http://127.0.0.1:8000/ASUi3dea/recieve_data/"
    headers = {}


    # contents = '{"inverter_id": "' + inverter.id + '",' + """
    #
    test = """
    "PartNumber": "-3G79-",
    "SerialNumber": "557651",
    "Firmware": "C.0.2.2",
    "Inverter Version": "PVI-4.2-OUTD",

    "inputvoltage":    230.320648,

    "inputcurrent":     11.876156,

    "inputpower":   3162.865479,

    "gridvoltage":    249.781143,

    "gridcurrent":     12.144599,

    "gridpower":   3014.922119,

    "frequency":     59.986565,

    "conversionefficiency":     95.068008,

    "invertertemperature":     59.829319,

    "cumulatedenergy": {
    "dailyenergy":       16.339,
    "weeklyenergy":       52.413,
    "monthlyenergy":       76.281,
    "yearlyenergy":     6387.256,
    "totalenergy":    18013.019
    }
    """
    # }
    # """

    contents = '{"inverter_id": "' + inverter.id + '", ' + test + '}'

    print contents
    r = requests.post(url, data=contents, headers=headers)

def start():
    scheduler = BlockingScheduler()
    scheduler.add_job(send_data, 'interval', hours=0.01)
    scheduler.start()

if __name__ == "__main__":
    thread = Thread(target = start, args = ())
    thread.start()
    thread.join()
