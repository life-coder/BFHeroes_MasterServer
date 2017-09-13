from Utils import PacketEncoder, PacketDecoder, Globals
from Config import ConsoleColor

def ReceiveComponent(self, data):
    print ConsoleColor('Info') + '[TheaterManager][ECNL] Client disconnected from server....' + ConsoleColor('End')
    ECHLPacket = PacketEncoder.SetVar('LID', PacketDecoder.decode(data).GetVar('LID'))
    ECHLPacket += PacketEncoder.SetVar('GID', PacketDecoder.decode(data).GetVar('GID'))
    ECHLPacket += PacketEncoder.SetVar('TID', self.PacketID, True)
    ECHLPacket = PacketEncoder.encode('ECHL', ECHLPacket, 0x0, 0)
    self.transport.getHandle().sendall(ECHLPacket)
