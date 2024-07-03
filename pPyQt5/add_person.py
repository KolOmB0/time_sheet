from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import os
from window_person import DataEntryWindow_1
from Dismissal_transfer import Dismissal_transfer


class DataEntryWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.window_person = DataEntryWindow_1()
        self.window_person_1 = Dismissal_transfer()
        self.setObjectName("Form")
        self.resize(770, 725)
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(30, 30, 151, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(580, 30, 151, 31))
        self.pushButton_2.setObjectName("pushButton_2")

        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.setGeometry(QtCore.QRect(10, 70, 750, 600))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(self.window_person.number_of_lines())
        self.tableWidget.setColumnCount(4)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableWidget.setHorizontalHeaderLabels(("ФИО","Должность","Смена","Дата устройства на работу",))

        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(580, 680, 151, 31))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.pushButton.clicked.connect(self.open_window_person)
        self.iterate_over_cells()
        self.enable_sorting()
        self.pushButton_3.clicked.connect(self.open_wimdow_Dismissal_transfer)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Сотрудники"))
        self.pushButton.setText(_translate("Form", "Добавить сотрудника "))
        self.pushButton_2.setText(_translate("Form", "Отпуск"))
        self.pushButton_3.setText(_translate("Form", "Увольнение/Перевод"))

    def open_window_person(self):
        self.window_person.show()
        self.window_person.closeEvent = self.update_table
    def open_wimdow_Dismissal_transfer(self):
        self.window_person_1.show()

    def update_table(self, event):
        self.tableWidget.setRowCount(self.window_person.number_of_lines())
        self.iterate_over_cells()
        event.accept()

    def iterate_over_cells(self):
        self.tableWidget.clearContents()
        row = 0
        for Data in self.window_person.list_Data():
            col = 0
            for item in Data:
                table_item = QTableWidgetItem(item)
                table_item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable)
                self.tableWidget.setItem(row, col, table_item)
                col += 1
            row += 1

    def enable_sorting(self):
        self.tableWidget.setSortingEnabled(True)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = DataEntryWindow()
    ui.show()
    sys.exit(app.exec_())
