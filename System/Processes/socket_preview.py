"""
использует сокеты для обмена данными между заданиями: запускает потоки
выполнения, взаимодействующие с помощью сокетов; независимые программы также
могут использовать сокеты для взаимодействий, потому что они принадлежат
системе в целом, как и именованные каналы; смотрите части книги, посвященные
разработке графических интерфейсов и сценариев для Интернета, где приводятся
более практичные примеры использования сокетов; некоторым серверам может
потребоваться взаимодействовать через сокеты с клиентами в виде потоков
выполнения и процессов; данные через сокеты передаются в виде строк байтов, но
точно так же через них можно передавать сериализованные объекты или кодированный
текст Юникода;
ВНИМАНИЕ: при обращении к функции print в потоках выполнения может потребоваться
синхронизировать их, если есть вероятность перекрытия по времени;
"""
from socket import socket, AF_INET, SOCK_STREAM # переносимый API сокетов

port=50008
host='localhost'

def server():
    sock=socket(AF_INET, SOCK_STREAM) #IP-адрес TCP-соединения
    sock.bind(('', port))               # подключить к порту на заданной машине
    sock.listen(5)                      # количество клиентов

    while True:
        conn, addr=sock.accept()        #ожидание соединения с клиентом
        data = conn.recv(1024)          # чтение данных от клиента
        reply='server got: [%s]' % data #
        conn.send(reply.encode())       # отправить данные клиенту
def client(name):
    sock=socket(AF_INET, SOCK_STREAM)
    sock.connect((host, port))
    sock.send(name.encode())
    reply=sock.recv(1024)
    sock.close()
    print('client got: [%s]' % s reply)

if __name__=='__main__':
    from  threading import Thread
    sthread=Thread(target=server)
    sthread.daemon=True
    sthread.start()
    for i in range(5):
        Thread(target=client, args=('client%s' % i)).start()