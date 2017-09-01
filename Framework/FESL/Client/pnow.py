from Config import ConsoleColor
from Utils import PacketEncoder, PacketDecoder, DataClass, Globals, RandomStringGenerator
from Framework.Database import GetWebSession, GetUserName, GetEmail, GetAccountID

def ReceiveComponent(self, data, txn):
    if txn == 'Start':
        print '[FESLClient][Matchmatching] Started matchmatching...'

        StartPacket = PacketEncoder.SetVar('TXN', 'Start')
        StartPacket += PacketEncoder.SetVar('id.id', '1')
        StartPacket += PacketEncoder.SetVar('id.partition', PacketDecoder.decode(data).GetVar('partition.partition'))
        StartPacket = PacketEncoder.encode('pnow', StartPacket, 0xC0000000, self.PacketID)
        self.transport.getHandle().sendall(StartPacket)