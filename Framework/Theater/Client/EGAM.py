from Utils import PacketEncoder, PacketDecoder, Globals
from Config import ConsoleColor

def ReceiveComponent(self, data):
    try:
        self.ServerGAMEOBJ
    except:
        return ''

    if self.ServerGAMEOBJ != None:
        self.ServerGAMEOBJ.ClientTheaterNetworkInt = self.transport
        EGAMPacket = PacketEncoder.SetVar('LID', PacketDecoder.decode(data).GetVar('LID'))
        EGAMPacket += PacketEncoder.SetVar('GID', PacketDecoder.decode(data).GetVar('GID'))
        EGAMPacket += PacketEncoder.SetVar('TID', self.PacketID)
        EGAMPacket = PacketEncoder.encode('EGAM', EGAMPacket, 0x0, 0)
        self.transport.getHandle().sendall(EGAMPacket)

        self.GAMEOBJ.EXTPORT = PacketDecoder.decode(data).GetVar('PORT')
        # Using static stats until i'm preparing stats management

        ServerEGRQPacket = PacketEncoder.SetVar('TID', 0)
        ServerEGRQPacket += PacketEncoder.SetVar('NAME', 'TestSoldier1')
        ServerEGRQPacket += PacketEncoder.SetVar('UID', 1)
        ServerEGRQPacket += PacketEncoder.SetVar('PID', 9)
        ServerEGRQPacket += PacketEncoder.SetVar('TICKET', 2018751182)
        ServerEGRQPacket += PacketEncoder.SetVar('IP', self.GAMEOBJ.EXTIP)
        ServerEGRQPacket += PacketEncoder.SetVar('PORT', self.GAMEOBJ.EXTPORT)
        ServerEGRQPacket += PacketEncoder.SetVar('INT-IP', PacketDecoder.decode(data).GetVar('R-INT-IP'))
        ServerEGRQPacket += PacketEncoder.SetVar('INT-PORT', PacketDecoder.decode(data).GetVar('R-INT-PORT'))

        ServerEGRQPacket += PacketEncoder.SetVar('PTYPE', PacketDecoder.decode(data).GetVar('PTYPE'))
        ServerEGRQPacket += PacketEncoder.SetVar('R-USER', 'TestSoldier1')
        ServerEGRQPacket += PacketEncoder.SetVar('R-UID', 1)
        ServerEGRQPacket += PacketEncoder.SetVar('R-U-accid', 1)
        ServerEGRQPacket += PacketEncoder.SetVar('R-U-elo', 1)
        ServerEGRQPacket += PacketEncoder.SetVar('R-U-team', 1)
        ServerEGRQPacket += PacketEncoder.SetVar('R-U-kit', 1)
        ServerEGRQPacket += PacketEncoder.SetVar('R-U-lvl', 1)
        ServerEGRQPacket += PacketEncoder.SetVar('R-U-dataCenter', 'iad')
        ServerEGRQPacket += PacketEncoder.SetVar('R-U-externalIp', self.GAMEOBJ.EXTIP)
        ServerEGRQPacket += PacketEncoder.SetVar('R-U-internalIp', PacketDecoder.decode(data).GetVar('R-INT-IP'))
        ServerEGRQPacket += PacketEncoder.SetVar('R-U-category', PacketDecoder.decode(data).GetVar('R-U-category'))
        ServerEGRQPacket += PacketEncoder.SetVar('R-INT-IP', PacketDecoder.decode(data).GetVar('R-INT-IP'))
        ServerEGRQPacket += PacketEncoder.SetVar('R-INT-PORT', PacketDecoder.decode(data).GetVar('R-INT-PORT'))

        ServerEGRQPacket += PacketEncoder.SetVar('XUID', 24)
        ServerEGRQPacket += PacketEncoder.SetVar('R-XUID', 24)

        ServerEGRQPacket += PacketEncoder.SetVar('LID', PacketDecoder.decode(data).GetVar('LID'))
        ServerEGRQPacket += PacketEncoder.SetVar('GID', PacketDecoder.decode(data).GetVar('GID'))

        ServerEGRQPacket = PacketEncoder.encode('EGRQ', ServerEGRQPacket, 0x0, 0)
        self.ServerGAMEOBJ.TheaterNetworkInt.getHandle().sendall(ServerEGRQPacket)

        self.PacketID += 1
        ClientEGEGPacket = PacketEncoder.SetVar('TID', self.PacketID)
        ClientEGEGPacket += PacketEncoder.SetVar('PL', 'PC')
        ClientEGEGPacket += PacketEncoder.SetVar('TICKET', 2018751182)

        ClientEGEGPacket += PacketEncoder.SetVar('PID', 9)
        ClientEGEGPacket += PacketEncoder.SetVar('I', PacketDecoder.decode(data).GetVar('R-INT-IP'))
        ClientEGEGPacket += PacketEncoder.SetVar('P', PacketDecoder.decode(data).GetVar('R-INT-PORT'))
        ClientEGEGPacket += PacketEncoder.SetVar('HUID', 1)
        ClientEGEGPacket += PacketEncoder.SetVar('EKEY', 'O65zZ2D2A58mNrZw1hmuJw%3d%3d')
        ClientEGEGPacket += PacketEncoder.SetVar('INT-IP', PacketDecoder.decode(data).GetVar('R-INT-IP'))
        ClientEGEGPacket += PacketEncoder.SetVar('INT-PORT', PacketDecoder.decode(data).GetVar('R-INT-PORT'))
        ClientEGEGPacket += PacketEncoder.SetVar('SECRET', 2587913)
        ClientEGEGPacket += PacketEncoder.SetVar('UGID', 'BFHeroesServerPC')
        ClientEGEGPacket += PacketEncoder.SetVar('LID', PacketDecoder.decode(data).GetVar('LID'))
        ClientEGEGPacket += PacketEncoder.SetVar('GID', PacketDecoder.decode(data).GetVar('GID'))
        ClientEGEGPacket = PacketEncoder.encode('EGEG', ClientEGEGPacket, 0x0, 0)
        self.transport.getHandle().sendall(ClientEGEGPacket)