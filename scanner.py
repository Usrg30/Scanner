#!/usr/bin/python3

import optparse
import socket
from socket import *
from colors import *


def connexionScan(tgtHost: str, tgtPort: int) -> None:
    try:
        connSock: socket = socket(AF_INET, SOCK_STREAM)
        connSock.connect((tgtHost, tgtPort))
        connSock.send(('scan\r\n').encode("utf-8"))
        result: bytes = connSock.recv(100)
        print(f'{VERDE}  [+] {tgtPort}/tcp Abierto')
        print(f'{CIAN}{ITALIC}[+] {result}\n{RESET}')
        connSock.close()
    except:
        print(f'{ROJO}  [-] {tgtPort} Cerrado\n{RESET}')
    
       


def portScann(tgtHost: str, tgtPorts: list[int]) -> None:
    try:
        tgtIp: str = gethostbyname(tgtHost)
    except:
        print(f'{NEGRITA}{AMARILLO}[-] No se puede resolver {tgtHost} : Host no encontrado{RESET}')
        return
    try:
        tgtName: tuple[str, list[str], list[str]] = gethostbyaddr(tgtIp)
        print(f'\n{NEGRITA}{AMARILLO}[+] Resultado del escaneo {tgtName[0]}\n{RESET}')
    except:
        print(f'{NEGRITA}{AMARILLO}[+] Resultado del escaneo {tgtIp}{RESET}')
    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        print(f'{SUBRRAYADO}{AMARILLO}Puerto:{RESET}')
        connexionScan(tgtHost, int(tgtPort))


def main():
    parser: optparse.OptionParser = optparse.OptionParser('usage%prog -h' + '<target host> -p <target port>')
    parser.add_option('-H', dest='tgtHost', type='string', help='especifica el host objetivo')
    parser.add_option('-p', dest='tgtPort', type='string', help='indica el puerto')
    (options, args) = parser.parse_args()
    tgtHost: str = options.tgtHost
    tgtPorts: list[int] = options.tgtPort.split(',')
    if (tgtHost == None) | (tgtPorts[0] == None):
        print(parser.usage)
        exit(0)
    portScann(tgtHost, tgtPorts)


if __name__=='__main__':
    main()