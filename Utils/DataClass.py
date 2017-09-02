class BF2Client:
    Type = 'Client'
    UserID = 0
    PersonaID = 0
    Name = ''
    SessionID = ''
    EMail = ''
    LoginKey = ''
    FESLNetworkInt = None
    TheaterNetworkInt = None
    EXTIP = ''
    EXTPort = 0
    IsOnline = False

class BF2Server:
    Type = 'Server'
    UserID = 0
    LoginKey = ''
    FESLNetworkInt = None
    TheaterNetworkInt = None
    IsOnline = False
    EXTIP = ''
    EXTPort = 0

    ClientTheaterNetworkInt = None
    # Server Data
    GameID = 0
    AttrNames = []
    AttrData = []

    def GetData(self, RequestedData):
        try:
            index = self.AttrNames.index(RequestedData)
            value = self.AttrData[index]
            return value
        except:
            return ''