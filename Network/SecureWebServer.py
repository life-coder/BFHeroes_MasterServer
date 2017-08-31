from twisted.web import resource


class Simple(resource.Resource):
    isLeaf = True

    def render_GET(self, request):
        print '[SecureWebServer][Get] ' + request.uri
        if request.uri == '/nucleus/authToken':
            if request.getCookie('magma') != None:
                return '<success><token code="NEW_TOKEN">' + request.getCookie('magma') + '</token></success>'

        else:
            return '<update><status>Online</status></update>'

    def render_POST(self, request):
        print '[SecureWebServer][Post] ' + request.uri
        uri = request.uri

        if uri.split(':')[0] == '/relationships/status/nucleus':
            return '<update><id>1</id><name>Test</name><state>ACTIVE</state><type>server</type><status>Online</status><realid>' + uri.split(':')[1] + '</realid></update>'

        else:
            return '<update><status>Online</status></update>'
