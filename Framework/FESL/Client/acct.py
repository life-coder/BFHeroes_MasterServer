from Config import ConsoleColor
from Utils import PacketEncoder, PacketDecoder
def ReceiveComponent(self, data, txn):
    if txn == 'NuLogin':
        LoginPacket = PacketEncoder.SetVar('TXN', 'NuLogin')
        LoginPacket += PacketEncoder.SetVar('localizedMessage', '"The user is not entitled to access this game"')
        LoginPacket += PacketEncoder.SetVar('errorContainer.[]', 0)
        LoginPacket += PacketEncoder.SetVar('errorCode', 120, True)
        LoginPacket = PacketEncoder.encode('acct', LoginPacket, 0xC0000000, self.PacketID)
        self.transport.getHandle().sendall(LoginPacket)
        self.transport.loseConnection()
    else:
        print '[FESLClient][acct] Got unknown TXN (' + txn + ')'