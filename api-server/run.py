# coding=utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from app import app

import socket
host_ip_addr = socket.gethostbyname(socket.gethostname())
port_no = 5300

app.run(host=host_ip_addr, port=port_no, debug=True)
