from typing import (
    Optional,
    Any
)
from PyQt5.QtCore import (
    QObject,
    Qt,
    QVariant
)
from data_model import DataModel
import json
from collections import OrderedDict

decoder = json.JSONDecoder(object_pairs_hook=OrderedDict)


class InstrumentModel(DataModel):
    def __init__(self, parent: Optional[QObject] = ...) -> None:
        super().__init__(parent=parent)

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...) -> Any:
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            if section == 0:
                return QVariant("Symbol")
            if section == 1:
                return QVariant("Price")
            if section == 2:
                return QVariant("Tick Direction")
            if section == 3:
                return QVariant("Timestamp")
            if section == 4:
                return QVariant("Change %")
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

        if action == 'update':
            symbol = data[0].get('symbol', None)
            last_price = data[0].get('lastPrice', None)
            last_tick_direction = data[0].get('lastTickDirection', None)
            timestamp = data[0].get('timestamp', None)
            last_change_pcnt = data[0].get('lastChangePcnt', None)

            if (symbol != None and
                    last_price != None and
                    last_tick_direction != None and
                    timestamp != None and
                    last_change_pcnt != None):
                fill_color = Qt.gray
                font_color = Qt.white

                if last_tick_direction.startswith("Minus"):
                    fill_color = Qt.red
                elif last_tick_direction.startswith("Plus"):
                    fill_color = Qt.green
                    font_color = Qt.black

                self.entries[symbol] = [
                    symbol,
                    last_price,
                    last_tick_direction,
                    timestamp,
                    last_change_pcnt,
                    fill_color,
                    font_color
                ]
                self.modelReset.emit()
