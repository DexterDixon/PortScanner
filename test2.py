import socket
import re
import sys
import argparse
from ipaddress import *

parser = argparse.ArgumentParser()
parser.add_argument("target", help="Scans ports of selected target.")
args = parser.parse_args()

def GetTarget():
    option = input("Choose an option" + "\n"
                "1: Enter Hostname" + "\n"
                "2: Enter IP Address" + "\n"
    )

    if(option == '1'):
        target = socket.gethostbyname(input("Enter Hostname Here: "))

    else:
        target = input("Enter the IP address:")
        while re.match("([0-9]{1,3}.){3}[0-9]{1,3}$", target) is None:
            print("Incorect format. Please try again.")
            target = input("Enter the IP address:")
        
    target = ip_address(target)
    return str(target)

def Scan(target):
    #target = GetTarget()
    print("-"* 60)
    print("Scanning target: " + target)
    print("-"* 60)
    socket.setdefaulttimeout(.00001)

    for i in range(1,1025):  
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:   
            result = sock.connect_ex((target, i))
        
        except socket.gaierror as e:
            print("Hostname could not be resolved.\n"), e
            error.append('Hostname could not be resolved.\n')
            sys.exit()
    
        except socket.error as e:
            print("Couldn't connect to server\n")
            error.append('Couldn't connect to server.\n')
            sys.exit()

        except Exception as e:
            print("Unknown error occured\n"), e
            error.append('Unknown error occured\n')
            sys.exit()
        
        if result == 0:
                print("Port %s is open on host %s" % (i, target))
                sock.close()
Scan(args.target)