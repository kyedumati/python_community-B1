# import socket
import os
import subprocess
import json
import sys
import platform

config_file = "devices_config.json"

def check_connectivity(data):
        if len(data)>0:
            for device in data:
                address = device['address']
                param = '-n' if platform.system().lower() == 'windows' else '-c'
                cmd=['ping', param,'1', address]
                res = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                res.wait()
                if res.poll():
                    print("ping to", address, "Failed")
                else:
                    print("ping to", address, "OK")


if __name__ == '__main__':
    # opening file
    data=''
    with open(os.path.join(sys.path[0], config_file), "r") as file:
        # returns JSON object as a dictionary
        data = json.load(file)

    if data!='':
        check_connectivity(data)
