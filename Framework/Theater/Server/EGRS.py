from Config import ConsoleColor
from Utils import PacketEncoder, PacketDecoder

def ReceiveComponent(self, data):
    EGRSPacket = PacketEncoder.SetVar('TID', self.PacketID)
    EGRSPacket = PacketEncoder.encode('EGRS', EGRSPacket, 0x0, 0)
    self.GAMEOBJ.ClientTheaterNetworkInt.getHandle().sendall(EGRSPacket)