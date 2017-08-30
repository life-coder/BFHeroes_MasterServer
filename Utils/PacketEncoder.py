from Utils.PacketChecksum import CreateChecksum

def SetVar(var, value, isLast=False):
    AddedValue = var + '=' + str(value)
    if isLast == True:
        AddedValue += '\x00'
    else:
        AddedValue += '\n'
    return AddedValue

def encode(command, data, value, PacketID):
    value = value + PacketID

    Checksum = CreateChecksum(data, value)
    return command + Checksum + data
