import socket
import threading

#socket used to initiate or respond to a connection request (network-layer, transport-layer)
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_port=("3.121.226.198",5378)

#establishes a connection using a socket (IP-address/domain name, port number)
sock.connect(host_port)

string_bytes="HELLO-FROM DavidBenjamin\n".encode("utf-8")

# sendall calls send repeatedly until all bytes are sent.
sock.sendall(string_bytes)

# Waiting until data comes in
# Receive at most 4096 bytes.
data = sock.recv(4096)

# Display whether or not data was received
if not data:
    print("Socket is closed.")
else:
    print("Socket has data.")

print(data)

# Exception handling
try:
    sock.send("how to handle errors?".encode("utf-8"))
    answer=sock.recv(4096)
except OSError as msg:
    print(msg)

# Get user input and analyse string
def GetUserInput():
    userInput = input("Type a command (!) or message (@): ")
    InputCheckCommand = {'!'}
    InputCheckMessage = {'@'}
    if InputCheckCommand in userInput:
        print("userInput is command")
    #print("Is this what you just said?: ", userInput)

t=threading.Thread(target=print, args=("hello","world"))
t.start()
t.join()
