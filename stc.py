# Server To Client functions
import socket

def receive_from_server(sock):
    # Wait until data comes in
    # Receive at most 4096 bytes.
    server_msg = sock.recv(4096)
    server_msg = server_msg.decode("utf-8")  # Transform server_msg from type bytes into string

    # DEBUG: Display whether or not data was received
    if not server_msg:
        print("Socket is closed.")
    else:
        print("Socket has data.")
    print(server_msg)

    if server_msg.find("WHO-OK"):
        print("YES!")

    #def check_server_response(msg):

# Determine server response
# server_response_type = check_server_response(server_msg)