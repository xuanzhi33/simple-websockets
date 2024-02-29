import asyncio
from .ws import SimpleWS
from websockets import serve
from websockets import broadcast as ws_broadcast

class SimpleWSServer(SimpleWS):
    def __init__(self,
                 host="",
                 port=8765,
                 print_details=True,
                 print_messages=True):
        
        super().__init__(print_details,
                         print_messages)
        self.host = host
        self.port = port
        
    async def _main(self):
        self.log("Starting server")
        try:
            async with serve(self._handler, self.host, self.port):
                self.log(f"Server started at port {self.port}")
                await asyncio.get_running_loop().create_future()  # run forever
        except asyncio.CancelledError:
            self.log("Server stopped")

    def broadcast(self, clients, message):
        ws_broadcast(clients, message)

    def serve(self):
        asyncio.run(self._main())
