from typing import (
    Optional,
    Any
)
from PyQt5.QtCore import (
    QModelIndex,
    QObject,
    Qt,
    QVariant
)
from data_model import DataModel
import json
from collections import OrderedDict

decoder = json.JSONDecoder(object_pairs_hook=OrderedDict)


class OrderbookModel(DataModel):
    def __init__(self, parent: Optional[QObject] = ...) -> None:
        super().__init__(parent=parent)

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...) -> Any:
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            if section == 0:
                return QVariant("Symbol")
            if section == 1:
                return QVariant("ID")
            if section == 2:
                return QVariant("Side")
            if section == 3:
                return QVariant("Size")
            if section == 4:
                return QVariant("Price")
        return super().headerData(section, orientation, role)

    def append_data(self, text: str = ...) -> Any:
        entry = decoder.decode(text)
        if entry is None:
            return

        table = entry.get('table', None)
        action = entry.get('action', None)
        data = entry.get('data', None)

        if table is None or action is None or data is None:
            return

        if action == 'insert':
            symbol = data[0].get('symbol', None)
            id = data[0].get('id', None)
            side = data[0].get('side', None)
            size = data[0].get('size', None)
            price = data[0].get('price', None)

            if (symbol != None and
                    id != None and
                    side != None and
                    size != None and
                    price != None):
                fill_color = Qt.gray
                font_color = Qt.white

                if side.startswith("Sell"):
                    fill_color = Qt.red
                elif side.startswith("Buy"):
                    fill_color = Qt.green
                    font_color = Qt.black

                self.entries[symbol] = [
                    symbol,
                    id,
                    side,
                    size,
                    price,
                    fill_color,
                    font_color
                ]
