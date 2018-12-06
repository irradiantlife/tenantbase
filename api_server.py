import socket
import threading
import SocketServer

class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        data = self.request.recv(1024)
        cur_thread = threading.current_thread()
        response = "{}: {}".format(cur_thread.name, data)
        self.request.sendall(response)

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

class API_Server:

    def __init__(self, database, port):
       print 'entered API_Server init with port: ', port
       self.db = database

       server = ThreadedTCPServer(("", port), ThreadedTCPRequestHandler)
       server_thread = threading.Thread(target=server.serve_forever)
       server_thread.daemon = True
       server_thread.start()
