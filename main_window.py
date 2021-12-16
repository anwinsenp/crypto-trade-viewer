from PyQt5.QtWidgets import QLabel, QMainWindow, QWidget
from data_table_view import DataTableView
from websocket_client import WebsocketClient
from instrument_model import InstrumentModel
from orderbook_model import OrderbookModel

from PyQt5.QtCore import QSortFilterProxyModel
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Trade Viewer")

        instrument_label = QLabel("Bitmex - topic: instrument, action: update")
        instrument_table = DataTableView(self)
        instrument_table.setSortingEnabled(True)

        instrument_model = InstrumentModel(self)
        instrument_proxymodel = QSortFilterProxyModel(self)
        instrument_proxymodel.setSourceModel(instrument_model)
        instrument_table.setModel(instrument_proxymodel)

        instrument_ws_client = WebsocketClient(self)
        instrument_ws_client.data_changed.connect(
            instrument_model.append_data)
        instrument_ws_client.connectToHost(
            "wss://ws.bitmex.com/realtime?subscribe=instrument")

        instrument_vboxlayout = QVBoxLayout(self)
        instrument_vboxlayout.addWidget(instrument_label)
        instrument_vboxlayout.addWidget(instrument_table)

        instrument_widget = QWidget(self)
        instrument_widget.setLayout(instrument_vboxlayout)

        # Bitmex Instrument topic table
        orderbook_label = QLabel("Bitmex - topic: orderbook, action: insert")
        orderbook_table = DataTableView(self)
        orderbook_table.setSortingEnabled(True)

        orderbook_model = OrderbookModel(self)
        orderbook_proxymodel = QSortFilterProxyModel(self)
        orderbook_proxymodel.setSourceModel(orderbook_model)
        orderbook_table.setModel(orderbook_proxymodel)

        orderbook_ws_client = WebsocketClient(self)
        orderbook_ws_client.data_changed.connect(
            orderbook_model.append_data)
        orderbook_ws_client.connectToHost(
            "wss://ws.bitmex.com/realtime?subscribe=orderBookL2")

        orderbook_vboxlayout = QVBoxLayout(self)
        orderbook_vboxlayout.addWidget(orderbook_label)
        orderbook_vboxlayout.addWidget(orderbook_table)

        orderbook_widget = QWidget(self)
        orderbook_widget.setLayout(orderbook_vboxlayout)

        central_hboxlayout = QHBoxLayout(self)
        central_hboxlayout.addWidget(instrument_widget)
        central_hboxlayout.addWidget(orderbook_widget)
        central_widget = QWidget(self)
        central_widget.setLayout(central_hboxlayout)

        self.setCentralWidget(central_widget)
