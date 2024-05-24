# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
import datetime

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(2, 0, 70, 40))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_1 = QtWidgets.QPushButton(Form)
        self.pushButton_1.setGeometry(QtCore.QRect(600, 0, 70, 40))
        self.pushButton_1.setObjectName("pushButton_1")
        self.tabWidget_2 = QtWidgets.QTabWidget(Form)
        self.tabWidget_2.setGeometry(QtCore.QRect(0, 40, 800, 550))
        self.tabWidget_2.setObjectName("tabWidget_2")

        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableWidget_16 = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_16.setGeometry(QtCore.QRect(0, 0, 800, 550))
        self.tableWidget_16.setObjectName("tableWidget_16")
        self.tableWidget_16.setColumnCount(31)  # Количество колонок
        self.tableWidget_16.setRowCount(15)    # Количество строк

        self.tabWidget_2.addTab(self.tab_2, "")

        self.retranslateUi(Form)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.createMenu()
        self.populate_table_with_combo_boxes()
        self.merge_cells()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Табель/Обеды"))
        self.pushButton.setText(_translate("Form", "Месяц"))
        self.pushButton_1.setText(_translate("Form", str(datetime.datetime.now().year)))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), _translate("Form", "График учета рабочего времени"))

    def createMenu(self):
        self.menu_Button = QtWidgets.QMenu()
        self.menu_Button_1 = QtWidgets.QMenu()
        years = ["2024", "2025"]
        months = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь",
                  "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]

        for month in months:
            action = QtWidgets.QAction(month, self.menu_Button)
            action.triggered.connect(partial(self.click_handler, item=month, item_type="month"))
            self.menu_Button.addAction(action)
        for year in years:
            action_1 = QtWidgets.QAction(year, self.menu_Button_1)
            action_1.triggered.connect(partial(self.click_handler, item=year, item_type="year"))
            self.menu_Button_1.addAction(action_1)

        self.pushButton.setMenu(self.menu_Button)
        self.pushButton_1.setMenu(self.menu_Button_1)

    def click_handler(self, item=None, item_type=None):
        if item_type == "month":
            self.pushButton.setText(item)
        elif item_type == "year":
            self.pushButton_1.setText(item)

    def populate_table_with_combo_boxes(self):
        options = ["Вариант 1", "Вариант 2", "Вариант 3"]  # Пример опций
        for row in range(self.tableWidget_16.rowCount()):
            for col in range(self.tableWidget_16.columnCount()):
                combo = QtWidgets.QComboBox()
                combo.addItems(options)
                self.tableWidget_16.setCellWidget(row, col, combo)

    def merge_cells(self):
        # Пример объединения ячеек: объединить ячейки с 1-й по 3-ю строку и с 1-го по 3-й столбец
        self.tableWidget_16.setSpan(1, 1, 3, 3)  # Объединяет ячейки от (1,1) до (3,3)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

