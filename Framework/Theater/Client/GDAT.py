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

        # Basic stuff
        GDATPacket += PacketEncoder.SetVar('IP', self.ServerGAMEOBJ.EXTIP)
        GDATPacket += PacketEncoder.SetVar('PORT', self.ServerGAMEOBJ.GetData('PORT'))
        GDATPacket += PacketEncoder.SetVar('INT-IP', self.ServerGAMEOBJ.GetData('INT-IP'))
        GDATPacket += PacketEncoder.SetVar('INT-PORT', self.ServerGAMEOBJ.GetData('INT-PORT'))
        GDATPacket += PacketEncoder.SetVar('LID', self.ServerGAMEOBJ.GetData('LID')) # LobbyID
        GDATPacket += PacketEncoder.SetVar('GID', self.ServerGAMEOBJ.GetData('GID')) # GameID
        GDATPacket += PacketEncoder.SetVar('UGID', self.ServerGAMEOBJ.GetData('UGID'))
        GDATPacket += PacketEncoder.SetVar('MAX-PLAYERS', self.ServerGAMEOBJ.GetData('MAX-PLAYERS'))
        GDATPacket += PacketEncoder.SetVar('AP', 0) # Active Players. #TODO: Count it
        GDATPacket += PacketEncoder.SetVar('NAME', self.ServerGAMEOBJ.GetData('NAME').replace('"', '')) # Server Name
        GDATPacket += PacketEncoder.SetVar('SECRET', self.ServerGAMEOBJ.GetData('SECRET'))
        GDATPacket += PacketEncoder.SetVar('QLEN', self.ServerGAMEOBJ.GetData('QLEN')) # Queue Length
        GDATPacket += PacketEncoder.SetVar('QUEUE-LENGTH', 0) # TODO: Check diffirence between that and QLEN
        GDATPacket += PacketEncoder.SetVar('DISABLE-AUTO-DEQUEUE', self.ServerGAMEOBJ.GetData('DISABLE-AUTO-DEQUEUE'))

        # Server info
        GDATPacket += PacketEncoder.SetVar('B-maxObservers', self.ServerGAMEOBJ.GetData('B-maxObservers'))
        GDATPacket += PacketEncoder.SetVar('B-numObservers', self.ServerGAMEOBJ.GetData('B-numObservers'))
        GDATPacket += PacketEncoder.SetVar('B-version', self.ServerGAMEOBJ.GetData('B-version'))

        GDATPacket += PacketEncoder.SetVar('B-U-alwaysQueue', self.ServerGAMEOBJ.GetData('B-U-alwaysQueue'))
        GDATPacket += PacketEncoder.SetVar('B-U-army_balance', self.ServerGAMEOBJ.GetData('B-U-army_balance'))
        GDATPacket += PacketEncoder.SetVar('B-U-army_distribution', self.ServerGAMEOBJ.GetData('B-U-army_distribution').replace('"', ''))
        GDATPacket += PacketEncoder.SetVar('B-U-avail_slots_national', self.ServerGAMEOBJ.GetData('B-U-avail_slots_national'))
        GDATPacket += PacketEncoder.SetVar('B-U-avail_slots_royal', self.ServerGAMEOBJ.GetData('B-U-avail_slots_royal'))
        GDATPacket += PacketEncoder.SetVar('B-U-avail_vips_national', self.ServerGAMEOBJ.GetData('B-U-avail_vips_national'))
        GDATPacket += PacketEncoder.SetVar('B-U-avail_vips_royal', self.ServerGAMEOBJ.GetData('B-U-avail_vips_royal'))
        GDATPacket += PacketEncoder.SetVar('B-U-avg_ally_rank', self.ServerGAMEOBJ.GetData('B-U-avg_ally_rank'))
        GDATPacket += PacketEncoder.SetVar('B-U-avg_axis_rank', self.ServerGAMEOBJ.GetData('B-U-avg_axis_rank'))
        GDATPacket += PacketEncoder.SetVar('B-U-community_name', self.ServerGAMEOBJ.GetData('B-U-community_name'))
        GDATPacket += PacketEncoder.SetVar('B-U-data_center', self.ServerGAMEOBJ.GetData('B-U-data_center'))
        GDATPacket += PacketEncoder.SetVar('B-U-elo_rank', self.ServerGAMEOBJ.GetData('B-U-elo_rank'))
        GDATPacket += PacketEncoder.SetVar('B-U-easyzone', self.ServerGAMEOBJ.GetData('B-U-easyzone'))
        GDATPacket += PacketEncoder.SetVar('B-U-lvl_sdv', self.ServerGAMEOBJ.GetData('B-U-lvl_sdv'))
        GDATPacket += PacketEncoder.SetVar('B-U-lvl_avg', self.ServerGAMEOBJ.GetData('B-U-lvl_avg'))
        GDATPacket += PacketEncoder.SetVar('B-U-map', self.ServerGAMEOBJ.GetData('B-U-map'))
        GDATPacket += PacketEncoder.SetVar('B-U-map_name', self.ServerGAMEOBJ.GetData('B-U-map_name'))
        GDATPacket += PacketEncoder.SetVar('B-U-punkb', self.ServerGAMEOBJ.GetData('B-U-punkb'))
        GDATPacket += PacketEncoder.SetVar('B-U-percent_full', self.ServerGAMEOBJ.GetData('B-U-percent_full'))
        GDATPacket += PacketEncoder.SetVar('B-U-ranked', self.ServerGAMEOBJ.GetData('B-U-ranked'))
        GDATPacket += PacketEncoder.SetVar('B-U-server_ip', self.ServerGAMEOBJ.GetData('B-U-server_ip'))
        GDATPacket += PacketEncoder.SetVar('B-U-server_state', self.ServerGAMEOBJ.GetData('B-U-server_state'))
        GDATPacket += PacketEncoder.SetVar('B-U-server_port', self.ServerGAMEOBJ.GetData('B-U-server_port'))
        GDATPacket += PacketEncoder.SetVar('B-U-servertype', self.ServerGAMEOBJ.GetData('B-U-servertype'))

        # Unknown data
        GDATPacket += PacketEncoder.SetVar('HXFR', self.ServerGAMEOBJ.GetData('HXFR'))
        GDATPacket += PacketEncoder.SetVar('HTTYPE', self.ServerGAMEOBJ.GetData('HTTYPE'))
        GDATPacket += PacketEncoder.SetVar('JOIN', self.ServerGAMEOBJ.GetData('JOIN'))
        GDATPacket += PacketEncoder.SetVar('RESERVE-HOST', self.ServerGAMEOBJ.GetData('RESERVE-HOST'))
        GDATPacket += PacketEncoder.SetVar('RT', self.ServerGAMEOBJ.GetData('RT'))
        GDATPacket += PacketEncoder.SetVar('TYPE', self.ServerGAMEOBJ.GetData('TYPE'), True)

        GDATPacket = PacketEncoder.encode('GDAT', GDATPacket, 0x0, 0)
        self.transport.getHandle().sendall(GDATPacket)

        print ConsoleColor('Success') + '[TheaterClient][GDAT] Client joining to game... (' + str(RequestedGID) + ')' + ConsoleColor('End')
    else:
        self.ServerGAMEOBJ = None
        print ConsoleColor('Error') + '[TheaterClient][GDAT] Cannot find requested game!' + ConsoleColor('End')