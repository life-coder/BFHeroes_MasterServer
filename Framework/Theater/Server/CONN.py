from Utils import PacketEncoder, PacketDecoder
import time

def ReceiveComponent(self, data):
    ConnPacket = PacketEncoder.SetVar('TID', self.PacketID)
    ConnPacket += PacketEncoder.SetVar('TIME', str(time.time()).split('.')[0])
    ConnPacket += PacketEncoder.SetVar('activityTimeoutSecs', 3600)
    ConnPacket += PacketEncoder.SetVar('PROT', PacketDecoder.decode(data).GetVar('PROT'))

    ConnPacket = PacketEncoder.encode('CONN', ConnPacket, 0x0, 0)
    self.transport.getHandle().sendall(ConnPacket)