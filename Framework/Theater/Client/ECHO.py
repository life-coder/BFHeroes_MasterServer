from Config import ConsoleColor
from Utils import PacketEncoder, PacketDecoder

def ReceiveComponent(self, data, (host, port)):
    ECHOPacket = PacketEncoder.SetVar('TID', self.PacketID)
    ECHOPacket += PacketEncoder.SetVar('TXN', '')
    ECHOPacket += PacketEncoder.SetVar('IP', host)
    ECHOPacket += PacketEncoder.SetVar('PORT', port)
    ECHOPacket += PacketEncoder.SetVar('ERR', 0)
    ECHOPacket += PacketEncoder.SetVar('TYPE', 1)
    ECHOPacket = PacketEncoder.encode('ECHO', ECHOPacket, 0x0, 0)
    self.transport.write(ECHOPacket, (host, port))