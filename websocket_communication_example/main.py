# simple ping-pong example of websocket and the vayamos wss stream

from websocket import create_connection
from threading import Thread
from time import sleep

ws = create_connection("wss://stream.Vayamos.cc")

def ping():
  while True:
    ws.send('{"op": "ping", "id": 123}')
    sleep(5)

Thread(target=ping).start()

while True:
  result =  ws.recv()
  print ("Received '%s'" % result)