"""
*************************
@Purpose :: This module is an API to connect remote Linux host and get the repsonse

@Author         ::

@revision History

@DATE [ DD/MM/YYYY]               @Name                   @Remarks

10-06-2023                       winteck                 Adding New modules for testing product
"""

import re
import sys
from os.path import dirname,abspath
from lib import logger
from lib.connect import exec_cmd


sys.path.append(dirname(dirname(abspath(__file__))))

log = logger.get_logger(__name__)

class Storage:
    """ validation of storage components"""
    def __init__(self):
        pass


    def list_drives(self):
        server_drives=exec_cmd("lsblk")
        out = re.findall(r"(sd[a-z])\s",server_drives)
        return out


    def reset_drive(self):
        dmesg_c = exec_cmd("dmesg -c")
        reset = exec_cmd(r"sg_reset -t /dev/sdg")
        dmesg1 = exec_cmd("dmesg | tail -2")
        return dmesg_c,reset,dmesg1


    def raid_level(self,raid_name,raid_level,raid_devices,raid_drives):
        if raid_level[0]:
            raid_create = exec_cmd(f"echo 'y'| mdadm --create {raid_name} --level={raid_level} --force --raid-devices={raid_devices} {raid_drives}")
            raid_details = exec_cmd(f"mdadm --detail {raid_name}")
            # raid_output = re.findall("")
            return raid_create,raid_details
        else:
            raid = exec_cmd(f"echo 'y'| mdadm --create {raid_name} --level={raid_level} --raid-devices={raid_devices} {raid_drives}")
            raid_details = exec_cmd(f"mdadm --detail {raid_name}")
            return raid,raid_details




x = Storage()
# print(x.list_drives())
# print(x.reset_drive())

raid_name = input("enter raidname: ")
raid_level = input("enter raidlevel: ")
raid_devices = input("enter raid devices: ")
raid_drives = input("enter raid drives: ")

print(x.raid_level(raid_name,raid_level,raid_devices,raid_drives))








