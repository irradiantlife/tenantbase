import socket
import threading
import SocketServer
from database import Database

class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):
    def __init__(self, *args, **keys):
        self.db = Database()
        SocketServer.BaseRequestHandler.__init__(self, *args, **keys)

    def handle(self):
        data = self.request.recv(1024)

        sd = data.splitlines()[0].split()
        if len(sd) < 2:
            self.request.sendall("ERROR")
            return

        verb = sd[0]
        key = sd[1]
        response = ""

        if verb == 'GET':
            response = "VALUE " + (self.db.read(key) or "")

        if verb == 'SET':
            value = data.splitlines()[1]
            self.db.put_value(key, value)
            response = "STORED"

        if verb == 'DELETE':
            value = self.db.read(key) or ""
            self.db.delete(key)
            response = "DELETED" if len(value) > 0 else "NOT_FOUND"

        self.request.sendall(response)

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

class API_Server:

    def __init__(self, port):
       print 'entered API_Server init with port: ', port

       Handler = ThreadedTCPRequestHandler
       server = ThreadedTCPServer(("", port), Handler)
       server_thread = threading.Thread(target=server.serve_forever)
       server_thread.daemon = True
       server_thread.start()
