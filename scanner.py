import optparse

parser = optparse.OptionParser('usage %prog -h' + '<target host> -p <target port>')
parser.add_option('-h', dest='tgtHost', type='string', help='especifica el host objetivo')
parser.add_option('-p', dest='tgtPort', type='int', help='indica el puerto')
(options, args) = parser.parse_args()
tgtHost = options.tgtHost
tgtPort = options.tgtPort
if tgtHost == None | tgtPort == None:
    print(parser.usage)
    exit(0)
