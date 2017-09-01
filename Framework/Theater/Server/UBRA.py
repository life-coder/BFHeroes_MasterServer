from Config import ConsoleColor
from Utils import PacketEncoder

def ReceiveComponent(self, data):
    UBRAPacket = PacketEncoder.SetVar('TID', self.PacketID)
    UBRAPacket = PacketEncoder.encode('UBRA', UBRAPacket, 0x0, 0)
    self.transport.getHandle().sendall(UBRAPacket)
