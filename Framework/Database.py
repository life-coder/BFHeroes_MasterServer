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
                  "`EMail`     TEXT NOT NULL UNIQUE," \
                  "`Password`   TEXT NOT NULL," \
                  "`Birthday`   TEXT NOT NULL" \
                  ");"

        cursor = database.cursor()
        cursor.execute(command)
        database.commit()

        command = "CREATE TABLE `Heroes` 	(" \
                  "`AccountID`   INTEGER NOT NULL, " \
                  "`HeroID`   INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, " \
                  "`HeroName`	TEXT NOT NULL UNIQUE" \
                  ");"

        cursor = database.cursor()
        cursor.execute(command)
        database.commit()

        command = "CREATE TABLE `HeroesStats` 	(" \
                  "`HeroID`     INTEGER NOT NULL," \
                  "`StatName`	TEXT NOT NULL," \
                  "`StatValue`  INTEGER DEFAULT 0," \
                  "`StatText`   TEXT" \
                  ");"

        cursor = database.cursor()
        cursor.execute(command)
        database.commit()

        command = "CREATE TABLE `Servers` 	(" \
                  "`ServerID`     INTEGER NOT NULL," \
                  "`OwnerName`    TEXT NOT NULL," \
                  "`ServerPassword`	TEXT NOT NULL UNIQUE," \
                  "`Key`   TEXT NOT NULL" \
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

def RegisterUser(username, email, password, birthday):
    database = sqlite3.connect(DatabaseFileLocation)
    cursor = database.cursor()
    cursor.execute("INSERT INTO Accounts (Username,EMail,Password,Birthday) VALUES (?,?,?,?)", (username, email, password, birthday,))
    database.commit()

def RegisterHero(ID, baseMSGFactionStats, baseMSGPersonaClassStats, baseMSGAppearanceSkinToneStats, haircolor_ui_name, baseMSGAppearanceHairStyleStats, facial_ui_name, nameCharacterText):
    database = sqlite3.connect(DatabaseFileLocation)
    cursor = database.cursor()
    cursor.execute("INSERT INTO `Heroes` (AccountID, HeroName) VALUES (?,?)", (ID, nameCharacterText,))
    database.commit()

    cursor = database.cursor()
    cursor.execute("SELECT HeroID FROM `Heroes` WHERE HeroName = ?", (nameCharacterText,))
    HeroID = cursor.fetchone()[0]

    cursor = database.cursor()
    cursor.execute("INSERT INTO `HeroesStats` (HeroID, StatName, StatValue) VALUES (?,?,?)", (HeroID, 'c_team', baseMSGFactionStats))
    cursor.execute("INSERT INTO `HeroesStats` (HeroID, StatName, StatValue) VALUES (?,?,?)", (HeroID, 'c_kit', baseMSGPersonaClassStats))
    cursor.execute("INSERT INTO `HeroesStats` (HeroID, StatName, StatValue) VALUES (?,?,?)", (HeroID, 'c_skc', baseMSGAppearanceSkinToneStats))
    cursor.execute("INSERT INTO `HeroesStats` (HeroID, StatName, StatValue) VALUES (?,?,?)", (HeroID, 'c_hrc', haircolor_ui_name))
    cursor.execute("INSERT INTO `HeroesStats` (HeroID, StatName, StatValue) VALUES (?,?,?)", (HeroID, 'c_fhrs', baseMSGAppearanceHairStyleStats))
    cursor.execute("INSERT INTO `HeroesStats` (HeroID, StatName, StatValue) VALUES (?,?,?)", (HeroID, 'c_hrs', facial_ui_name))
    database.commit()

def GetStat(ID, StatName):
    database = sqlite3.connect(DatabaseFileLocation)
    cursor = database.cursor()
    cursor.execute("SELECT StatValue FROM `HeroesStats` WHERE `HeroID` = ? AND `StatName` = ?", (ID,StatName,))
    value = cursor.fetchone()
    if value == None:
        value = 0
    else:
        value = value[0]
    return value

def GetText(ID, StatName):
    database = sqlite3.connect(DatabaseFileLocation)
    cursor = database.cursor()
    cursor.execute("SELECT StatText FROM `HeroesStats` WHERE `HeroID` = ? AND `StatName` = ?", (ID,StatName,))
    value = cursor.fetchone()
    if value == None:
        value = 0
    else:
        value = value[0]
    return value

def UpdateStat(ID, StatName, StatValue, StatText):
    database = sqlite3.connect(DatabaseFileLocation)
    cursor = database.cursor()
    cursor.execute("SELECT StatValue FROM `HeroesStats` WHERE `HeroID` = ? AND `StatName` = ?", (ID,StatName,))
    value = cursor.fetchone()

    if value == None:
        cursor = database.cursor()
        cursor.execute("INSERT INTO `HeroesStats` (HeroID, StatName, StatValue, StatText) VALUES (?,?,?,?)", (ID, StatName, StatValue, StatText,))
    else:
        cursor = database.cursor()
        cursor.execute("UPDATE `HeroesStats` SET StatName = ?, StatValue = ?, StatText = ? WHERE StatName = ? AND HeroID = ?", (StatName, StatValue, StatText, StatName, ID,))
    database.commit()

def GetHeroes(ID):
    database = sqlite3.connect(DatabaseFileLocation)
    cursor = database.cursor()
    cursor.execute("SELECT * FROM `Heroes` WHERE `AccountID` = ?", (ID,))
    return cursor.fetchall()

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

def GetEmail(ID):
    database = sqlite3.connect(DatabaseFileLocation)
    cursor = database.cursor()
    cursor.execute("SELECT EMail FROM `Accounts` WHERE AccountID = ?", (ID,))
    return cursor.fetchone()[0]

def GetBirthday(ID):
    database = sqlite3.connect(DatabaseFileLocation)
    cursor = database.cursor()
    cursor.execute("SELECT Birthday FROM `Accounts` WHERE AccountID = ?", (ID,))
    return cursor.fetchone()[0]

def GetHeroIDByName(name):
    database = sqlite3.connect(DatabaseFileLocation)
    cursor = database.cursor()
    cursor.execute("SELECT HeroID FROM `Heroes` WHERE HeroName = ?", (name,))
    value = cursor.fetchone()
    if value == None:
        return False
    else:
        return value[0]

def CheckServerPassword(password):
    database = sqlite3.connect(DatabaseFileLocation)
    cursor = database.cursor()
    cursor.execute("SELECT * FROM `Servers` WHERE `ServerPassword` = ?", (password,))
    value = cursor.fetchone()
    if value == None:
        return False
    else:
        return value[0]

def GetServerAuthData(id):
    database = sqlite3.connect(DatabaseFileLocation)
    cursor = database.cursor()
    cursor.execute("SELECT * FROM `Servers` WHERE `ServerID` = ?", (id,))
    value = cursor.fetchone()
    if value == None:
        return False
    else:
        return value