import re
import socket
from threading import Thread
import struct
import time

sk_client = socket.socket()
host = '14.17.102.77'
port = 12602
sk_client.connect((host, port))

def send_msg(msg):
    content = msg.encode()
    length = len(content) + 8
    code = 689
    head = struct.pack('i', length) + struct.pack('i', length) + struct.pack('i', code)
    sk_client.sendall(head + content)

def init(room_id):
    msg_login = 'type@=loginreq/username@=/password@=/roomid@={}/\x00'.format(room_id)
    send_msg(msg_login)
    time.sleep(1)
    msg_join = 'type@=joingroup/rid@={}/gid@=-9999/\x00'.format(room_id)
    send_msg(msg_join)

def get_dm():
    pattern = re.compile(b'type@=chatmsg/.+?/nn@=(.+?)/txt@=(.+?)/.+?/level@=(.+?)/')
    while True:
        buffer = b''
        while True:
            recv_data = sk_client.recv(4096)
            buffer += recv_data
            if recv_data.endswith(b'\x00'):
                break
        for nn ,txt, level in pattern.findall(buffer):
            print("[lv.{:0<2}][{}]: {}".format(level.decode(), nn.decode(), txt.decode().strip()))

def keep_alive():
    while True:
        time.sleep(40)
        msg_keep = 'type@=mrkl/\x00'
        send_msg(msg_keep)

def main():
    init('688')
    t1 = Thread(target=get_dm)
    t2 = Thread(target=keep_alive)
    t1.start()
    t2.start()

if __name__ == '__main__':
    main()