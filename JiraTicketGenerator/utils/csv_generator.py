import csv
from PyQt5.QtWidgets import QFileDialog, QMainWindow

class CSVGenerator(QMainWindow):
    def __init__(self, content):
        super(CSVGenerator, self).__init__()
        self.content = content
        print(self.content)

    def writeCsv(self):
        path, _ = QFileDialog.getSaveFileName(self, 'Save File', "c:/Temp/export.csv", "CSV Files(*.csv *.txt)")
        if path:
            with open(path, 'w', newline='') as stream:
                print("saving", path)
                writer = csv.writer(stream, delimiter=',', quoting=csv.QUOTE_ALL)
                headers = []
                for column in range(self.content.columnCount()):
                    header = self.content.horizontalHeaderItem(column)
                    if header is not None:
                         headers.append(header.text())
                    else:
                        headers.append(str(column))
                writer.writerow(headers)
                for row in range(self.content.rowCount()):
                    rowdata = []
                    for column in range(self.content.columnCount()):
                        item = self.content.item(row, column)
                        if item is not None:
                            rowdata.append(item.text())
                        else:
                            rowdata.append('')
                    writer.writerow(rowdata)
