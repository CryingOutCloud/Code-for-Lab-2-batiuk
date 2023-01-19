import socket

BYTES_TO_READ = 4096

def get(host, port):
    # created our request
    request_data = b"GET / HTTP/1.1\nHost:" + host.encode('utf-8') + b'\n\n'

    # create our socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # sent some data
    s.connect((host, port))
    s.send(request_data)

    # otherwise, server will hang
    s.shutdown(socket.SHUT_WR)

    # listen to response from server
    response = s.recv(BYTES_TO_READ)
    while(len(response) > 0):
        print(response)
        response = s.recv(BYTES_TO_READ)

    s.close()


get("www.google.com", 80)