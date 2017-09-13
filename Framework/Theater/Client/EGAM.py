from Utils import PacketEncoder, PacketDecoder
from Framework.Database import GetStat

def ReceiveComponent(self, data):

    try:
        self.ServerGAMEOBJ
    except:
        return ''

    if self.ServerGAMEOBJ != None:
        self.ServerGAMEOBJ.ClientTheaterNetworkInt = self.transport
        EGAMPacket = PacketEncoder.SetVar('LID', PacketDecoder.decode(data).GetVar('LID'))
        EGAMPacket += PacketEncoder.SetVar('GID', PacketDecoder.decode(data).GetVar('GID'))
        EGAMPacket += PacketEncoder.SetVar('TID', self.PacketID, True)
        EGAMPacket = PacketEncoder.encode('EGAM', EGAMPacket, 0x0, 0)

        # This packet gets sent to the SERVER the client connects to, it contains information about the client
        ServerEGRQPacket = PacketEncoder.SetVar('TID', 0)
        ServerEGRQPacket += PacketEncoder.SetVar('NAME', self.GAMEOBJ.Name)
        ServerEGRQPacket += PacketEncoder.SetVar('UID', self.GAMEOBJ.UserID) # this has to be persona_id
        ServerEGRQPacket += PacketEncoder.SetVar('PID', self.GAMEOBJ.UserID)
        ServerEGRQPacket += PacketEncoder.SetVar('TICKET', 2018751182) # TODO: generate this
        ServerEGRQPacket += PacketEncoder.SetVar('IP', self.GAMEOBJ.EXTIP)
        ServerEGRQPacket += PacketEncoder.SetVar('PORT', self.GAMEOBJ.INTPORT)
        ServerEGRQPacket += PacketEncoder.SetVar('INT-IP', PacketDecoder.decode(data).GetVar('R-INT-IP'))
        ServerEGRQPacket += PacketEncoder.SetVar('INT-PORT', PacketDecoder.decode(data).GetVar('R-INT-PORT'))

        ServerEGRQPacket += PacketEncoder.SetVar('PTYPE', PacketDecoder.decode(data).GetVar('PTYPE'))
        ServerEGRQPacket += PacketEncoder.SetVar('R-USER', self.GAMEOBJ.Name)
        ServerEGRQPacket += PacketEncoder.SetVar('R-UID', self.GAMEOBJ.UserID)
        ServerEGRQPacket += PacketEncoder.SetVar('R-U-accid', self.GAMEOBJ.UserID)
        ServerEGRQPacket += PacketEncoder.SetVar('R-U-elo', GetStat(self.GAMEOBJ.UserID, 'elo'))
        ServerEGRQPacket += PacketEncoder.SetVar('R-U-team', GetStat(self.GAMEOBJ.UserID, 'c_team'))
        ServerEGRQPacket += PacketEncoder.SetVar('R-U-kit', GetStat(self.GAMEOBJ.UserID, 'c_kit'))
        ServerEGRQPacket += PacketEncoder.SetVar('R-U-lvl', GetStat(self.GAMEOBJ.UserID, 'level'))
        ServerEGRQPacket += PacketEncoder.SetVar('R-U-dataCenter', self.ServerGAMEOBJ.GetData('B-U-data_center'))
        ServerEGRQPacket += PacketEncoder.SetVar('R-U-externalIp', self.GAMEOBJ.EXTIP)
        ServerEGRQPacket += PacketEncoder.SetVar('R-U-internalIp', PacketDecoder.decode(data).GetVar('R-INT-IP'))
        ServerEGRQPacket += PacketEncoder.SetVar('R-U-category', PacketDecoder.decode(data).GetVar('R-U-category'))
        ServerEGRQPacket += PacketEncoder.SetVar('R-INT-IP', PacketDecoder.decode(data).GetVar('R-INT-IP')) # internal ip where the CLIENT is hosted
        ServerEGRQPacket += PacketEncoder.SetVar('R-INT-PORT', PacketDecoder.decode(data).GetVar('R-INT-PORT'))

        ServerEGRQPacket += PacketEncoder.SetVar('XUID', 24)
        ServerEGRQPacket += PacketEncoder.SetVar('R-XUID', 24)

        ServerEGRQPacket += PacketEncoder.SetVar('LID', PacketDecoder.decode(data).GetVar('LID'))
        ServerEGRQPacket += PacketEncoder.SetVar('GID', PacketDecoder.decode(data).GetVar('GID'), True)

        ServerEGRQPacket = PacketEncoder.encode('EGRQ', ServerEGRQPacket, 0x0, 0)
        print repr(ServerEGRQPacket)

        ClientEGEGPacket = PacketEncoder.SetVar('TID', self.PacketID)
        ClientEGEGPacket += PacketEncoder.SetVar('PL', 'PC')
        ClientEGEGPacket += PacketEncoder.SetVar('TICKET', 2018751182)

        ClientEGEGPacket += PacketEncoder.SetVar('PID', 1)
        ClientEGEGPacket += PacketEncoder.SetVar('I', self.ServerGAMEOBJ.EXTIP)
        ClientEGEGPacket += PacketEncoder.SetVar('P', self.ServerGAMEOBJ.INTPort)
        ClientEGEGPacket += PacketEncoder.SetVar('HUID', 1)
        ClientEGEGPacket += PacketEncoder.SetVar('EKEY', 'O65zZ2D2A58mNrZw1hmuJw%3d%3d')
        ClientEGEGPacket += PacketEncoder.SetVar('INT-IP', self.ServerGAMEOBJ.INTIP)
        ClientEGEGPacket += PacketEncoder.SetVar('INT-PORT', self.ServerGAMEOBJ.INTPort)
        ClientEGEGPacket += PacketEncoder.SetVar('SECRET', 2587913)
        ClientEGEGPacket += PacketEncoder.SetVar('UGID', 'BFHeroesServerPC')
        ClientEGEGPacket += PacketEncoder.SetVar('LID', PacketDecoder.decode(data).GetVar('LID'))
        ClientEGEGPacket += PacketEncoder.SetVar('GID', PacketDecoder.decode(data).GetVar('GID'), True)
        ClientEGEGPacket = PacketEncoder.encode('EGEG', ClientEGEGPacket, 0x0, 0)
        print repr(ClientEGEGPacket)

        self.transport.getHandle().sendall(EGAMPacket)
        self.ServerGAMEOBJ.TheaterNetworkInt.getHandle().sendall(ServerEGRQPacket)
        self.transport.getHandle().sendall(ClientEGEGPacket)