from Config import ConsoleColor
from Utils import PacketEncoder, PacketDecoder, DataClass, Globals, RandomStringGenerator
from Framework.Database import GetWebSession, GetUserName, GetEmail

def ReceiveComponent(self, data, txn):
    if txn == 'GetStats':
        # Get Account Stats (info)

        OwnerID = PacketDecoder.decode(data).GetVar('owner')
        OwnerType = PacketDecoder.decode(data).GetVar('ownerType')

        GetStatsPacket = PacketEncoder.SetVar('TXN', 'GetStats')
        GetStatsPacket += PacketEncoder.SetVar('ownerId', OwnerID)
        GetStatsPacket += PacketEncoder.SetVar('ownerType', OwnerType)

        RequestedKeysNumber = int(PacketDecoder.decode(data).GetVar('keys.[]'))

        # Get all requested keys names

        loop = 0
        RequestedKeysNames = []

        while loop != RequestedKeysNumber:
            RequestedKeyName = PacketDecoder.decode(data).GetVar('keys.' + str(loop))
            RequestedKeysNames.append(RequestedKeyName)
            loop += 1

        loop = 0

        # Get and return requested keys values

        while loop != RequestedKeysNumber:
            # For now everything is static
            GetStatsPacket += PacketEncoder.SetVar('stats.' + str(loop) + '.key', RequestedKeysNames[loop])
            GetStatsPacket += PacketEncoder.SetVar('stats.' + str(loop) + '.value', 0)
            GetStatsPacket += PacketEncoder.SetVar('stats.' + str(loop) + '.text', '')
            loop += 1

        GetStatsPacket += PacketEncoder.SetVar('stats.[]', RequestedKeysNumber)

        GetStatsPacket = PacketEncoder.encode('acct', GetStatsPacket, 0xC0000000, self.PacketID)
        self.transport.getHandle().sendall(GetStatsPacket)

    elif txn == 'GetStatsForOwners':
        # Get Soldier Stats
        # Requested soldiers
        Owners = int(PacketDecoder.decode(data).GetVar('owners.[]'))

        OwnerIDs = []
        OwnerTypes = []

        loop = 0

        while loop != Owners:
            OwnerID = PacketDecoder.decode(data).GetVar('owners.' + str(loop) + '.ownerId')
            OwnerType = PacketDecoder.decode(data).GetVar('owners.' + str(loop) + '.ownerType')

            OwnerIDs.append(OwnerID)
            OwnerTypes.append(OwnerType)

            loop += 1

        GetStatsForOwnersPacket = PacketEncoder.SetVar('TXN', 'GetStats')

        # Get all requested keys names
        RequestedKeysNumber = int(PacketDecoder.decode(data).GetVar('keys.[]'))
        loop = 0
        RequestedKeysNames = []

        while loop != RequestedKeysNumber:
            RequestedKeyName = PacketDecoder.decode(data).GetVar('keys.' + str(loop))
            RequestedKeysNames.append(RequestedKeyName)
            loop += 1

        loop = 0

        while loop != Owners:
            GetStatsForOwnersPacket += PacketEncoder.SetVar('stats.' + str(loop) + '.ownerId', OwnerIDs[loop])
            GetStatsForOwnersPacket += PacketEncoder.SetVar('stats.' + str(loop) + '.ownerType', OwnerTypes[loop])

            key = 0
            while key != RequestedKeysNumber:
                GetStatsForOwnersPacket += PacketEncoder.SetVar('stats.' + str(loop) + '.stats.' + str(key) + '.key', RequestedKeysNames[key])
                GetStatsForOwnersPacket += PacketEncoder.SetVar('stats.' + str(loop) + '.stats.' + str(key) + '.value', 1)
                GetStatsForOwnersPacket += PacketEncoder.SetVar('stats.' + str(loop) + '.stats.' + str(key) + '.text', '')
                key += 1

            GetStatsForOwnersPacket += PacketEncoder.SetVar('stats.' + str(loop) + '.stats.[]', RequestedKeysNumber)

            loop += 1

        GetStatsForOwnersPacket += PacketEncoder.SetVar('stats.[]', Owners)

        GetStatsForOwnersPacket = PacketEncoder.encode('acct', GetStatsForOwnersPacket, 0xC0000000, self.PacketID)
        self.transport.getHandle().sendall(GetStatsForOwnersPacket)

    elif txn == 'UpdateStats':
        # Doesn't update any Stats
        UpdateStatsPacket = PacketEncoder.encode('rank', PacketEncoder.SetVar('TXN', 'UpdateStats'), 0xC0000000, self.PacketID)
        self.transport.getHandle().sendall(UpdateStatsPacket)
    else:
        print ConsoleColor('Warning') + '[FESLClient][rank] Got unknown TXN (' + txn + ')' + ConsoleColor('End')
