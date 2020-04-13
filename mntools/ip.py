import re
import random


class IP:
    address = ""
    regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                    25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                    25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                    25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)'''

    def __init__(self):
        for octet in range(0, 3):
            self.address += str(random.randrange(0, 256)) + '.'

        self.address += str(random.randrange(0, 256))

    def __init__(self, prefix=""):


def isValidIP(IPstring):
    regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
                25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)'''

    if(re.search(regex, IPstring)):
        return True
    else:
        return False

def randomIP(subnetMask='', prefix=None):
    ip = ""
    for octet in range(0,3):
        ip = ip + str(random.randrange(0,256)) + '.'

    ip += str(random.randrange(0,256))

    if prefix != None:
        ip = prefix
        while len(ip) < 11:
            ip = ip + str(random.randrange(0,256)) + '.'

        ip += str(random.randrange(0,256))


    return ip+subnetMask


