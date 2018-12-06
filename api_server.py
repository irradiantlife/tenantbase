import socket
import threading

class API_Server:

    def __init__(self, database, port):
       print('entered API_Server init with port: ?', [port])
       self.db = database

       bind_ip = '0.0.0.0'

       self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       self.server.bind((bind_ip, port))
       self.server.listen(5)  # max backlog of connections

       print 'Listening on {}:{}'.format(bind_ip, port)

       while True:
           client_sock, address = self.server.accept()
           print 'Accepted connection from {}:{}'.format(address[0], address[1])
           client_handler = threading.Thread(
               target=handle_client_connection,
               args=(client_sock,)  # without comma you'd get a... TypeError: handle_client_connection() argument after * must be a sequence, not _socketobject
           )
           client_handler.start()


    def handle_client_connection(client_socket):
        request = client_socket.recv(1024)
        print 'Received {}'.format(request)
        client_socket.send('ACK!')
        client_socket.close()
