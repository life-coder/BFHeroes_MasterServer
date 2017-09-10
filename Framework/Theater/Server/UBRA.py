from Config import ConsoleColor
from Utils import PacketEncoder
import UGAM

def ReceiveComponent(self, data):
    UBRAPacket = PacketEncoder.SetVar('TID', self.PacketID)
    UBRAPacket = PacketEncoder.encode('UBRA', UBRAPacket, 0x0, 0)
    self.transport.getHandle().sendall(UBRAPacket)

    if data.find('UGAM') != -1:
        data = data.split('UGAM')[1]
        UGAM.ReceiveComponent(self, data)