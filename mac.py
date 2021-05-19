#!/bin/python3
import subprocess
import optparse
import sys
import re
from colorama import Fore, Back, Style
def checkLinux(): # Checking platform for the script to run
    if sys.platform != "linux":
        print(Fore.RED+"Only works in Linux, Sorry")
        exit()

def printBanner(): #Printing the banner 
    print(Fore.LIGHTCYAN_EX+"Welcome to Mac-Changer V 13.37, please use --help for instructions")
    pass 

def parser(): #parsing the data 
    parser = optparse.OptionParser()
    parser.add_option("-i","--interface",dest="interface",help="Interface to change your Mac Address to, like eth0,wlan0")
    parser.add_option("-m","--mac",dest="mac",help="The New Mac Address, You want to change to, like 2A:21:54:9I:90:31")
    (options, arguments) = parser.parse_args()
    return (options.interface,options.mac)

def checkNull(interface,new_mac): # checking if the data is null
    if interface ==None or new_mac == None:
        print(Fore.LIGHTRED_EX+"Specify parameters please, use --help for info");
        exit()
        pass 

def mainwork(interface,new_mac): # changing the mac asddress
    print(Fore.WHITE+"Changing tha Mac Address of "+interface+" to "+new_mac)
    subprocess.call(["sudo", "ifconfig",interface,"down"])
    subprocess.call(["sudo","ifconfig",interface,"hw" ,"ether",new_mac])
    subprocess.call(["sudo","ifconfig",interface,"up"])
    return True
    pass

def checkChainged(interface,new_mac): # Going through Regex to see if your mac changed
    print(Fore.GREEN+"Checking if the mac address did change")
    output = subprocess.check_output(["sudo" ,"ifconfig",interface])
    regresult = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",output.decode('utf-8'))
    if regresult.group(0):
        if regresult.group(0) == new_mac.lower():
            print(Fore.GREEN+"Mac Address was successfully changed")
        else:
            print(Fore.RED+"Mac Address was not successfully changed")
    else:
        print("Error")

# Calling Functions
printBanner()
checkLinux()
parser()
interface,new_mac = parser()
checkNull(interface,new_mac)
work = mainwork(interface,new_mac)
if work == True:
    checkChainged(interface,new_mac)
else:
    print("something went wrong")
