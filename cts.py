# Client to Server functions
import socket
import sys


def initiate_contact(sock):
    host_port = ("3.121.226.198", 5378)

    # establishes a connection using a socket (IP-address/domain name, port number)
    sock.connect(host_port)

    # Encode first hand-shake message
    string_send_bytes = "HELLO-FROM DavidBenjamin\n".encode("utf-8")

    # sendall calls send repeatedly until all bytes are sent
    sock.sendall(string_send_bytes)


def determine_input_type(user_input):
    if user_input == "!quit":
        print("Quitting!")
        return "quit"
    elif user_input == "!who":
        return "who"
    elif user_input[0] == "@":
        return "msg"
    else:
        print("Unknown command. Please try again.")


def perform_user_action(sock, user_input_type, user_input):
    if user_input_type == "who":
        print("Finding users!")  # DEBUG
        string_send_bytes = "WHO\n".encode("utf-8")
        sock.sendall(string_send_bytes)
    elif user_input_type == "msg":
        string_send = "SEND " + user_input.lstrip("@") + "\n"
        print("Sending: " + string_send)
        string_send_bytes = string_send.encode("utf-8")
        sock.sendall(string_send_bytes)


def handle_user_input(sock):
    # get user input
    user_input = input("Type a command (!) or message (@): ")

    # determine input type
    user_input_type = determine_input_type(user_input)
    if user_input_type == "quit":
        print("hello")
        return True

    # perform user action
    perform_user_action(sock, user_input_type, user_input)
