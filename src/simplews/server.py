import asyncio
from .ws import SimpleWS
from websockets import serve

class SimpleWSServer(SimpleWS):
    def __init__(self,
                 host="",
                 port=8765,
                 on_connect=None,
                 on_close=None,
                 on_message=None,
                 print_details=True,
                 print_messages=True):
        
        super().__init__(on_connect,
                         on_close,
                         on_message,
                         print_details,
                         print_messages)
        self.host = host
        self.port = port
        
    async def _main(self):
        self.log("Starting server")        
        async with serve(self._handler, self.host, self.port):
            self.log(f"Server started at port {self.port}")
            await asyncio.get_running_loop().create_future()  # run forever
        self.log("Server stopped")

    def serve(self):
        asyncio.run(self._main())
