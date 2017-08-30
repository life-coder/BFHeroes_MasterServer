import sqlite3, os
from Config import DatabaseFileLocation, ConsoleColor


def Prepare():
    if os.path.exists(DatabaseFileLocation):
        pass
    else:
        print ConsoleColor('Info') + '[Database] Creating database file...' + ConsoleColor('End')
        try:
            database = sqlite3.connect(DatabaseFileLocation)
        except Exception, e:
            raise Exception, e

        command = "CREATE TABLE `Accounts` 	(" \
                  "`AccountID`   INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, " \
                  "`Username`	TEXT NOT NULL UNIQUE," \
                  "`Password`   TEXT NOT NULL" \
                  ");"

        cursor = database.cursor()
        cursor.execute(command)
        database.commit()

        command = "CREATE TABLE `Personas` 	(" \
                  "`AccountID`   INTEGER NOT NULL, " \
                  "`PersonaName`	TEXT NOT NULL UNIQUE" \
                  ");"

        cursor = database.cursor()
        cursor.execute(command)
        database.commit()

        command = "CREATE TABLE `WebSessions` 	(" \
                  "`AccountID`   INTEGER NOT NULL, " \
                  "`SessionID`	TEXT NOT NULL UNIQUE" \
                  ");"

        cursor = database.cursor()
        cursor.execute(command)
        database.commit()

def RegisterUser(username, password):
    database = sqlite3.connect(DatabaseFileLocation)
    cursor = database.cursor()
    cursor.execute("INSERT INTO Accounts (Username,Password) VALUES (?,?)", (username, password,))
    database.commit()

def LoginUser(username):
    database = sqlite3.connect(DatabaseFileLocation)
    cursor = database.cursor()
    cursor.execute("SELECT * FROM `Accounts` WHERE `Username` = ?", (username,))
    return cursor.fetchone()

def SaveWebSession(NewSession, username):
    id = GetAccountID(username)

    database = sqlite3.connect(DatabaseFileLocation)
    cursor = database.cursor()
    cursor.execute("INSERT INTO `WebSessions` VALUES (?,?)", (id, NewSession,))
    database.commit()

def DeleteWebSession(Session):
    database = sqlite3.connect(DatabaseFileLocation)
    cursor = database.cursor()
    cursor.execute("DELETE FROM `WebSessions` WHERE SessionID = ?", (Session,))
    database.commit()

def GetWebSession(Session):
    database = sqlite3.connect(DatabaseFileLocation)
    cursor = database.cursor()
    cursor.execute("SELECT * FROM `WebSessions` WHERE SessionID = ?", (Session,))
    return cursor.fetchone()

def GetAccountID(username):
    database = sqlite3.connect(DatabaseFileLocation)
    cursor = database.cursor()
    cursor.execute("SELECT AccountID FROM `Accounts` WHERE Username = ?", (username,))
    return cursor.fetchone()[0]

def GetUserName(ID):
    database = sqlite3.connect(DatabaseFileLocation)
    cursor = database.cursor()
    cursor.execute("SELECT Username FROM `Accounts` WHERE AccountID = ?", (ID,))
    return cursor.fetchone()[0]