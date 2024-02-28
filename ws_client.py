from json import loads
from websocket import WebSocketApp

from handler import Handler

class WebSocketClient:

    websocket_app: WebSocketApp
    ping_counter = 1

    def __init__(self, web_socket_url: str, handler) -> None:
        self.web_socket_url = web_socket_url
        self.handler = handler
        self.create_ws_app()

    def format_event(self, event: str):
        return loads(event[4:])

    def create_ws_app(self):
        self.websocket_app = WebSocketApp(
            url=self.web_socket_url,
            on_open=self.on_open,
            on_close=self.on_close,
            on_message=self.on_message,
            on_pong=self.on_pong
            )
    
    def on_open(self, ws: WebSocketApp):
        print("Opened connection")
    
    def on_message(self, ws: WebSocketApp, event: str):
        self.handler_event(event)

    def on_close(self, ws, close_status_code, close_msg):
        print("Closed connection")

    def on_pong(self, ws: WebSocketApp, pong_message: str):
        print("Making ping to server 🏓")
        self.ping_counter += 1
        ping_message = f"5:{self.ping_counter}+::" + '{"name":"ping"}'
        ws.send(ping_message)

    def init(self):
        self.websocket_app.run_forever(ping_interval=10)

    def handler_event(self, event: str):

        if not event.startswith("3"):
            return
        
        print("New event had arrive")

        event_json = self.format_event(event)
        self.handler(event_json)


handler = Handler()


ws = WebSocketClient(
    "wss://pub-csm-usea-02-t.trouter.skype.com/socket.io/1/websocket/...",
    handler.general_handler
)

ws.init()