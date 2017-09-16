from twisted.web import resource


class Simple(resource.Resource):
    isLeaf = True

    def render_GET(self, request):
        print '[SecureWebServer][Get] ' + request.uri

        uri = request.uri
        if uri == '/nucleus/authToken':
            if request.getCookie('magma') != None:
                request.setHeader('content-type', 'text/plain; charset=utf-8')
                return '<success><token code="NEW_TOKEN">' + request.getCookie('magma') + '</token></success>'

        elif uri.find('/nucleus/wallets/') != -1:
            request.setHeader('content-type', 'text/xml; charset=utf-8')
            file_handler = open('Data/wallets.xml', 'rb')
            response = file_handler.read()
            return response

        elif uri.find('/nucleus/entitlements/') != -1:
            HeroID = uri.split('/nucleus/entitlements/')[1]
            request.setHeader('content-type', 'text/xml; charset=utf-8')
            file_handler = open('Data/entitlements.xml', 'rb')
            response = file_handler.read()
            response = response.replace('$HeroID', HeroID)
            return response

        elif uri == '/ofb/products':
            request.setHeader('content-type', 'text/xml; charset=utf-8')
            file_handler = open('Data/products.xml', 'rb')
            response = file_handler.read()
            return response

        elif uri.split(':')[0] == '/relationships/status/nucleus':
            request.setHeader('content-type', 'text/plain; charset=utf-8')
            return '<update><id>1</id><name>Test</name><state>ACTIVE</state><type>server</type><status>Online</status><realid>' + uri.split(':')[1] + '</realid></update>'

        else:
            request.setHeader('content-type', 'text/plain; charset=utf-8')
            return '<update><status>Online</status></update>'

    def render_POST(self, request):
        print '[SecureWebServer][Post] ' + request.uri
        uri = request.uri

        if uri.split(':')[0] == '/relationships/status/nucleus':
            request.setHeader('content-type', 'text/plain; charset=utf-8')
            return '<update><id>1</id><name>Test</name><state>ACTIVE</state><type>server</type><status>Online</status><realid>' + uri.split(':')[1] + '</realid></update>'

        elif uri.split(':')[0] == '/relationships/status/server':
            request.setHeader('content-type', 'text/plain; charset=utf-8')
            return '<update><id>1</id><name>Test</name><state>ACTIVE</state><type>server</type><status>Online</status><realid>' + uri.split(':')[1] + '</realid></update>'

        else:
            request.setHeader('content-type', 'text/plain; charset=utf-8')
            return '<update><status>Online</status></update>'
