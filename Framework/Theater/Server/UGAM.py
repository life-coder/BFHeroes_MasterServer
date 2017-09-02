from Config import ConsoleColor
from Utils import PacketEncoder

def ReceiveComponent(self, data):
    # Update server info

    if data.find('UBRA@') != -1:
        data = data.split('UBRA@')[0]
        UBRAPacket = PacketEncoder.SetVar('TID', self.PacketID)
        UBRAPacket = PacketEncoder.encode('UBRA', UBRAPacket, 0x0, 0)
        self.transport.getHandle().sendall(UBRAPacket)

    NewData = data.replace('UGAM', '')[8:]
    NewData = NewData.replace('\x00', '').split('\n')

    NewValues = len(NewData) - 1

    loop = 0
    NewKeysNames = []
    NewKeysValues = []
    while loop != NewValues:
        NewKeysNames.append(NewData[loop].split('=')[0])
        NewKeysValues.append(NewData[loop].split('=')[1])
        loop += 1

    loop = 0

    while loop != len(NewKeysNames):
        if NewKeysNames[loop] in self.GAMEOBJ.AttrNames:
            AttrId = self.GAMEOBJ.AttrNames.index(NewKeysNames[loop])
            self.GAMEOBJ.AttrData[AttrId] = NewKeysValues[loop]
        else:
            self.GAMEOBJ.AttrNames.append(NewKeysNames[loop])
            self.GAMEOBJ.AttrData.append(NewKeysValues[loop])
        loop += 1

    print ConsoleColor('Success') + '[TheaterServer][UGAM] Successfully updated game info!' + ConsoleColor('End')