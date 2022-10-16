from asynchat import simple_producer
from pydoc import cli
import socket

message=input("Please Enter Your Mesage : ")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 3213))
s.listen(5)

while True:
    client, address = s.accept()
    key = "abcdefghijklmnopqrstuvwxyz0123456789 !@#"
    val = key[::-1]

    encripter=dict(zip(key, val))

    message = "".join([encripter[words] for words in message.lower()])

    client.send(bytes(message, "utf-8"))
