from twisted.internet.protocol import Protocol, DatagramProtocol
from Config import ConsoleColor
from Utils import PacketDecoder
from Framework.Theater.Server import CONN, USER, CGAM, UBRA, UGAM, EGRS, ECHO, PLVT

class HANDLER(Protocol):
    def __init__(self):
        self.DATABUFF = ''
        self.GAMEOBJ = None
        self.PacketID = 0

    def timeoutConnection(self):
        print ConsoleColor('Warning') + '[TheaterServer] Closed connection to ' + self.ip + ':' + str(
            self.port) + ' Reason: Connection Timeout' + ConsoleColor('End')

    def connectionMade(self):
        self.ip, self.port = self.transport.client
        print ConsoleColor('Info') + '[TheaterServer] Got connection from ' + self.ip + ':' + str(
            self.port) + ConsoleColor('End')
        return

    def connectionLost(self, reason):
        print ConsoleColor('Info') + '[TheaterServer] Lost connection to ' + self.ip + ':' + str(
            self.port) + ConsoleColor('End')

        return

    def readConnectionLost(self):
        print ConsoleColor('Info') + '[TheaterServer] Lost connection to ' + self.ip + ':' + str(
            self.port) + ConsoleColor('End')
        self.transport.loseConnection()
        return

    def writeConnectionLost(self):
        print ConsoleColor('Warning') + '[TheaterServer] Closed connection to ' + self.ip + ':' + str(
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
        elif Command == 'CGAM':
            CGAM.ReceiveComponent(self, data)
        elif Command == 'UBRA':
            UBRA.ReceiveComponent(self, data)
        elif Command == 'UGAM':
            UGAM.ReceiveComponent(self, data)
        elif Command == 'EGRS':
            EGRS.ReceiveComponent(self, data)
        elif Command == 'PLVT':
            PLVT.ReceiveComponent(self, data)
        else:
            print ConsoleColor(
                'Warning') + '[TheaterServer] Warning! Got unknown command (' + Command + ']!' + ConsoleColor(
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
                'Warning') + '[TheaterServer] Warning! Got unknown command (' + Command + ']!' + ConsoleColor(
                'End')