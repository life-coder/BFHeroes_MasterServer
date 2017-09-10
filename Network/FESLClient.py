from twisted.internet.protocol import Protocol
from Config import ConsoleColor
from Utils import PacketDecoder
from Framework.FESL.Client import fsys, acct, rank, pnow

class HANDLER(Protocol):
    def __init__(self):
        self.DATABUFF = ''
        self.GAMEOBJ = None
        self.PacketID = 0

    def timeoutConnection(self):
        print ConsoleColor('Warning') + '[FESLClient] Closed connection to ' + self.ip + ':' + str(
            self.port) + ' Reason: Connection Timeout' + ConsoleColor('End')

    def connectionMade(self):
        self.ip, self.port = self.transport.client
        print ConsoleColor('Info') + '[FESLClient] Got connection from ' + self.ip + ':' + str(
            self.port) + ConsoleColor('End')
        return

    def connectionLost(self, reason):
        print ConsoleColor('Info') + '[FESLClient] Lost connection to ' + self.ip + ':' + str(
            self.port) + ConsoleColor('End')

        return

    def readConnectionLost(self):
        print ConsoleColor('Info') + '[FESLClient] Lost connection to ' + self.ip + ':' + str(
            self.port) + ConsoleColor('End')
        self.transport.loseConnection()
        return

    def writeConnectionLost(self):
        print ConsoleColor('Warning') + '[FESLClient] Closed connection to ' + self.ip + ':' + str(
            self.port) + ConsoleColor('End')
        self.transport.loseConnection()
        return

    def dataReceived(self, data):
        # Check if packet are correct, if not set command and txn to null
        try:
            Command = PacketDecoder.decode(data).GetCommand()
            TXN = PacketDecoder.decode(data).GetTXN()
        except:
            Command = 'null'
            TXN = 'null'

        if Command == 'fsys':
            fsys.ReceiveComponent(self, TXN)
        elif Command == 'acct':
            self.PacketID += 1
            acct.ReceiveComponent(self, data, TXN)
        elif Command == 'rank':
            self.PacketID += 1
            rank.ReceiveComponent(self, data, TXN)
        elif Command == 'pnow':
            self.PacketID += 1
            pnow.ReceiveComponent(self, data, TXN)
        else:
            print ConsoleColor('Warning') + '[FESLClient] Warning! Got unknown command (' + Command + '] and unknown TXN (' + TXN + ')!' + ConsoleColor('End')