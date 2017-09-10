from Utils import PacketEncoder, PacketDecoder, Globals
import socket, struct

def ReceiveComponent(self, data):
    LoginKey = PacketDecoder.decode(data).GetVar('LKEY')

    ServersCount = len(Globals.Servers)

    # Check if user are already logged in FESL
    loop = 0
    while ServersCount != loop:
        CurrentLoginKey = Globals.Servers[loop].LoginKey
        self.GAMEOBJ = Globals.Servers[loop]
        self.GAMEOBJ.TheaterNetworkInt = self.transport

        if CurrentLoginKey != LoginKey:
            CorrectlyLoggedIn = False
            loop += 1
            continue
        else:
            CorrectlyLoggedIn = True
            self.GAMEOBJ = Globals.Servers[loop]
            break

    if CorrectlyLoggedIn == True:
        self.GAMEOBJ.EXTIP, self.port = self.transport.client
        USERPacket = PacketEncoder.SetVar('TID', self.PacketID)
        USERPacket += PacketEncoder.SetVar('NAME', 'BFHeroesServerPC')
        USERPacket += PacketEncoder.SetVar('CID', '', True)

        USERPacket = PacketEncoder.encode('USER', USERPacket, 0x0, 0)
        self.transport.getHandle().sendall(USERPacket)