# -*- coding: utf-8 -*-

import socket
from app import app


host_ip_addr = socket.gethostbyname(socket.gethostname())
port_no = 5300

app.run(host=host_ip_addr, port=port_no, debug=True)
