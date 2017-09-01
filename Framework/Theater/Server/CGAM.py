from Utils import PacketDecoder, PacketEncoder, Globals, RandomStringGenerator
from Config import ConsoleColor
def ReceiveComponent(self, data):
    # Create game

    # Get all game data
    NewData = data.replace('UGAM', '')[12:]
    NewData = NewData.replace('\x00', '').split('\n')
    NewValues = len(NewData) - 1

    loop = 0

    while loop != NewValues:
        self.GAMEOBJ.AttrNames.append(NewData[loop].split('=')[0])
        self.GAMEOBJ.AttrData.append(NewData[loop].split('=')[1])
        loop += 1

    CGAMPacket = PacketEncoder.SetVar('TID', self.PacketID)
    CGAMPacket += PacketEncoder.SetVar('LID', '1')
    CGAMPacket += PacketEncoder.SetVar('UGID', PacketDecoder.decode(data).GetVar('UGID'))
    CGAMPacket += PacketEncoder.SetVar('MAX-PLAYERS', PacketDecoder.decode(data).GetVar('MAX-PLAYERS'))
    CGAMPacket += PacketEncoder.SetVar('EKEY', RandomStringGenerator.Generate(22) + '%3d%3d')
    CGAMPacket += PacketEncoder.SetVar('UGID', PacketDecoder.decode(data).GetVar('UGID'))
    CGAMPacket += PacketEncoder.SetVar('SECRET', RandomStringGenerator.Generate(7))
    CGAMPacket += PacketEncoder.SetVar('JOIN', PacketDecoder.decode(data).GetVar('JOIN'))
    CGAMPacket += PacketEncoder.SetVar('J', PacketDecoder.decode(data).GetVar('JOIN'))
    CGAMPacket += PacketEncoder.SetVar('GID', Globals.CurrentGameID)
    Globals.CurrentGameID += 1
    CGAMPacket = PacketEncoder.encode('CGAM', CGAMPacket, 0x0, 0)
    self.transport.getHandle().sendall(CGAMPacket)

    print ConsoleColor('Success') + '[TheaterServer][CGAM] Successfully created new game!' + ConsoleColor('End')