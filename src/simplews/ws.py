from datetime import datetime

class SimpleWS:
    def __init__(self,
                 on_connect,
                 on_close,
                 on_message,
                 print_details,
                 print_messages):
        self.on_connect = on_connect
        self.on_close = on_close
        self.on_message = on_message
        self.print_details = print_details
        self.print_messages = print_messages


    def log(self, message):
        if self.print_details:
            current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"[SimpleWS] [{current_datetime}] {message}")

    def _on_connect(self, websocket):
        self.log(f"Connected: {websocket.remote_address}")
        if self.on_connect:
            self.on_connect(websocket)
    def _on_close(self, websocket):
        self.log(f"Disconnected: {websocket.remote_address}")
        if self.on_close:
            self.on_close(websocket)
    def _on_message(self, websocket, message):
        if not self.print_messages:
            message = "Message received"
        self.log(f"Message from {websocket.remote_address}: {message}")
        if self.on_message:
            self.on_message(websocket, message)

    async def _handler(self, websocket):
        self._on_connect(websocket)
        async for message in websocket:
            self._on_message(websocket, message)
        self._on_close(websocket)