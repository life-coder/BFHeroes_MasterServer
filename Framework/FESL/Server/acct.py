from Config import ConsoleColor
from Utils import PacketEncoder, PacketDecoder, DataClass, Globals, RandomStringGenerator
from Framework.Database import CheckServerPassword, GetServerAuthData

def ReceiveComponent(self, data, txn):
    if txn == 'NuLogin':
        try:
            ServerPassword = PacketDecoder.decode(data).GetVar('password')
        except:
            ServerPassword = None

        # Save client connection info
        if self.GAMEOBJ == None:
            self.GAMEOBJ = DataClass.BF2Server()
            self.GAMEOBJ.FESLNetworkInt = self.transport
            Globals.Servers.append(self.GAMEOBJ)

        if ServerPassword == None:
            print ConsoleColor('Warning') + '[FESLServer][acct] Server didnt send password! Disconnecting...' + ConsoleColor('End')
            LoginPacket = PacketEncoder.SetVar('TXN', 'NuLogin')
            LoginPacket += PacketEncoder.SetVar('localizedMessage', '"The password the user specified is incorrect"')
            LoginPacket += PacketEncoder.SetVar('errorContainer.[]', 0)
            LoginPacket += PacketEncoder.SetVar('errorCode', 122, True)
            LoginPacket = PacketEncoder.encode('acct', LoginPacket, 0xC0000000, self.PacketID)
            self.transport.getHandle().sendall(LoginPacket)
            self.transport.loseConnection()

        if CheckServerPassword(ServerPassword) == True:
            print ConsoleColor(
                'Success') + '[FESLServer][acct] Server successfully logged in!' + ConsoleColor('End')
            self.GAMEOBJ.LoginKey = RandomStringGenerator.Generate(24)
            self.GAMEOBJ.UserID = CheckServerPassword(ServerPassword)

            LoginPacket = PacketEncoder.SetVar('TXN', 'NuLogin')
            LoginPacket += PacketEncoder.SetVar('lkey', self.GAMEOBJ.LoginKey)
            LoginPacket += PacketEncoder.SetVar('nuid', GetServerAuthData(self.GAMEOBJ.UserID)[1])
            LoginPacket += PacketEncoder.SetVar('profileId', self.GAMEOBJ.UserID)
            LoginPacket += PacketEncoder.SetVar('userId', self.GAMEOBJ.UserID)
            LoginPacket = PacketEncoder.encode('acct', LoginPacket, 0xC0000000, self.PacketID)
            self.transport.getHandle().sendall(LoginPacket)
        else:
            print ConsoleColor('Warning') + '[FESLServer][acct] Server specified wrong password! Disconnecting...' + ConsoleColor('End')
            LoginPacket = PacketEncoder.SetVar('TXN', 'NuLogin')
            LoginPacket += PacketEncoder.SetVar('localizedMessage', '"The password the user specified is incorrect"')
            LoginPacket += PacketEncoder.SetVar('errorContainer.[]', 0)
            LoginPacket += PacketEncoder.SetVar('errorCode', 122, True)
            LoginPacket = PacketEncoder.encode('acct', LoginPacket, 0xC0000000, self.PacketID)
            self.transport.getHandle().sendall(LoginPacket)
            self.transport.loseConnection()

    elif txn == 'NuGetPersonas':
        PersonaPacket = PacketEncoder.SetVar('TXN', 'NuGetPersonas')
        PersonaPacket += PacketEncoder.SetVar('personas.[]', 0)
        PersonaPacket = PacketEncoder.encode('acct', PersonaPacket, 0xC0000000, self.PacketID)
        self.transport.getHandle().sendall(PersonaPacket)

    elif txn == 'NuGetAccount':
        AccountPacket = PacketEncoder.SetVar('TXN', 'NuGetAccount')
        AccountPacket += PacketEncoder.SetVar('heroName', GetServerAuthData(self.GAMEOBJ.UserID)[1])
        AccountPacket += PacketEncoder.SetVar('nuid', GetServerAuthData(self.GAMEOBJ.UserID)[1])
        AccountPacket += PacketEncoder.SetVar('DOBDay', 01)
        AccountPacket += PacketEncoder.SetVar('DOBMonth', 01)
        AccountPacket += PacketEncoder.SetVar('DOBYear', 1970)
        AccountPacket += PacketEncoder.SetVar('userId', self.GAMEOBJ.UserID)
        AccountPacket += PacketEncoder.SetVar('globalOptin', 0)
        AccountPacket += PacketEncoder.SetVar('thidPartyOptin', 0)
        AccountPacket += PacketEncoder.SetVar('language', 'enUS')
        AccountPacket += PacketEncoder.SetVar('country', 'US')
        AccountPacket = PacketEncoder.encode('acct', AccountPacket, 0xC0000000, self.PacketID)
        self.transport.getHandle().sendall(AccountPacket)

    elif txn == 'NuLoginPersona':
        LoginPacket = PacketEncoder.SetVar('TXN', 'NuLoginPersona')
        LoginPacket += PacketEncoder.SetVar('lkey', self.GAMEOBJ.LoginKey)
        LoginPacket += PacketEncoder.SetVar('profileId', self.GAMEOBJ.UserID)
        LoginPacket += PacketEncoder.SetVar('userId', self.GAMEOBJ.UserID)
        LoginPacket = PacketEncoder.encode('acct', LoginPacket, 0xC0000000, self.PacketID)
        self.transport.getHandle().sendall(LoginPacket)

    elif txn == 'NuLookupUserInfo':
        LookupPacket = PacketEncoder.SetVar('TXN', 'NuLookupUserInfo')
        LookupPacket += PacketEncoder.SetVar('userInfo.0.userName', GetServerAuthData(self.GAMEOBJ.UserID)[1])
        LookupPacket += PacketEncoder.SetVar('userInfo.0.userId', self.GAMEOBJ.UserID)
        LookupPacket += PacketEncoder.SetVar('userInfo.0.masterUserId', self.GAMEOBJ.UserID)
        LookupPacket += PacketEncoder.SetVar('userInfo.0.namespace', 'MAIN')
        LookupPacket += PacketEncoder.SetVar('userInfo.0.xuid', 24)
        LookupPacket += PacketEncoder.SetVar('userInfo.0.cid', self.GAMEOBJ.UserID)
        LookupPacket += PacketEncoder.SetVar('userInfo.[]', 1)
        LookupPacket = PacketEncoder.encode('acct', LookupPacket, 0xC0000000, self.PacketID)
        self.transport.getHandle().sendall(LookupPacket)
    else:
        print ConsoleColor('Warning') + '[FESLServer][acct] Got unknown TXN (' + txn + ')' + ConsoleColor('End')