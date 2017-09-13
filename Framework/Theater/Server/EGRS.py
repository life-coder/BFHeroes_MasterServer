from Config import ConsoleColor
from Utils import PacketEncoder, PacketDecoder

def ReceiveComponent(self, data):
    # TODO: If allowed = 1, add player to active players

    EGRSPacket = PacketEncoder.SetVar('TID', self.PacketID)
    EGRSPacket = PacketEncoder.encode('EGRS', EGRSPacket, 0x0, 0)

    self.transport.getHandle().sendall(EGRSPacket)