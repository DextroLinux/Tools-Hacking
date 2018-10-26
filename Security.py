import os, sys, time
from time import sleep as timeout
def restart_program():
        python = sys.executable
        os.execl(python, python, * sys.argv)
        curdir = os.getcwd()
print "Creado Por : D3XTRO "
print "GitHub : https://github.com/DextroLinux"
print "Facebook : https://www.facebook.com/Shany15.06.17"
print "YouTube : https://www.youtube.com/channel/UCk14G9pHkfzsFMD14snabFw"
print "           [1]> Brute Force              "
print "           [2]> DDos Attack              "
print "           [3]> NMap PortScanner         "
print "           [4]> Install Tools Hacking    "
print 
print " [0]> Exit "
print
A = raw_input("D3XTR0 ==>> ")

if A == "1" or A == "01":
  os.system("python2 brute.py")

elif A == "2" or A == "02":
    os.system("clear")
    os.system("figlet DDOS Attack")
    ip = raw_input("IP Address : ")
    port = raw_input("Port       : ")
    packet =raw_input("Packet     : ")
    os.system("python2 pntddos %s %s %s" % (ip, port, packet))

elif A == "3" or A == "03":
    os.system("clear")
    os.system("figlet NMap Scan")
    host = raw_input("Host : ")
    os.system("nmap %s" % (host))

elif A == "4" or A == "04":
    os.system("python2 lazymux.py")
    
elif A == "0" or A == "00":
    sys.exit()
    
else:
     print "\nERROR: Wrong Input"
     timeout(3)
     restart_program()
