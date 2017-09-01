from twisted.web import resource


class Simple(resource.Resource):
    isLeaf = True

    def render_GET(self, request):
        print '[SecureWebServer][Get] ' + request.uri

        uri = request.uri
        if uri == '/nucleus/authToken':
            if request.getCookie('magma') != None:
                return '<success><token code="NEW_TOKEN">' + request.getCookie('magma') + '</token></success>'

        elif uri.find('/nucleus/wallets/') != -1:
            HeroID = uri.split('/nucleus/wallets/')[1]
            request.setHeader('content-type', 'text/xml')
            return '<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\" ?><billingAccounts><walletAccount><currency>hp</currency><balance>1</balance></billingAccounts>"'

        elif uri.find('/nucleus/entitlements/') != -1:
            HeroID = uri.split('/nucleus/entitlements/')[1]
            request.setHeader('content-type', 'text/xml')
            file_handler = open('Data/entitlements.xml', 'rb')
            response = file_handler.read()
            response = response.replace('$HeroID', HeroID)
            return response

        elif uri == '/ofb/products':
            request.setHeader('content-type', 'text/xml')
            file_handler = open('Data/products.xml', 'rb')
            response = file_handler.read()
            return response

        elif uri.split(':')[0] == '/relationships/status/nucleus':
            return '<update><id>1</id><name>Test</name><state>ACTIVE</state><type>server</type><status>Online</status><realid>' + uri.split(':')[1] + '</realid></update>'

        else:
            return '<update><status>Online</status></update>'

    def render_POST(self, request):
        print '[SecureWebServer][Post] ' + request.uri
        uri = request.uri

        if uri.split(':')[0] == '/relationships/status/nucleus':
            return '<update><id>1</id><name>Test</name><state>ACTIVE</state><type>server</type><status>Online</status><realid>' + uri.split(':')[1] + '</realid></update>'

        elif uri.split(':')[0] == '/relationships/status/server':
            return '<update><id>1</id><name>Test</name><state>ACTIVE</state><type>server</type><status>Online</status><realid>' + uri.split(':')[1] + '</realid></update>'

        else:
            return '<update><status>Online</status></update>'
