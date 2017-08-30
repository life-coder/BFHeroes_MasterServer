#! python2.7
import sys

from Config import *
from Network import FESLClient, FESLServer, TheaterClient, TheaterServer, WebServer, GameWebServer, SecureWebServer
from Framework import Database
from Utils import Globals

try:
    from twisted.internet import ssl, reactor
    from twisted.internet.protocol import Factory, Protocol
    from twisted.web import server, resource
except ImportError, Error:
    print ConsoleColor('Error') + 'Fatal Error! Cannot import Twisted modules!'
    print 'Make sure you installed latest Twisted from pip!'
    print '\n'
    print 'Additional error info:'
    print Error, ConsoleColor('End')
    sys.exit(1)

try:
    Database.Prepare()
except Exception, DatabaseError:
    print ConsoleColor('Error') + 'Fatal Error! Cannot create database file!'
    print 'Make sure you have writing and reading permissions in "' + DatabaseFileLocation + '"'
    print '\n'
    print 'Additional error info:'
    print DatabaseError, ConsoleColor('End')
    sys.exit(1)

def Start():

    Globals.ServerIP = ServerIP

    try:
        SSLContext = ssl.DefaultOpenSSLContextFactory('Certificates/BFHeroes.key', 'Certificates/BFHeroes.crt')
    except Exception, OpenSSLError:
        print ConsoleColor('Error') + 'Fatal Error in OpenSSL!'
        print '\n'
        print 'Additional error info:'
        print OpenSSLError, ConsoleColor('End')
        sys.exit(1)

    try:
        factory = Factory()
        factory.protocol = FESLClient.HANDLER
        reactor.listenSSL(FESLClientPort, factory, SSLContext)
        print ConsoleColor('Success') + '[FESLClient] Started listening at port: ' + str(FESLClientPort)
    except Exception, BindError:
        print ConsoleColor('Error') + 'Fatal Error! Cannot bind socket to port: ' + str(FESLClientPort)
        print 'Make sure that other programs are not currently listening to this port!'
        print '\n'
        print 'Additional error info:'
        print BindError, ConsoleColor('End')
        sys.exit(1)

    try:
        factory = Factory()
        factory.protocol = FESLServer.HANDLER
        reactor.listenTCP(FESLServerPort, factory)
        print ConsoleColor('Success') + '[FESLServer] Started listening at port: ' + str(FESLServerPort)
    except Exception, BindError:
        print ConsoleColor('Error') + 'Fatal Error! Cannot bind socket to port: ' + str(FESLServerPort)
        print 'Make sure that other programs are not currently listening to this port!'
        print '\n'
        print 'Additional error info:'
        print BindError, ConsoleColor('End')
        sys.exit(1)

    try:
        factory = Factory()
        factory.protocol = TheaterClient.HANDLER
        reactor.listenTCP(TheaterClientPort, factory)
        print ConsoleColor('Success') + '[TheaterClient] Started listening at port: ' + str(TheaterClientPort)
    except Exception, BindError:
        print ConsoleColor('Error') + 'Fatal Error! Cannot bind socket to port: ' + str(TheaterClientPort)
        print 'Make sure that other programs are not currently listening to this port!'
        print '\n'
        print 'Additional error info:'
        print BindError, ConsoleColor('End')
        sys.exit(1)

    try:
        factory = Factory()
        factory.protocol = TheaterServer.HANDLER
        reactor.listenTCP(TheaterServerPort, factory)
        print ConsoleColor('Success') + '[TheaterServer] Started listening at port: ' + str(TheaterServerPort)
    except Exception, BindError:
        print ConsoleColor('Error') + 'Fatal Error! Cannot bind socket to port: ' + str(TheaterServerPort)
        print 'Make sure that other programs are not currently listening to this port!'
        print '\n'
        print 'Additional error info:'
        print BindError, ConsoleColor('End')
        sys.exit(1)

    try:
        site = server.Site(WebServer.Simple())
        reactor.listenTCP(WebServerPort, site)
        print ConsoleColor('Success') + '[WebServer] Started listening at port: ' + str(WebServerPort)
    except Exception, BindError:
        print ConsoleColor('Error') + 'Fatal Error! Cannot bind socket to port: ' + str(WebServerPort)
        print 'Make sure that other programs are not currently listening to this port!'
        print '\n'
        print 'Additional error info:'
        print BindError, ConsoleColor('End')
        sys.exit(1)

    try:
        site = server.Site(GameWebServer.Simple())
        reactor.listenTCP(GameWebServerPort, site)
        print ConsoleColor('Success') + '[GameWebServer] Started listening at port: ' + str(GameWebServerPort)
    except Exception, BindError:
        print ConsoleColor('Error') + 'Fatal Error! Cannot bind socket to port: ' + str(GameWebServerPort)
        print 'Make sure that other programs are not currently listening to this port!'
        print '\n'
        print 'Additional error info:'
        print BindError, ConsoleColor('End')
        sys.exit(1)

    try:
        site = server.Site(SecureWebServer.Simple())
        reactor.listenSSL(SecureWebServerPort, site, SSLContext)
        print ConsoleColor('Success') + '[SecureWebServer] Started listening at port: ' + str(SecureWebServerPort)
    except Exception, BindError:
        print ConsoleColor('Error') + 'Fatal Error! Cannot bind socket to port: ' + str(SecureWebServerPort)
        print 'Make sure that other programs are not currently listening to this port!'
        print '\n'
        print 'Additional error info:'
        print BindError, ConsoleColor('End')
        sys.exit(1)
    reactor.run()

if __name__ == '__main__':
    Start()