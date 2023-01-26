import socket
import threading
import time

class Server:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

        # Создаем сокет
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.ip, self.port))
        self.server.listen(10)
        threading.Thread(target=self.connected_strim).start()
        print('[+]Server start')

    def connected_strim(self):
        while True:
            clien, addres = self.server.accept()
            clien.send('[*]Connect...'.encode('UTF-8'))
            time.sleep(1)

Server('127.0.0.1', 5555)





# if __name__ == '__main__':
#     print_hi('PyCharm')

