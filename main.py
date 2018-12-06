from database import Database
from api_server import API_Server
from web_server import Web_Server

def main():
    db = Database()
    api = API_Server(db, 11211)
    web = Web_Server(db, 8000)

if __name__ == '__main__':
    main()
