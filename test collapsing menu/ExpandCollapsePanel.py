from PySide6 import QtWidgets
from PySide6.QtCore import QFile, QIODeviceBase, QTextStream
from PySide6.QtWidgets import QDialog
from Ui_main_window import Ui_Dialog

class ExpandCollapsePanel(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.collapse_expand_button.setProperty("state", "COLLAPSED")
        self.bottom_panel.setVisible(False)

        self.collapse_expand_button.clicked.connect(self.collapse_expand)

    def collapse_expand(self):
        old_state = self.collapse_expand_button.property("state")
        if old_state == "EXPANDED":
            self.collapse_expand_button.setProperty("state", "COLLAPSED")
        else:
            self.collapse_expand_button.setProperty("state", "EXPANDED")
        self.collapse_expand_button.style().polish(self.collapse_expand_button)
        self.bottom_panel.setVisible(old_state != "EXPANDED")

