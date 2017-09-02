from Utils import PacketEncoder, PacketDecoder, Globals
from Config import ConsoleColor

def ReceiveComponent(self, data):
    RequestedGID = PacketDecoder.decode(data).GetVar('GID')

    loop = 0
    ServersOnline = len(Globals.Servers)

    while loop != ServersOnline:

        if Globals.Servers[loop].GameID == int(RequestedGID):
            completed = True
            break
        else:
            completed = False
            loop += 1
            continue

    if completed == True:
        self.ServerGAMEOBJ = Globals.Servers[loop]


        GDATPacket = PacketEncoder.SetVar('TID', self.PacketID)

        Keys = len(self.ServerGAMEOBJ.AttrNames)

        loop = 0
        while loop != Keys:
            GDATPacket += PacketEncoder.SetVar(self.ServerGAMEOBJ.AttrNames[loop], self.ServerGAMEOBJ.AttrData[loop])
            loop += 1

        GDATPacket = PacketEncoder.encode('GDAT', GDATPacket, 0x0, 0)
        self.transport.getHandle().sendall(GDATPacket)
        print ConsoleColor('Success') + '[TheaterClient][GDAT] Client joining to game... (' + str(RequestedGID) + ')' + ConsoleColor('End')
    else:
        self.ServerGAMEOBJ = None
        print ConsoleColor('Error') + '[TheaterClient][GDAT] Cannot find requested game!' + ConsoleColor('End')