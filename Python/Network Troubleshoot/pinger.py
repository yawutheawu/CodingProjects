import json
import platform
import subprocess
from datetime import datetime, timedelta
import wmi

interval = 12

currentMoment = datetime.now()
pastPing = datetime.now() - timedelta(seconds = interval)
stored = r"pingData.json"
failData = r"FailureData.json"
def load(file):
    with open(file, "r") as f:
        return json.load(f)

def save(file, Storage):
    with open(file, "w") as f:
        json.dump(Storage, f)
    return 0
def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """

    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host]

    return subprocess.call(command) == 0

dataDict = load(stored)

while True:
    if pastPing + timedelta(seconds = interval) < currentMoment:
        currentMoment = datetime.now()
        pastPing = datetime.now()
        r = ping('google.com')
        dataDict[str(currentMoment.strftime("%m/%d/%Y %H:%M:%S"))] = r
        save(stored, dataDict)
        if not r:
            win = wmi.WMI()
            failDict = load(failData)
            FailList = []
            for process in win.Win32_Process():
                FailList.append(process.Name)
            failDict[str(currentMoment.strftime("%d/%m/%Y %H:%M:%S"))] = FailList
            save(failData,failDict)
    else:
        currentMoment = datetime.now()
