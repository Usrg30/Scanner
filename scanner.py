import optparse
from socket import *


def connexionScan(tgtHost: str, tgtPort: int) -> None:
    try:
        connSock = socket(AF_INET, SOCK_STREAM)
        connSock.connect((tgtHost, tgtPort))
        print(f'[+] {tgtPort} Abierto')
        connSock.close()
    except:
        print(f'[-] {tgtPort} Cerrado')


def portScann(tgtHost: str, tgtPorts: list[int]) -> None:
    try:
        tgtIp: str = gethostbyname(tgtHost)
    except:
        print(f'[-] No se puede resolver {tgtHost} : Host no encontrado')
        return
    try:
        tgtName: tuple[str, list[str], list[str]] = gethostbyaddr(tgtIp)
        print(f'\n [+] Resultado del escaneo {tgtName[0]}')
    except:
        print(f'[+] Resultado del escaneo {tgtIp}')
    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        print(f'Escaneando puerto {tgtPort}')
        connexionScan(tgtHost, int(tgtPort))











parser = optparse.OptionParser('usage %prog -h' + '<target host> -p <target port>')
parser.add_option('-h', dest='tgtHost', type='string', help='especifica el host objetivo')
parser.add_option('-p', dest='tgtPort', type='int', help='indica el puerto')
(options, args) = parser.parse_args()
tgtHost = options.tgtHost
tgtPort = options.tgtPort
if tgtHost == None | tgtPort == None:
    print(parser.usage)
    exit(0)
