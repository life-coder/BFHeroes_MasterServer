from Config import ConsoleColor
from Utils import PacketEncoder, PacketDecoder

def ReceiveComponent(self, data):
    # Remove player from server
    print ConsoleColor('Info') + '[TheaterServer][PLVT] Client has been kicked from game!' + ConsoleColor('End')

    KICKPacket = PacketEncoder.SetVar('PID', 1) # TODO: Make it non-static
    KICKPacket += PacketEncoder.SetVar('LID', 1) # LobbyID
    KICKPacket += PacketEncoder.SetVar('GID', self.GAMEOBJ.GameID, True)
    KICKPacket = PacketEncoder.encode('KICK', KICKPacket, 0x0, 0)
    self.transport.getHandle().sendall(KICKPacket)

    PLVTPacket = PacketEncoder.SetVar('TID', self.PacketID, True)
    PLVTPacket = PacketEncoder.encode('PLVT', PLVTPacket, 0x0, 0)
    self.transport.getHandle().sendall(PLVTPacket)