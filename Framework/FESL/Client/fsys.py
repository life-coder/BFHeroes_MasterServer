from Config import ConsoleColor, TheaterClientPort
from Utils import PacketEncoder, Globals
from time import strftime

def ReceiveComponent(self, txn):
    if txn == 'Hello':
        MemCheckPacket = PacketEncoder.SetVar('TXN', 'MemCheck')
        MemCheckPacket += PacketEncoder.SetVar('memcheck.[]', 0)
        MemCheckPacket += PacketEncoder.SetVar('salt', 5, True)

        MemCheckPacket = PacketEncoder.encode('fsys', MemCheckPacket, 0xC0000000, self.PacketID)

        GetSessionIdPacket = PacketEncoder.SetVar('TXN', 'GetSessionId', True)
        GetSessionIdPacket = PacketEncoder.encode('gsum', GetSessionIdPacket, 0x0, 0)

        self.PacketID += 1
        CurrentTime = strftime('%b-%d-%Y %H:%M:%S UTC')
        HelloPacket = PacketEncoder.SetVar('curTime', CurrentTime)
        HelloPacket += PacketEncoder.SetVar('messengerIp', Globals.ServerIP)
        HelloPacket += PacketEncoder.SetVar('messengerPort', 13505)
        HelloPacket += PacketEncoder.SetVar('TXN', 'Hello')
        HelloPacket += PacketEncoder.SetVar('domainPartition.subDomain', 'bfwest-dedicated')
        HelloPacket += PacketEncoder.SetVar('theaterIp', Globals.ServerIP)
        HelloPacket += PacketEncoder.SetVar('theaterPort', TheaterClientPort)
        HelloPacket += PacketEncoder.SetVar('domainPartition.domain', 'eagames')
        HelloPacket += PacketEncoder.SetVar('activityTimeoutSecs', 3600, True)
        HelloPacket = PacketEncoder.encode('fsys', HelloPacket, 0xC0000000, self.PacketID)

        self.transport.getHandle().sendall(MemCheckPacket)
        self.transport.getHandle().sendall(GetSessionIdPacket)
        self.transport.getHandle().sendall(HelloPacket)

    elif txn == 'MemCheck':
        # Unneeded
        pass

    elif txn == 'Goodbye':
        # Unneeded
        pass

    elif txn == 'GetPingSites':
        self.PacketID += 1
        GetPingSitesPacket = PacketEncoder.SetVar('TXN', 'GetPingSites')
        GetPingSitesPacket += PacketEncoder.SetVar('minPingSitesToPing', 2)
        GetPingSitesPacket += PacketEncoder.SetVar('pingSites.[]', 2)
        GetPingSitesPacket += PacketEncoder.SetVar('pingSites.0.addr', Globals.ServerIP)
        GetPingSitesPacket += PacketEncoder.SetVar('pingSites.0.name', 'gva')
        GetPingSitesPacket += PacketEncoder.SetVar('pingSites.0.type', 0)
        GetPingSitesPacket += PacketEncoder.SetVar('pingSites.1.addr', Globals.ServerIP)
        GetPingSitesPacket += PacketEncoder.SetVar('pingSites.1.name', 'nrt')
        GetPingSitesPacket += PacketEncoder.SetVar('pingSites.1.type', 0)
        GetPingSitesPacket += PacketEncoder.encode('fsys', GetPingSitesPacket, 0xC0000000, self.PacketID)
    else:
        print ConsoleColor('Warning') + '[FESLClient][fsys] Got unknown TXN (' + txn + ')' + ConsoleColor('End')
