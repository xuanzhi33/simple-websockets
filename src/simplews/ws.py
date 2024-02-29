from datetime import datetime

class SimpleWS:
    def __init__(self,
                 print_details,
                 print_messages):
        self.on_connect_callback = None
        self.on_close_callback = None
        self.on_message_callback = None
        self.print_details = print_details
        self.print_messages = print_messages


    def log(self, message):
        if self.print_details:
            current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"[Simple Websockets] [{current_datetime}] {message}")

    async def _on_connect(self, websocket):
        self.log(f"Connected: {websocket.remote_address}")
        if self.on_connect_callback:
            await self.on_connect_callback(websocket)
    async def _on_close(self, websocket):
        self.log(f"Disconnected: {websocket.remote_address}")
        if self.on_close_callback:
            await self.on_close_callback(websocket)
    async def _on_message(self, websocket, message):
        if self.print_messages:
            self.log(f"Message from {websocket.remote_address}: {message}")
        if self.on_message_callback:
            await self.on_message_callback(websocket, message)

    async def _handler(self, websocket):
        await self._on_connect(websocket)
        async for message in websocket:
            await self._on_message(websocket, message)
        await self._on_close(websocket)
    
    # Decorators
    def on_connect(self, callback):
        self.on_connect_callback = callback
        return callback
    def on_close(self, callback):
        self.on_close_callback = callback
        return callback
    def on_message(self, callback):
        self.on_message_callback = callback
        return callback
