from typing import (
    Optional,
    Any
)

from PyQt5.QtCore import (
    Qt,
    QAbstractTableModel,
    QObject,
    QModelIndex,
    QVariant
)

from collections import OrderedDict

from PyQt5.QtGui import QBrush


class DataModel(QAbstractTableModel):
    def __init__(self, parent: Optional[QObject] = ...) -> None:
        super().__init__(parent=parent)
        self.entries = OrderedDict()

    def rowCount(self, parent: QModelIndex = ...) -> int:
        return len(self.entries) if len(self.entries) > 0 else 0

    def columnCount(self, parent: QModelIndex = ...) -> int:
        return len(list(self.entries.values())[0]) - 2 if len(self.entries) > 0 else 0

    def data(self, index: QModelIndex, role: int = ...) -> Any:
        if len(self.entries) <= 0:
            return QVariant()

        row = index.row()
        col = index.column()
        if role == Qt.DisplayRole:
            return QVariant(list(self.entries.values())[row][col])

        if role == Qt.BackgroundRole:
            return QVariant(QBrush(list(self.entries.values())[row][self.columnCount()]))
        if role == Qt.ForegroundRole:
            return QVariant(QBrush(list(self.entries.values())[row][self.columnCount()+1]))

        return QVariant()
