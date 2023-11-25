from socketserver import TCPServer
from core.server import ThreatedTCPServer,MyTCPHandler


HOST, PORT = "localhost", 8010
TCPServer.allow_reuse_address = True        
with ThreatedTCPServer((HOST, PORT), MyTCPHandler) as server:
    server.serve_forever()
    


