import sys
from PySide6.QtWidgets import QApplication
from ExpandCollapsePanel import ExpandCollapsePanel

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = ExpandCollapsePanel()
    dialog.show()
    sys.exit(app.exec_())