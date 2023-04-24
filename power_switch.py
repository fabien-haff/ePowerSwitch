from time import sleep
import requests
import sys
from requests.auth import HTTPDigestAuth

auth = HTTPDigestAuth('USER_ID', 'PASSWORD')
#Replace USER_ID and PASSWORD by your credentials

""" CMD codification 
    0_0_0 
    first digit is unused 
    second digit is outlet number starting from 0
    third digit is action, 0 = 0N, 1 = OFF, 2 = Reboot
"""



def control_outlet(outlet_number, action):
    action_num=0
    number = outlet_number -1
    match action:
        case "ON":
            action_num = 0
        case "OFF":
            action_num = 1
        case "RST":
            action_num = 2
        case _:
            exit(555)
    url = f"http://IP_ADDRESS/admin/control.cgi?CMD=0_{number}_{action_num}"
    requests.get(url, auth=auth)

control_outlet(int(sys.argv[1]),sys.argv[2])


