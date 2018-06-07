from socket import *
import struct

sendData = struct.pack("!8sb5sb", 1, "test.jpg", 0, "octet", 0)

# udpSocked = socket(AF_INET, SOCK_DGRAM)
# udpSocked.sendto(sendData, ())
#
# udpSocked.close()

result = struct.unpack("!HH", sendData[:4])
print(result)
