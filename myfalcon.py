import falcon


class Health(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = ('OK')

def myapp():
    app = falcon.API()
    health = Health()
    app.add_route('/health', health)
    return app

if __name__ == '__main__':
    from wsgiref import simple_server
    wsgi_app = myapp()
    httpd = simple_server.make_server('127.0.0.1', 8070, wsgi_app)
    httpd.serve_forever()
