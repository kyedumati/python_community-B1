

import random
import scapy
print ("Test")
HIGH_EPHEM_PORT_RANGE_NUMBER = 60999
LOW_EPHEM_PORT_RANGE_NUMBER = 32768
EPHEM_PORTS = list(range(LOW_EPHEM_PORT_RANGE_NUMBER, HIGH_EPHEM_PORT_RANGE_NUMBER))
print(EPHEM_PORTS)
CLOSED_PORTS=[]
VICTIM_IP = ""
RESOLVER_IP = ""
TARGET_NAME = ""
POSION_IP = ""
success=0
def doCheck(ephem_ports, closed_port=1):
# send 50 UDP packets spoofing the RESOLVER_IP to the VICTIM_IP
# send UDP packet to the VICTIM_IP to closed_port and wait for reply
# if ICMP received:
#   return True
# else:
#   return False

def doPosion(ephem_port,success=None):
    return 1

    # Use scapy to send 65,535 DNS Replies for all possible DNS Magic Numbers
    # Spoof the RESOLVER_IP
    # Send the POSION_IP instead of the real IP for www.example.com
    #

        def naga():
            result = False
            closed_port = 1
            old_index = 0
            new_index = 50
            ephem_ports = []

            while not result:
                ports = EPHEM_PORTS[old_index:new_index]
                print(ports)
                result = doCheck(ports=ephem_ports, closed_port=1)
                if not result:
                    old_index = new_index
                    new_index = old_index + 50

    #
    # Do binary search over the ephem_ports list
    #
    #  Im too tired to think this bit through right now :p
    #

            result = False
            old_index = 0
            new_index = 25

            while not result:
                final_ephem_ports = ephem_ports[old_index:new_index]
                final_ephem_ports.extend(CLOSED_PORTS[0:25])
               # result = doCheck(ports=final_ephem_ports, closed_port=1)
                result =0
                if not result:
                    if new_index == 25:
                        old_index = 25
                        new_index = 50
                    elif new_index == 50:
                        # We did not find the Open Port again in this list
                        # It may be closed already or may not have been false positive
                        new_index = 50
                    else:
                        #
                        # Now we need to split the 25 in half and fill in the rest
                        # with CLOSED_PORTS
                        #
                        #
                        # Port Found
                        #
                        success = doPosion(ephem_port)
        naga()
doPosion(EPHEM_PORTS)

    if success:
        print ("Pwn All The Things!")
    else:
        print ("I should loop this program to just keep going instead of quitting here")

if __name__ == '__main__':
    doCheck(EPHEM_PORTS)

