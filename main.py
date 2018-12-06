from api_server import API_Server
from web_server import Web_Server

def main():
    api = API_Server(11211)
    web = Web_Server(8000)

if __name__ == '__main__':
    main()
    try:
        input()
    except SyntaxError:
        print 'Exiting'
        pass
