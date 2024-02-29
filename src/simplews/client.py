import asyncio
from .ws import SimpleWS
from websockets import connect

class SimpleWSClient(SimpleWS):
    def __init__(self,
                 uri="ws://localhost:8765",
                 print_details=True,
                 print_messages=True):
        
        super().__init__(print_details,
                         print_messages)
        self.uri = uri

    async def _main(self):
        self.log("Starting client")   
        async with connect(self.uri) as websocket:
            self.log(f"Connected to {self.uri}")
            self._handler(websocket)
        self.log("Client stopped")

    def connect(self):
        asyncio.run(self._main())
