from twisted.internet.protocol import Protocol
from Config import ConsoleColor

class HANDLER(Protocol):
    def __init__(self):
        self.DATABUFF = ''
        self.GAMEOBJ = None

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
        print '[TheaterServer] ' + str(data.split())