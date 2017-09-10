from twisted.web import html, resource
from twisted.web.util import redirectTo
from twisted.web.server import Session
from Config import ConsoleColor
from Framework.Database import RegisterUser, LoginUser, SaveWebSession, GetWebSession, GetAccountID, RegisterHero
from Utils import RandomStringGenerator
from base64 import b64encode

TempData = []

class Simple(resource.Resource):
    isLeaf = True

    def render_GET(self, request):
        uri = request.uri
        session = request.getSession()

        if uri == '/':
            uri = '/index'

        if uri == '/api/status':
            request.setHeader('content-type', 'application/json')
            login = "false"
            data = ""
            if hasattr(session, 'username'):
                login = "true"
                try:
                    launch_arguments = b64encode('+sessionId ' + request.getCookie('SessionID') + ' +magma ' +
                                                 str(GetWebSession(request.getCookie('SessionID'))[
                                                         0]) + ' +punkbuster 0 +developer 1')
                    data = 'bfheroes://' + launch_arguments
                except:
                    data = '#'

                return '{ "status": "ok", "login": ' + login + ', "data": {"token": "' + data + '", "username": "' +  html.escape(session.username) + '"}}'
            return '{ "status": "ok", "login": ' + login + ', "data": {}}'

        if uri == '/Logout':
            if hasattr(session, 'username'):
                request.getSession().expire()
                session.username = ""
            return redirectTo("/", request)

        if uri.split('?')[0] == '/api/GetSession':
            data = uri.split('?')[1]

            try:
                username = data.split('username=')[1].split('&')[0]
                password = data.split('password=')[1]
            except:
                response = '<meta http-equiv="refresh" content="0; url=/" />'
                return response

            account = LoginUser(username)
            if account == None:
                response = '<meta http-equiv="refresh" content="0; url=/" />'
                return response

            elif account[1] == username and account[3] == password:
                SessionID = RandomStringGenerator.Generate(64)
                SaveWebSession(SessionID, username)
                response = '<meta http-equiv="set-cookie" content="SessionID=' + SessionID + '; Path=/; ">'
                response += '<meta http-equiv="refresh" content="0; url=/" />'

                return response
            else:
                return '<meta http-equiv="refresh" content="0; url=/" />'

        if uri.find('.css') != -1:
            request.setHeader('content-type', 'text/css')

        if uri.find('.js') != -1:
            request.setHeader('content-type', 'application/javascript')

        if uri.find('.png') != -1:
            request.setHeader('content-type', 'image/png')

        if uri.find('.jpg') != -1:
            request.setHeader('content-type', 'image/jpeg')

        if uri.find('.gif') != -1:
            request.setHeader('content-type', 'image/gif')

        if uri.find('/Register') != -1: # Block Direct Register Request
            response = '<meta http-equiv="refresh" content="0; url=/" />'
            return response

        if len(uri.split('/')) == 2:
            uri += '.html'

        try:
            # Fixed going outside 'Web' Directory
            uri = uri.replace('..', '')
            file_handler = open('Web' + uri , 'rb')
            response = file_handler.read()
            if uri == '/index.html':
                try:
                    launch_arguments = b64encode('+sessionId ' + request.getCookie('SessionID') + ' +magma ' +
                                                 str(GetWebSession(request.getCookie('SessionID'))[
                                                         0]) + ' +punkbuster 0 +developer 1')
                    response = response.replace('$LaunchGame', 'bfheroes://' + launch_arguments)
                except:
                    response = response.replace('$LaunchGame', '#')
            file_handler.close()
        except:
            request.setResponseCode(404)
            response = '<html><body><h1>404 - Not Found</h1></body></html>'

        return response

    def render_POST(self, request):
        print '[WebServer][Post] ' + request.uri
        session = request.getSession()

        if request.uri == '/api/register':
            request.setHeader('content-type', 'application/json')
            data = request.content.getvalue()

            entries = len(TempData)
            loop = 0

            while loop != entries:
                Session = TempData[loop]
                if Session.keys()[0] == session.uid:
                    data2 = Session[session.uid]
                loop += 1

            if hasattr(session, 'username'):
                return '{ "status": "err", "code": "username", "message": "You have already an account!", "data": "null" }'

            try:
                username = data.split('username=')[1].split('&')[0]
                if len(username) == 0:
                    raise Exception
            except:
                return '{ "status": "err", "code": "username", "message": "' + "You must enter username!" + '", "data": "null" }'

            try:
                email = data.split('email=')[1].split('&')[0]
                if len(email) == 0:
                    raise Exception
            except:
                return '{ "status": "err", "code": "username", "message": "' + "You must enter email!" + '", "data": "null" }'

            try:
                password1 = data.split('password=')[1].split('&')[0]
                password2 = data.split('password2=')[1].split('&')[0]

                if len(password1) == 0:
                    raise Exception
                if len(password2) == 0:
                    raise Exception
            except:
                request.setHeader('content-type', 'application/json')
                return '{ "status": "err", "code": "password1", "message": "' + "You must enter both passwords!" + '", "data": "null" }'

            if password1 != password2:
                request.setHeader('content-type', 'application/json')
                return '{ "status": "err", "code": "password2", "message": "' + "Passwords you typed doesn't match!" + '", "data": "null" }'

            try:
                birthday = data.split('birthday=')[1]

                if len(birthday) == 0:
                    raise Exception
            except:
                return '{ "status": "err", "code": "birthday", "message": "' + "You didn't specified correct birthday date!" + '", "data": "null" }'

            try:
                RegisterUser(username, email, password1, birthday)
            except:
                return '{ "status": "err", "code": "username", "message": "' + "This username or email are already registered!" + '", "data": "null" }'

            AccountID = GetAccountID(username)

            try:
                pass
            except:
                print ConsoleColor('Warning') + "[WebServer][Register] Cannot register new hero!" + ConsoleColor('End')
            baseMSGFactionStats = data2.split('baseMSGFactionStats=')[1].split('&')[0]
            baseMSGPersonaClassStats = data2.split('baseMSGPersonaClassStats=')[1].split('&')[0]
            baseMSGAppearanceSkinToneStats = data2.split('baseMSGAppearanceSkinToneStats=')[1].split('&')[0]
            haircolor_ui_name = data2.split('haircolor_ui_name=')[1].split('&')[0]
            baseMSGAppearanceHairStyleStats = data2.split('baseMSGAppearanceHairStyleStats=')[1].split('&')[0]
            facial_ui_name = data2.split('facial_ui_name=')[1].split('&')[0]
            nameCharacterText = data2.split('nameCharacterText=')[1]
            RegisterHero(AccountID, baseMSGFactionStats, baseMSGPersonaClassStats, baseMSGAppearanceSkinToneStats,
                         haircolor_ui_name, baseMSGAppearanceHairStyleStats, facial_ui_name, nameCharacterText)
            TempData.remove(Session)
            print ConsoleColor(
                'Success') + '[WebServer] Successfully registered new user! (' + username + ')' + ConsoleColor('End')
            session.username = username
            return '{ "status": "ok", "data": {"redirect": "/api/GetSession?username=' + username + '&password=' + password1 + '"}, "message": "' + "Hello" + username + "!" + '" }'

        if request.uri == '/api/login':
            request.setHeader('content-type', 'application/json')
            data = request.content.getvalue()

            if hasattr(session, 'username'):
                return '{ "status": "err", "code": "username", "message": "You are already loggedom!", "data": "null" }'

            try:
                if len(data.split('&')[0].split('username=')[1]) == 0:
                    raise Exception

                username = data.split('&')[0].split('username=')[1]
            except:
                request.setHeader('content-type', 'application/json')
                return '{ "status": "err", "code": "username", "message": "' + "You must enter username!" + '", "data": "null" }'

            try:
                if len(data.split('&')[1].split('password=')[1]) == 0:
                    raise Exception

                password = data.split('&')[1].split('password=')[1]
            except:
                request.setHeader('content-type', 'application/json')
                return '{ "status": "err", "code": "password", "message": "' + "You must enter password!" + '", "data": "null" }'

            account = LoginUser(username)

            if account == None:
                return '{ "status": "err", "code": "username", "message": "' + "User not found!" + '", "data": "null" }'

            if account[1] == username and account[3] == password:
                print ConsoleColor(
                    'Success') + '[WebServer] User ' + username + ' successfully logged in!' + ConsoleColor('End')
                session.username = username
                return '{ "status": "ok", "data": {"redirect": "/api/GetSession?username=' + username + '&password=' + password + '"}, "message": "' + "Hello" + username + "!" + '" }'

        if request.uri == '/Register':
            file_handler = open('Web/Register.html', 'rb')
            response = file_handler.read()
            TempData.append({session.uid: request.content.getvalue()})
            file_handler.close()
            return response