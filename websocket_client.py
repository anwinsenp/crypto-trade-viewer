from typing import Optional

from PyQt5.QtWebSockets import QWebSocket
from PyQt5.QtCore import QObject, QUrl, pyqtSignal


class WebsocketClient(QObject):
    data_changed = pyqtSignal(str)

    def __init__(self, parent: Optional[QObject] = ...) -> None:
        super().__init__(parent=parent)
        self.websocket = QWebSocket()
        self.websocket.stateChanged.connect(self.on_state_changed)
        self.websocket.error.connect(self.on_error)
        self.websocket.textMessageReceived.connect(self.data_changed)

    def connectToHost(self, address: str) -> None:
        self.websocket.open(QUrl(address))

    def disconnect(self) -> None:
        self.websocket.close()

    def on_state_changed(self, state) -> None:
        print("websocket client state changed: ", state)

    def on_error(self, error) -> None:
        print("websocket client error: ", error)
