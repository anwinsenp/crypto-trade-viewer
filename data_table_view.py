from typing import Optional
from PyQt5.QtWidgets import QTableView, QWidget
from PyQt5.QtCore import QTimerEvent


class DataTableView(QTableView):
    def __init__(self, parent: Optional[QWidget] = ...) -> None:
        super().__init__(parent=parent)
        self.refresh_timer_id = self.startTimer(500)

    def timerEvent(self, event: QTimerEvent) -> None:
        if event.timerId() == self.refresh_timer_id:
            if self.model() != None:
                self.model().modelReset.emit()
        return super().timerEvent(event)
