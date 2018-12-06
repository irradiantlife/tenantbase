import SimpleHTTPServer
import SocketServer
import threading


class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass


class Web_Server:

    def __init__(self, database, port):
        print "entered Web_Server init with port:", port

        self.db = database

        Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

        server = ThreadedTCPServer(("", port), Handler)

        server_thread = threading.Thread(target=server.serve_forever)
        server_thread.daemon = True
        server_thread.start()
