from socket import * import os
import sys
import struct
import time import select import binascii
ICMP_ECHO_REQUEST = 8 MAX_HOPS = 30
TIMEOUT = 2.0
TRIES = 2
# The packet that we shall send to each router along the path is the ICMP echo # request packet, which is exactly what we had used in the ICMP ping exercise. # We shall use the same packet that we built in the Ping exercise
def checksum(string):
# In this function we make the checksum of our packet
# hint: see icmpPing lab #
def build_packet():
# In the sendOnePing() method of the ICMP Ping exercise ,firstly the header of our # packet to be sent was made, secondly the checksum was appended to the header and # then finally the complete packet was sent to the destination.
# Make the header in a similar way to the ping exercise. # Append checksum to the header.
# Don’t send the packet yet , just return the final packet in this function. # So the function ending should look like this
packet = header + data return packet
def get_route(hostname):
bytes])[0]
timeLeft = TIMEOUT
for ttl in range(1,MAX_HOPS):
for tries in range(TRIES):
destAddr = gethostbyname(hostname)
#Fill in start
# Make a raw socket named mySocket
#Fill in end
mySocket.setsockopt(IPPROTO_IP, IP_TTL, struct.pack('I', ttl)) mySocket.settimeout(TIMEOUT)
try:
d = build_packet()
mySocket.sendto(d, (hostname, 0))
t= time.time()
startedSelect = time.time()
whatReady = select.select([mySocket], [], [], timeLeft) howLongInSelect = (time.time() - startedSelect)
if whatReady[0] == []: # Timeout
print(" * * * Request timed out.") recvPacket, addr = mySocket.recvfrom(1024)
timeReceived = time.time()
timeLeft = timeLeft - howLongInSelect
if timeLeft <= 0: print(" *
except timeout: continue
else:
* *
Request timed out.")
#Fill in start
#Fetch the icmp type from the IP packet #Fill in end
if types == 11:
bytes = struct.calcsize("d")
timeSent = struct.unpack("d", recvPacket[28:28 +

(timeReceived -t)*1000, addr[0]))
bytes])[0] (timeReceived-t)*1000, addr[0]))
print(" %d rtt=%.0f ms
bytes])[0]
print(" %d (timeReceived - timeSent)*1000, addr[0]))
return
else:
print("error")
                           break
                    finally:
rtt=%.0f ms
get_route("google.com")
