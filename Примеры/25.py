import sqlite3
import sys

from PyQt6.QtWidgets import (QWidget, QApplication, QTableWidgetItem,
                             QMessageBox)
from movies import Ui_Form

DATABASE_NAME = 'movies_db.db'


def connectDB():
    try:
        return sqlite3.connect(f'file:{DATABASE_NAME}?mode=rw', uri=True)
    except sqlite3.DatabaseError as e:
        print(f'{e.__class__.__name__}: {e}')
        sys.exit(-1)


class Window(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.con = connectDB()
        ...


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
