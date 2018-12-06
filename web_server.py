import SimpleHTTPServer
import SocketServer
import threading
from database import Database


class ThreadedSimpleHTTPRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def __init__(self, *args, **keys):
        self.db = Database()
        SimpleHTTPServer.SimpleHTTPRequestHandler__init__(self, *args, **keys)

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
