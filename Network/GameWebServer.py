from twisted.web import resource


class Simple(resource.Resource):
    isLeaf = True

    def render_GET(self, request):
        print '[WebServer][Get] ' + request.uri

    def render_POST(self, request):
        print '[WebServer][Post] ' + request.uri