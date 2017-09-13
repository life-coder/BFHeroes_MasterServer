ServerIP = '127.0.0.1'
DatabaseFileLocation = 'Data/Database.db'

WebServerPort = 80
SecureWebServerPort = 443
FESLClientPort = 18270
FESLServerPort = 18051
TheaterClientPort = 18275
TheaterServerPort = 18056

def ConsoleColor(RequestedColor):
    if RequestedColor == 'End':
        return '\33[0m'
    elif RequestedColor == 'Info':
        return '\33[1m'
    elif RequestedColor == 'Error':
        return '\33[31m'
    elif RequestedColor == 'Success':
        return '\33[32m'
    elif RequestedColor == 'Warning':
        return '\33[33m'
    else:
        return None