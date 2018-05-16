import cv2
import socket
import numpy

address = ('10.10.10.181', 8001)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(address)
s.listen(True)

def receive(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf:
            return None
        buf += newbuf
        count -= len(newbuf)
    return buf

conn, addr = s.accept()
while 1:
    length = receive(conn, 16)
    stringData = receive(conn, int(length))
    data = numpy.fromstring(stringData, dtype='uint8')
    decimg = cv2.imdecode(data, 1)
    cv2.imshow('SERVER', decimg)
    if cv2.waitKey(10) == 27:
        break

s.close()
cv2.destroyAllWindows()

