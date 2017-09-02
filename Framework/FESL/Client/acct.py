from Config import ConsoleColor
from Utils import PacketEncoder, PacketDecoder, DataClass, Globals, RandomStringGenerator
from Framework.Database import GetWebSession, GetUserName, GetEmail, GetAccountID

def ReceiveComponent(self, data, txn):
    if txn == 'NuLogin':
        SessionID = PacketDecoder.decode(data).GetVar('encryptedInfo')

        # Basic login data retrieve system, (Get AccountID, username and email from Database), if that data are missing return error to game
        try:
            AccountID = str(GetWebSession(SessionID)[0])
            Username = GetUserName(AccountID)
            email = GetEmail(AccountID)
        except:
            AccountID = None
            Username = None
            email = None
        # Save client connection info
        if self.GAMEOBJ == None:
            self.GAMEOBJ = DataClass.BF2Client()
            self.GAMEOBJ.FESLNetworkInt = self.transport
            Globals.Clients.append(self.GAMEOBJ)

        self.GAMEOBJ.IsOnline = True

        self.GAMEOBJ.SessionID = SessionID
        self.GAMEOBJ.UserID = AccountID
        self.GAMEOBJ.EMail = email


        if AccountID == None or Username == None or email == None:
            print ConsoleColor('Warning') + '[FESLClient][acct] User tryed to login using dead or incorrect SessionID! Ignoring...' + ConsoleColor('End')
            LoginPacket = PacketEncoder.SetVar('TXN', 'NuLogin')
            LoginPacket += PacketEncoder.SetVar('localizedMessage', '"The user is not entitled to access this game"')
            LoginPacket += PacketEncoder.SetVar('errorContainer.[]', 0)
            LoginPacket += PacketEncoder.SetVar('errorCode', 120, True)
            LoginPacket = PacketEncoder.encode('acct', LoginPacket, 0xC0000000, self.PacketID)
            self.transport.getHandle().sendall(LoginPacket)
            self.transport.loseConnection()

        else:
            print ConsoleColor(
                'Success') + '[FESLClient][acct] User ' + Username + ' Successfully logged in!' + ConsoleColor(
                'End')
            self.GAMEOBJ.LoginKey = RandomStringGenerator.Generate(24)

            LoginPacket = PacketEncoder.SetVar('TXN', 'NuLogin')
            LoginPacket += PacketEncoder.SetVar('profileId', AccountID)
            LoginPacket += PacketEncoder.SetVar('userId', AccountID)
            LoginPacket += PacketEncoder.SetVar('nuid', Username)
            LoginPacket += PacketEncoder.SetVar('lkey', self.GAMEOBJ.LoginKey, True)
            LoginPacket = PacketEncoder.encode('acct', LoginPacket, 0xC0000000, self.PacketID)
            self.transport.getHandle().sendall(LoginPacket)

    elif txn == 'NuGetPersonas':
        # Get User Soldiers

        GetPersonasPacket = PacketEncoder.SetVar('TXN', 'NuGetPersonas')

        # For now I'm using static variables.
        GetPersonasPacket += PacketEncoder.SetVar('personas.0', 'TestSoldier1')
        GetPersonasPacket += PacketEncoder.SetVar('personas.1', 'TestSoldier2')
        GetPersonasPacket += PacketEncoder.SetVar('personas.2', 'TestSoldier3')
        GetPersonasPacket += PacketEncoder.SetVar('personas.3', 'TestSoldier4')
        GetPersonasPacket += PacketEncoder.SetVar('personas.4', 'TestSoldier5')
        GetPersonasPacket += PacketEncoder.SetVar('personas.5', 'TestSoldier6')
        GetPersonasPacket += PacketEncoder.SetVar('personas.[]', 6, True)
        GetPersonasPacket = PacketEncoder.encode('acct', GetPersonasPacket, 0xC0000000, self.PacketID)
        self.transport.getHandle().sendall(GetPersonasPacket)

    elif txn == 'NuGetAccount':
        # Get Account data

        GetAccountPacket = PacketEncoder.SetVar('TXN', 'NuGetAccount')

        # For now I'm using static variables.
        GetAccountPacket += PacketEncoder.SetVar('heroName', 'TestAccount')
        GetAccountPacket += PacketEncoder.SetVar('nuid', self.GAMEOBJ.EMail)

        # Birthday date
        GetAccountPacket += PacketEncoder.SetVar('DOBDay', '1')
        GetAccountPacket += PacketEncoder.SetVar('DOBMonth', '1')
        GetAccountPacket += PacketEncoder.SetVar('DOBYear', '2017')

        GetAccountPacket += PacketEncoder.SetVar('userId', self.GAMEOBJ.UserID)

        # Not sure what is this
        GetAccountPacket += PacketEncoder.SetVar('globalOptin', 0)
        GetAccountPacket += PacketEncoder.SetVar('thidPartyOptin', 0)

        # Other required data
        GetAccountPacket += PacketEncoder.SetVar('language', 'enUS')
        GetAccountPacket += PacketEncoder.SetVar('country', 'US', True)
        GetAccountPacket = PacketEncoder.encode('acct', GetAccountPacket, 0xC0000000, self.PacketID)
        self.transport.getHandle().sendall(GetAccountPacket)

    elif txn == 'NuLookupUserInfo':
        # Load Soldiers info
        RequestedPersonas = int(PacketDecoder.decode(data).GetVar('userInfo.[]'))
        loop = 0

        LookupUserInfoPacket = PacketEncoder.SetVar('TXN', 'NuLookupUserInfo')

        while loop != RequestedPersonas:
            LookupUserInfoPacket += PacketEncoder.SetVar('userInfo.' + str(loop) + '.userName', 'TestSoldier' + str(loop + 1))
            LookupUserInfoPacket += PacketEncoder.SetVar('userInfo.' + str(loop) + '.userId', loop + 1)
            LookupUserInfoPacket += PacketEncoder.SetVar('userInfo.' + str(loop) + '.masterUserId', loop + 1)
            LookupUserInfoPacket += PacketEncoder.SetVar('userInfo.' + str(loop) + '.namespace', 'MAIN')
            LookupUserInfoPacket += PacketEncoder.SetVar('userInfo.' + str(loop) + '.xuid', 24)
            loop += 1

        LookupUserInfoPacket += PacketEncoder.SetVar('userInfo.[]', RequestedPersonas, True)

        LookupUserInfoPacket = PacketEncoder.encode('acct', LookupUserInfoPacket, 0xC0000000, self.PacketID)
        self.transport.getHandle().sendall(LookupUserInfoPacket)

    elif txn == 'NuLoginPersona':
        # For now - Always login
        self.GAMEOBJ.LoginKey = RandomStringGenerator.Generate(24)
        LoginPersonaPacket = PacketEncoder.SetVar('TXN', 'NuLoginPersona')
        LoginPersonaPacket += PacketEncoder.SetVar('lkey', self.GAMEOBJ.LoginKey)
        LoginPersonaPacket += PacketEncoder.SetVar('profileId', self.GAMEOBJ.UserID)
        LoginPersonaPacket += PacketEncoder.SetVar('userId', self.GAMEOBJ.UserID)

        LoginPersonaPacket = PacketEncoder.encode('acct', LoginPersonaPacket, 0xC0000000, self.PacketID)
        self.transport.getHandle().sendall(LoginPersonaPacket)
    else:
        print ConsoleColor('Warning') + '[FESLClient][acct] Got unknown TXN (' + txn + ')' + ConsoleColor('End')
