# simple-websockets

Simple websocket server and client with callback-based API.

[![PyPI - Version](https://img.shields.io/pypi/v/simple-websockets.svg)](https://pypi.org/project/simple-websockets)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/simple-websockets.svg)](https://pypi.org/project/simple-websockets)

-----

**Table of Contents**

- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Installation

```console
pip install simple-websockets
```

## Usage

### Server

Here is a example of websocket echo server:

```python
from simple_websockets import SimpleWSServer

server = SimpleWSServer(host="",
                        port=8765,
                        print_details=True, # Print basic logs
                        print_messages=True) # Print every message received

@server.on_connect
async def on_connect(ws): # called when a client connects
    print(f'Client {ws.remote_address} connected')

@server.on_message
async def on_message(ws, message): # called when a message is received from a client
    await ws.send(message) # send the message back to the client

@server.on_close
async def on_close(ws): # called when a client disconnects
    print(f'Client {ws.remote_address} disconnected')

server.serve() # serve forever
```

### Client

Here is a example of websocket client:

```python
from simple_websockets import SimpleWSClient
client = SimpleWSClient(uri="ws://localhost:8765",
                        print_details=True, # Print basic logs
                        print_messages=True) # Print every message received

@client.on_connect
async def on_connect(ws): # called when the connection is established
    print(f'Connected to {ws.remote_address}')

@client.on_message
async def on_message(ws, message): # called when a message is received
    print(f'Received: {message}')

@client.on_close
async def on_close(ws): # called when the connection is closed
    print(f'Connection to {ws.remote_address} closed')

client.connect() # connect to the server
```

## License

`simple-websockets` is distributed under the terms of the [GPL-3.0-only](https://spdx.org/licenses/GPL-3.0-only.html) license.
