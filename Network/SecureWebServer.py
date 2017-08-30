from twisted.web import resource


class Simple(resource.Resource):
    isLeaf = True

    def render_GET(self, request):
        print '[SecureWebServer][Get] ' + request.uri
        if request.uri == '/nucleus/authToken':
            if request.getCookie('magma') != None:
                return '<success><token code="NEW_TOKEN">' + request.getCookie('magma') + '</token></success>'

    def render_POST(self, request):
        print '[SecureWebServer][Post] ' + request.uri