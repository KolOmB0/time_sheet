from PyQt5 import QtCore, QtGui, QtWidgets
import os

class DataEntryWindow_2(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("self")
        self.resize(528, 288)
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(100, 30, 411, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(10, 30, 81, 31))
        self.label.setMinimumSize(QtCore.QSize(0, 31))
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 81, 31))
        self.label_2.setMinimumSize(QtCore.QSize(0, 31))
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(False)
        self.label_2.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(10, 110, 81, 31))
        self.label_3.setMinimumSize(QtCore.QSize(0, 31))
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(False)
        self.label_3.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(90, 140, 151, 71))
        self.label_4.setMinimumSize(QtCore.QSize(0, 31))
        self.label_4.setScaledContents(False)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_4.setObjectName("label_4")

        self.dateEdit = QtWidgets.QDateEdit(self)
        self.dateEdit.setGeometry(QtCore.QRect(300, 160, 101, 31))
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDisplayFormat("dd.MM.yyyy")
        self.dateEdit.setDate(QtCore.QDate.currentDate())

        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(190, 220, 101, 41))
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.setGeometry(QtCore.QRect(100, 71, 411, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setCurrentIndex(0)
        self.comboBox.addItems(["Аппаратчик", "Мастер смены", "Мастер по сырью"])
        self.comboBox_2 = QtWidgets.QComboBox(self)
        self.comboBox_2.setGeometry(QtCore.QRect(100, 110, 411, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.setCurrentIndex(0)
        self.comboBox_2.addItems(["Пятидневка", "Cмена A", "Cмена B", "Cмена C", "Cмена D"])

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "Карточка сотрудника"))
        self.label.setText(_translate("self", "ФИО"))
        self.label_2.setText(_translate("self", "Должность"))
        self.label_3.setText(_translate("self", "Смена"))
        self.label_4.setText(_translate("self", "Дата устройства на работу   ( Первый рабочий день)"))
        self.pushButton.setText(_translate("self", "Сохранить"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    current = DataEntryWindow_2()
    current.show()
    sys.exit(app.exec_())