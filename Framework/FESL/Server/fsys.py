from Config import ConsoleColor, TheaterServerPort
from Utils import PacketEncoder, Globals
from time import strftime

def ReceiveComponent(self, txn):
    if txn == 'Hello':
        MemCheckPacket = PacketEncoder.SetVar('TXN', 'MemCheck')
        MemCheckPacket += PacketEncoder.SetVar('memcheck.[]', 0)
        MemCheckPacket += PacketEncoder.SetVar('salt', 5, True)

        MemCheckPacket = PacketEncoder.encode('fsys', MemCheckPacket, 0xC0000000, self.PacketID)

        self.PacketID += 1
        CurrentTime = strftime('%b-%d-%Y %H:%M:%S UTC')
        HelloPacket = PacketEncoder.SetVar('curTime', CurrentTime)
        HelloPacket += PacketEncoder.SetVar('messengerIp', Globals.ServerIP)
        HelloPacket += PacketEncoder.SetVar('messengerPort', 13505)
        HelloPacket += PacketEncoder.SetVar('TXN', 'Hello')
        HelloPacket += PacketEncoder.SetVar('domainPartition.subDomain', 'bfwest-server')
        HelloPacket += PacketEncoder.SetVar('theaterIp', Globals.ServerIP)
        HelloPacket += PacketEncoder.SetVar('theaterPort', TheaterServerPort)
        HelloPacket += PacketEncoder.SetVar('domainPartition.domain', 'eagames')
        HelloPacket += PacketEncoder.SetVar('activityTimeoutSecs', 3600, True)
        HelloPacket = PacketEncoder.encode('fsys', HelloPacket, 0xC0000000, self.PacketID)

        self.transport.getHandle().sendall(MemCheckPacket)
        self.transport.getHandle().sendall(HelloPacket)

    elif txn == 'MemCheck':
        # Unneeded
        pass

    elif txn == 'Goodbye':
        # Unneeded
        pass

    else:
        print ConsoleColor('Warning') + '[FESLServer][fsys] Got unknown TXN (' + txn + ')' + ConsoleColor('End')
