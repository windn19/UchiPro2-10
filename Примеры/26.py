class Window(QWidget, Ui_Form):
    def __init__(self):
        ...
        self.showMovies()
        self.showDirectors()
        ...

    def showMovies(self):
        result = self.con.execute('''
            SELECT *
            FROM movies
        ''').fetchall()
        self.tableWidget.setColumnCount(len(result[0]))
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setHorizontalHeaderLabels(
            ['ID', 'Название', 'Год', 'Длительность', 'ID режиссера'])
        for i, row in enumerate(result):
            for j, elem in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(
                    str(elem) if elem else '')
                                         )
        self.tableWidget.resizeColumnsToContents()

    def showDirectors(self):
        result = self.con.execute('''
            SELECT *
            FROM directors
        ''').fetchall()
        self.directorComboBox.addItems(
            [None] + [row[1] for row in result])
