import SimpleHTTPServer
import SocketServer
import threading
from database import Database
import json


class ThreadedSimpleHTTPRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def __init__(self, *args, **keys):
        self.db = Database()
        SimpleHTTPServer.SimpleHTTPRequestHandler.__init__(self, *args, **keys)

    def do_GET(self):
        if (self.path.endswith('json')):
            rawdata = self.db.read_all()
            content = json.dumps([dict(ix) for ix in rawdata])

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(content)
            return
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

class Web_Server:

    def __init__(self, port):
        print "entered Web_Server init with port:", port

        Handler = ThreadedSimpleHTTPRequestHandler

        server = ThreadedTCPServer(("", port), Handler)
        server_thread = threading.Thread(target=server.serve_forever)
        server_thread.daemon = True
        server_thread.start()
