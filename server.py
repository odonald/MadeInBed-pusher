from SimpleWebSocketServer import WebSocket, SimpleWebSocketServer

wss = [] # Should be globally scoped


class SimpleEcho(WebSocket):

    def handleMessage(self):

        if self.data is None:
            self.data = ''
        for ws in wss:
            ws.sendMessage(str(self.data))

        # echo message back to client
        self.sendMessage(str(self.data))
        print(self.data)

    def handleConnected(self):
        if self not in wss:
                wss.append(self)

    def handleClose(self):
        wss.remove(self)

server = SimpleWebSocketServer('localhost', 3000, SimpleEcho)
server.serveforever()