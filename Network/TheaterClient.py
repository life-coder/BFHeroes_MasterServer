from twisted.internet.protocol import Protocol, DatagramProtocol
from Config import ConsoleColor
from Utils import PacketDecoder
from Framework.Theater.Client import CONN, USER, GDAT, ECNL, EGAM, ECHO

class HANDLER(Protocol):
    def __init__(self):
        self.DATABUFF = ''
        self.GAMEOBJ = None
        self.PacketID = 0

    def timeoutConnection(self):
        print ConsoleColor('Warning') + '[TheaterClient] Closed connection to ' + self.ip + ':' + str(
            self.port) + ' Reason: Connection Timeout' + ConsoleColor('End')

    def connectionMade(self):
        self.ip, self.port = self.transport.client
        print ConsoleColor('Info') + '[TheaterClient] Got connection from ' + self.ip + ':' + str(
            self.port) + ConsoleColor('End')
        return

    def connectionLost(self, reason):
        print ConsoleColor('Info') + '[TheaterClient] Lost connection to ' + self.ip + ':' + str(
            self.port) + ConsoleColor('End')

        return

    def readConnectionLost(self):
        print ConsoleColor('Info') + '[TheaterClient] Lost connection to ' + self.ip + ':' + str(
            self.port) + ConsoleColor('End')
        self.transport.loseConnection()
        return

    def writeConnectionLost(self):
        print ConsoleColor('Warning') + '[TheaterClient] Closed connection to ' + self.ip + ':' + str(
            self.port) + ConsoleColor('End')
        self.transport.loseConnection()
        return

    def dataReceived(self, data):
        try:
            Command = PacketDecoder.decode(data).GetCommand()
            self.PacketID += 1
        except:
            Command = 'null'

        if Command == 'CONN':
            CONN.ReceiveComponent(self, data)
        elif Command == 'USER':
            USER.ReceiveComponent(self, data)
        elif Command == 'GDAT':
            GDAT.ReceiveComponent(self, data)
        elif Command == 'ECNL':
            ECNL.ReceiveComponent(self, data)
        elif Command == 'EGAM':
            EGAM.ReceiveComponent(self, data)
        else:
            print ConsoleColor(
                'Warning') + '[TheaterClient] Warning! Got unknown command (' + Command + ']!' + ConsoleColor(
                'End')

class HANDLER_UDP(DatagramProtocol):

    def __init__(self):
        self.PacketID = 0

    def datagramReceived(self, data, (host, port)):
        try:
            Command = PacketDecoder.decode(data).GetCommand()
            self.PacketID += 1
        except:
            Command = 'null'

        if Command == 'ECHO':
            ECHO.ReceiveComponent(self, data, (host, port))
        else:
            print ConsoleColor(
                'Warning') + '[TheaterClient] Warning! Got unknown command (' + Command + ']!' + ConsoleColor(
                'End')