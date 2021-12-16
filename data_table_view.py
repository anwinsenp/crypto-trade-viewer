from typing import Optional
from PyQt5.QtWidgets import QTableView, QWidget


class DataTableView(QTableView):
    def __init__(self, parent: Optional[QWidget] = ...) -> None:
        super().__init__(parent=parent)
