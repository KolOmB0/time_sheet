from PyQt5 import QtCore, QtGui, QtWidgets
from window_person import DataEntryWindow_1


class DataEntryWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("Form")
        self.resize(670, 725)
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(30, 30, 151, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(460, 30, 151, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.setGeometry(QtCore.QRect(10, 70, 651, 601))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(500, 680, 151, 31))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.window_person = DataEntryWindow_1()
        self.pushButton.clicked.connect(self.open_window_person)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Сотрудники"))
        self.pushButton.setText(_translate("Form", "Добавить сотрудника "))
        self.pushButton_2.setText(_translate("Form", "Отпуск"))
        self.pushButton_3.setText(_translate("Form", "Удалить сотрудника"))

    def open_window_person(self):
        self.window_person.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = DataEntryWindow()
    ui.show()
    sys.exit(app.exec_())