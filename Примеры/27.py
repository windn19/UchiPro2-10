class Window(QWidget, Ui_Form):
    def __init__(self):
        ...
        self.tableWidget.itemSelectionChanged.connect(self.showDetails)
        ...

    def showDetails(self):
        row = self.tableWidget.currentItem().row()
        title = self.tableWidget.item(row, 1).text()
        year = self.tableWidget.item(row, 2).text() or 0
        duration = self.tableWidget.item(row, 3).text() or 0
        director_id = self.tableWidget.item(row, 4).text()
        self.titleEdit.setText(title)
        self.yearSpinBox.setValue(int(year))
        self.durationSpinBox.setValue(int(duration))
        result = self.con.execute('''
            SELECT name
            FROM directors
            WHERE id = ?;
        ''', (director_id,)).fetchone()
        if result:
            self.directorComboBox.setCurrentText(result[0])
        else:
            self.directorComboBox.setCurrentText('')
