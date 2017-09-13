from Utils import PacketEncoder, PacketDecoder, Globals
import socket, struct

def ReceiveComponent(self, data):
    LoginKey = PacketDecoder.decode(data).GetVar('LKEY')

    ClientsCount = len(Globals.Clients)

    # Check if user are already logged in FESL
    loop = 0
    while ClientsCount != loop:
        CurrentLoginKey = Globals.Clients[loop].LoginKey
        self.GAMEOBJ = Globals.Clients[loop]
        self.GAMEOBJ.TheaterNetworkInt = self.transport

        if CurrentLoginKey != LoginKey:
            CorrectlyLoggedIn = False
            loop += 1
            continue
        else:
            CorrectlyLoggedIn = True
            self.GAMEOBJ = Globals.Clients[loop]
            break

    if CorrectlyLoggedIn == True:
        self.GAMEOBJ.EXTIP, self.GAMEOBJ.INTPORT = self.transport.client
        USERPacket = PacketEncoder.SetVar('TID', self.PacketID)
        USERPacket += PacketEncoder.SetVar('NAME', self.GAMEOBJ.Name)
        USERPacket += PacketEncoder.SetVar('CID', '', True)

        USERPacket = PacketEncoder.encode('USER', USERPacket, 0x0, 0)
        self.transport.getHandle().sendall(USERPacket)