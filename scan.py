import socket
import re
from ipaddress import *

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
    return target

def Scan():
    target = str(GetTarget())
    print("-"* 60)
    print ("Scanning target: " + target)
    print ("-"* 60)
    socket.setdefaulttimeout(.00001)
    try:
        for i in range(1,1025):  
        
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((target, i))
            if result == 0:
                print("Port %s is open on host %s" % (i, target))
                sock.close()
    
    except socket.error as error:
        pass
Scan()