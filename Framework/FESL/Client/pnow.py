from Config import ConsoleColor
from Utils import PacketEncoder, PacketDecoder, DataClass, Globals, RandomStringGenerator
from Framework.Database import GetWebSession, GetUserName, GetEmail, GetAccountID

def ReceiveComponent(self, data, txn):
    if txn == 'Start':
        print ConsoleColor('Info') + '[FESLClient][Matchmatching] Started matchmatching...' + ConsoleColor('End')

        StartPacket = PacketEncoder.SetVar('TXN', 'Start')
        StartPacket += PacketEncoder.SetVar('id.id', 1)
        StartPacket += PacketEncoder.SetVar('id.partition', '/eagames/bfwest-dedicated', True)
        StartPacket = PacketEncoder.encode('pnow', StartPacket, 0xC0000000, self.PacketID)
        self.transport.getHandle().sendall(StartPacket)

        StatusPacket = PacketEncoder.SetVar('TXN', 'Status')
        StatusPacket += PacketEncoder.SetVar('id.id', 1)
        StatusPacket += PacketEncoder.SetVar('id.partition', '/eagames/bfwest-dedicated')
        StatusPacket += PacketEncoder.SetVar('sessionState', 'COMPLETE')
        StatusPacket += PacketEncoder.SetVar('props.{}.[]', 2)
        StatusPacket += PacketEncoder.SetVar('props.{resultType}', 'JOIN')

        if len(Globals.Servers) != 0:
            # Return latest server #TODO: Do it better
            print ConsoleColor('Success') + '[FESLClient][Matchmatching] Game found!' + ConsoleColor('End')
            StatusPacket += PacketEncoder.SetVar('props.{games}.0.lid', 1)
            StatusPacket += PacketEncoder.SetVar('props.{games}.0.fit', 1001)
            StatusPacket += PacketEncoder.SetVar('props.{games}.0.gid', Globals.CurrentGameID - 1)
            StatusPacket += PacketEncoder.SetVar('props.{games}.[]', 1)
        else:
            print ConsoleColor('Warning') + '[FESLClient][Matchmatching] No games found!' + ConsoleColor('End')
            StatusPacket += PacketEncoder.SetVar('props.{games}.[]', 0)

        StatusPacket = PacketEncoder.encode('pnow', StatusPacket, 0x80000000, 0)
        self.transport.getHandle().sendall(StatusPacket)
