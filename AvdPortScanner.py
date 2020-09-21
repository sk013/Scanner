from socket import *
import optparse
from threading import *


def conscan(tgtHost, tgtPort):
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((tgtHost, tgtPort))
        print('%d/tcp is open ' % tgtPort)
    except:
        print('%d/tcp is closed ' % tgtPort)
    finally:
        sock.close()


def portscan(tgtHost, tgtPort):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print('unknown host %s ' % tgtHost)
    try:
        tgtName = gethostbyaddr(tgtIP)
        print('scan results for ' + tgtName[0])
    except:
        print('scan results for ' + tgtIP)
    setdefaulttimeout(1)
    for tgtP in tgtPort:
        t = Thread(target=conscan, args=(tgtHost, int(tgtP)))
        t.start()


def main():
    parser = optparse.OptionParser('usage of program ' + '-H <target host> -p <target port>')
    parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
    parser.add_option('-p', dest='tgtPort', type='string', help='specify target port')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPort = str(options.tgtPort).split(',')
    if (tgtHost == None) | (tgtPort[0] == None):
        print(parser.usage)
        exit(0)
    portscan(tgtHost, tgtPort)


if __name__ == '__main__':
    main()
