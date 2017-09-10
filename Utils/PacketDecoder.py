class decode():
    def __init__(self, packet):
        self.Packet = packet

    def GetCommand(self):
        return self.Packet[:4]

    def GetTXN(self):
        return self.Packet.split('TXN=')[1].split('\n')[0]

    def GetVar(self, var):
        return self.Packet.split(var + '=')[1].split('\n')[0]
