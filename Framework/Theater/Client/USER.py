from Utils import PacketEncoder, PacketDecoder, Globals

def ReceiveComponent(self, data):
    LoginKey = PacketDecoder.decode(data).GetVar('LKEY')

    ClientsCount = len(Globals.Clients)

    # Check if user are already logged in FESL
    loop = 0
    while ClientsCount != loop:
        CurrentLoginKey = Globals.Clients[loop].LoginKey

        if CurrentLoginKey != LoginKey:
            CorrectlyLoggedIn = False
            loop += 1
            continue
        else:
            CorrectlyLoggedIn = True
            self.GAMEOBJ = Globals.Clients[loop]
            break

    self.GAMEOBJ.Name = 'TestSoldier1'
    if CorrectlyLoggedIn == True:
        USERPacket = PacketEncoder.SetVar('TID', self.PacketID)
        USERPacket += PacketEncoder.SetVar('NAME', self.GAMEOBJ.Name)
        USERPacket += PacketEncoder.SetVar('CID', '\n', True)

        USERPacket = PacketEncoder.encode('USER', USERPacket, 0x0, 0)
        print repr(USERPacket)
        self.transport.getHandle().sendall(USERPacket)