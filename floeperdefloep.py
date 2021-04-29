import socket
import sys
import threading
import time

import cts
import stc

# create socket used to initiate or respond to a connection request (network-layer, transport-layer)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# initiate contact
cts.initiate_contact(sock)
stc.receive_from_server(sock)

while True:
    end_program = cts.handle_user_input(sock)
    if end_program:
        sys.exit(0)
    stc.receive_from_server(sock)
    stc.receive_from_server(sock)

#THREADS
#    main process?
#    checking user input
#    awaiting server response
