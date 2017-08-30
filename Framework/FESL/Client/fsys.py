from Config import ConsoleColor, TheaterClientPort
from Utils import PacketEncoder, Globals
from time import strftime

def ReceiveComponent(self, txn):
    if txn == 'Hello':
        MemCheckPacket = 'TXN=MemCheck\n'
        MemCheckPacket += 'memcheck.[]=0\n'
        MemCheckPacket += 'salt=5\x00'

        MemCheckPacket = PacketEncoder.encode('fsys', MemCheckPacket, 0xC0000000, self.PacketID)

        GetSessionIdPacket = 'TXN=GetSessionId\x00'
        GetSessionIdPacket = PacketEncoder.encode('gsum', GetSessionIdPacket, 0x0, 0)

        self.PacketID += 1
        CurrentTime = strftime('%b-%d-%Y %H:%M:%S UTC')
        HelloPacket = 'curTime=' + CurrentTime + '\n'
        HelloPacket += 'messengerIp=' + Globals.ServerIP + '\n'
        HelloPacket += 'messengerPort=13505\n'
        HelloPacket += 'TXN=Hello\n'
        HelloPacket += 'domainPartition.subDomain=bfwest-dedicated\n'
        HelloPacket += 'theaterIp=' + Globals.ServerIP + '\n'
        HelloPacket += 'theaterPort=' + str(TheaterClientPort) + '\n'
        HelloPacket += 'domainPartition.domain=eagames\n'
        HelloPacket += 'activityTimeoutSecs=3600\x00'
        HelloPacket = PacketEncoder.encode('fsys', HelloPacket, 0xC0000000, self.PacketID)

        self.transport.getHandle().sendall(MemCheckPacket)
        self.transport.getHandle().sendall(GetSessionIdPacket)
        self.transport.getHandle().sendall(HelloPacket)
    else:
        print ConsoleColor('Warning') + '[FESLClient][fsys] Got unknown TXN (' + txn + ')' + ConsoleColor('End')
