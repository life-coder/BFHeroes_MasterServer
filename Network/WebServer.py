from twisted.web import resource
from Config import ConsoleColor
from Framework.Database import RegisterUser, LoginUser, SaveWebSession, GetWebSession
from Utils import RandomStringGenerator
from base64 import b64encode

class Simple(resource.Resource):
    isLeaf = True

    def render_GET(self, request):
        uri = request.uri

        if uri == '/':
            uri = '/index'

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

            elif account[1] == username and account[2] == password:
                SessionID = RandomStringGenerator.Generate(64)
                SaveWebSession(SessionID, username)
                response = '<meta http-equiv="set-cookie" content="SessionID=' + SessionID + '; Path=/; ">'
                response += '<meta http-equiv="refresh" content="0; url=/" />'

                return response

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

        if len(uri.split('/')) == 2:
            uri += '.html'

        try:
            file_handler = open('Web' + uri, 'rb')
            response = file_handler.read()
            if uri == '/index.html':
                launch_arguments = b64encode('+sessionId ' + request.getCookie('SessionID') + ' +magma ' +
                                             str(GetWebSession(request.getCookie('SessionID'))[
                                                     0]) + ' +punkbuster 0 +developer 1')
                response = response.replace('$LaunchGame', 'bfheroes://' + launch_arguments)
            file_handler.close()
        except:
            request.setResponseCode(404)
            response = '<html><body><h1>404 - Not Found</h1></body></html>'

        return response

    def render_POST(self, request):
        print '[WebServer][Post] ' + request.uri

        if request.uri == '/api/register':
            data = request.content.getvalue()

            try:
                username = data.split('username=')[1].split('&')[0]
            except:
                return '{ "status": "err", "code": "username", "message": "' + "You must enter username!" + '", "data": "null" }'

            try:
                password1 = data.split('password=')[1].split('&')[0]
                password2 = data.split('password2=')[1]
            except:
                request.setHeader('content-type', 'application/json')
                return '{ "status": "err", "code": "password1", "message": "' + "You must enter both passwords!" + '", "data": "null" }'

            if password1 != password2:
                request.setHeader('content-type', 'application/json')
                return '{ "status": "err", "code": "password2", "message": "' + "Passwords you typed doesn't match!" + '", "data": "null" }'

            try:
                RegisterUser(username, password1)
            except:
                return '{ "status": "err", "code": "username", "message": "' + "This username is already registered!" + '", "data": "null" }'

            print ConsoleColor(
                'Success') + '[WebServer] Successfully registered new user! (' + username + ')' + ConsoleColor('End')
            return '{ "status": "ok", "data": {"redirect": "/api/GetSession?username=' + username + '&password=' + password1 + '"}, "message": "' + "Hello" + username + "!" + '" }'

        if request.uri == '/api/login':
            request.setHeader('content-type', 'application/json')
            data = request.content.getvalue()

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

            if account[1] == username and account[2] == password:
                print ConsoleColor(
                    'Success') + '[WebServer] User ' + username + ' successfully logged in!' + ConsoleColor('End')
                return '{ "status": "ok", "data": {"redirect": "/api/GetSession?username=' + username + '&password=' + password + '"}, "message": "' + "Hello" + username + "!" + '" }'
