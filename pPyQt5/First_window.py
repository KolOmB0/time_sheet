# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
import datetime


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(671, 575)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(2, 0, 70, 40))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_1 = QtWidgets.QPushButton(Form)
        self.pushButton_1.setGeometry(QtCore.QRect(600, 0, 70, 40))
        self.pushButton_1.setObjectName("pushButton_1")
        self.tabWidget_2 = QtWidgets.QTabWidget(Form)
        self.tabWidget_2.setGeometry(QtCore.QRect(0, 40, 671, 531))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget_3 = QtWidgets.QTabWidget(self.tab_2)
        self.tabWidget_3.setGeometry(QtCore.QRect(0, 0, 670, 510))
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab_23 = QtWidgets.QWidget()
        self.tab_23.setObjectName("tab_23")
        self.tableWidget_16 = QtWidgets.QTableWidget(self.tab_23)
        self.tableWidget_16.setGeometry(QtCore.QRect(0, 0, 670, 510))
        self.tableWidget_16.setObjectName("tableWidget_16")
        self.tableWidget_16.setColumnCount(0)
        self.tableWidget_16.setRowCount(0)
        self.tabWidget_3.addTab(self.tab_23, "")
        self.tab_24 = QtWidgets.QWidget()
        self.tab_24.setObjectName("tab_24")
        self.tableWidget_17 = QtWidgets.QTableWidget(self.tab_24)
        self.tableWidget_17.setGeometry(QtCore.QRect(0, 0, 670, 510))
        self.tableWidget_17.setObjectName("tableWidget_17")
        self.tableWidget_17.setColumnCount(0)
        self.tableWidget_17.setRowCount(0)
        self.tabWidget_3.addTab(self.tab_24, "")
        self.tab_25 = QtWidgets.QWidget()
        self.tab_25.setObjectName("tab_25")
        self.tableWidget_18 = QtWidgets.QTableWidget(self.tab_25)
        self.tableWidget_18.setGeometry(QtCore.QRect(0, 0, 670, 510))
        self.tableWidget_18.setObjectName("tableWidget_18")
        self.tableWidget_18.setColumnCount(0)
        self.tableWidget_18.setRowCount(0)
        self.tabWidget_3.addTab(self.tab_25, "")
        self.tabWidget_2.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget = QtWidgets.QTabWidget(self.tab_4)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 670, 510))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 670, 510))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tabWidget.addTab(self.tab, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_6)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 0, 670, 510))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget_3.setGeometry(QtCore.QRect(0, 0, 670, 510))
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(0)
        self.tableWidget_3.setRowCount(0)
        self.tabWidget.addTab(self.tab_3, "")
        self.tabWidget_2.addTab(self.tab_4, "")
        self.tab_17 = QtWidgets.QWidget()
        self.tab_17.setObjectName("tab_17")
        self.tabWidget_5 = QtWidgets.QTabWidget(self.tab_17)
        self.tabWidget_5.setGeometry(QtCore.QRect(0, 0, 670, 510))
        self.tabWidget_5.setObjectName("tabWidget_5")
        self.tab_26 = QtWidgets.QWidget()
        self.tab_26.setObjectName("tab_26")
        self.tableWidget_19 = QtWidgets.QTableWidget(self.tab_26)
        self.tableWidget_19.setGeometry(QtCore.QRect(0, 0, 670, 510))
        self.tableWidget_19.setObjectName("tableWidget_19")
        self.tableWidget_19.setColumnCount(0)
        self.tableWidget_19.setRowCount(0)
        self.tabWidget_5.addTab(self.tab_26, "")
        self.tab_27 = QtWidgets.QWidget()
        self.tab_27.setObjectName("tab_27")
        self.tableWidget_20 = QtWidgets.QTableWidget(self.tab_27)
        self.tableWidget_20.setGeometry(QtCore.QRect(0, 0, 670, 510))
        self.tableWidget_20.setObjectName("tableWidget_20")
        self.tableWidget_20.setColumnCount(0)
        self.tableWidget_20.setRowCount(0)
        self.tabWidget_5.addTab(self.tab_27, "")
        self.tab_28 = QtWidgets.QWidget()
        self.tab_28.setObjectName("tab_28")
        self.tableWidget_21 = QtWidgets.QTableWidget(self.tab_28)
        self.tableWidget_21.setGeometry(QtCore.QRect(0, 0, 670, 510))
        self.tableWidget_21.setObjectName("tableWidget_21")
        self.tableWidget_21.setColumnCount(0)
        self.tableWidget_21.setRowCount(0)
        self.tabWidget_5.addTab(self.tab_28, "")
        self.tabWidget_2.addTab(self.tab_17, "")
        self.tab_18 = QtWidgets.QWidget()
        self.tab_18.setObjectName("tab_18")
        self.tabWidget_6 = QtWidgets.QTabWidget(self.tab_18)
        self.tabWidget_6.setGeometry(QtCore.QRect(0, 0, 670, 510))
        self.tabWidget_6.setObjectName("tabWidget_6")
        self.tab_29 = QtWidgets.QWidget()
        self.tab_29.setObjectName("tab_29")
        self.tableWidget_22 = QtWidgets.QTableWidget(self.tab_29)
        self.tableWidget_22.setGeometry(QtCore.QRect(0, 0, 670, 510))
        self.tableWidget_22.setObjectName("tableWidget_22")
        self.tableWidget_22.setColumnCount(0)
        self.tableWidget_22.setRowCount(0)
        self.tabWidget_6.addTab(self.tab_29, "")
        self.tab_30 = QtWidgets.QWidget()
        self.tab_30.setObjectName("tab_30")
        self.tableWidget_23 = QtWidgets.QTableWidget(self.tab_30)
        self.tableWidget_23.setGeometry(QtCore.QRect(0, 0, 670, 510))
        self.tableWidget_23.setObjectName("tableWidget_23")
        self.tableWidget_23.setColumnCount(0)
        self.tableWidget_23.setRowCount(0)
        self.tabWidget_6.addTab(self.tab_30, "")
        self.tab_31 = QtWidgets.QWidget()
        self.tab_31.setObjectName("tab_31")
        self.tableWidget_24 = QtWidgets.QTableWidget(self.tab_31)
        self.tableWidget_24.setGeometry(QtCore.QRect(0, 0, 670, 510))
        self.tableWidget_24.setObjectName("tableWidget_24")
        self.tableWidget_24.setColumnCount(0)
        self.tableWidget_24.setRowCount(0)
        self.tabWidget_6.addTab(self.tab_31, "")
        self.tabWidget_2.addTab(self.tab_18, "")
        self.tab_19 = QtWidgets.QWidget()
        self.tab_19.setObjectName("tab_19")
        self.tabWidget_7 = QtWidgets.QTabWidget(self.tab_19)
        self.tabWidget_7.setGeometry(QtCore.QRect(0, 0, 670, 510))
        self.tabWidget_7.setObjectName("tabWidget_7")
        self.tab_32 = QtWidgets.QWidget()
        self.tab_32.setObjectName("tab_32")
        self.tableWidget_25 = QtWidgets.QTableWidget(self.tab_32)
        self.tableWidget_25.setGeometry(QtCore.QRect(0, 0, 670, 510))
        self.tableWidget_25.setObjectName("tableWidget_25")
        self.tableWidget_25.setColumnCount(0)
        self.tableWidget_25.setRowCount(0)
        self.tabWidget_7.addTab(self.tab_32, "")
        self.tab_33 = QtWidgets.QWidget()
        self.tab_33.setObjectName("tab_33")
        self.tableWidget_26 = QtWidgets.QTableWidget(self.tab_33)
        self.tableWidget_26.setGeometry(QtCore.QRect(0, 0, 670, 510))
        self.tableWidget_26.setObjectName("tableWidget_26")
        self.tableWidget_26.setColumnCount(0)
        self.tableWidget_26.setRowCount(0)
        self.tabWidget_7.addTab(self.tab_33, "")
        self.tab_34 = QtWidgets.QWidget()
        self.tab_34.setObjectName("tab_34")
        self.tableWidget_27 = QtWidgets.QTableWidget(self.tab_34)
        self.tableWidget_27.setGeometry(QtCore.QRect(0, 0, 670, 510))
        self.tableWidget_27.setObjectName("tableWidget_27")
        self.tableWidget_27.setColumnCount(0)
        self.tableWidget_27.setRowCount(0)
        self.tabWidget_7.addTab(self.tab_34, "")
        self.tabWidget_2.addTab(self.tab_19, "")
        self.tabWidget_2.raise_()
        self.pushButton.raise_()

        self.retranslateUi(Form)
        self.tabWidget_2.setCurrentIndex(4)
        self.tabWidget_3.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(2)
        self.tabWidget_5.setCurrentIndex(2)
        self.tabWidget_6.setCurrentIndex(2)
        self.tabWidget_7.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.createMenu()
        self.click_handler()

    # Rename attachment headers
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Табель/Обеды"))
        self.pushButton.setText(_translate("Form", "Месяц"))
        self.pushButton_1.setText(_translate("Form", str(datetime.datetime.now().year)))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_23), _translate("Form", "График учета рабочего времени "))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_24), _translate("Form", "График сменности"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_25), _translate("Form", "Обеды"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), _translate("Form", "Смена A"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "График учета рабочего времени "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("Form", "График сменности"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "Обеды"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("Form", "Смена B"))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_26), _translate("Form", "График учета рабочего времени "))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_27), _translate("Form", "График сменности"))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_28), _translate("Form", "Обеды"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_17), _translate("Form", "Смена C"))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_29), _translate("Form", "График учета рабочего времени "))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_30), _translate("Form", "График сменности"))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_31), _translate("Form", "Обеды"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_18), _translate("Form", "Смена D"))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tab_32), _translate("Form", "График учета рабочего времени "))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tab_33), _translate("Form", "График сменности"))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tab_34), _translate("Form", "Обеды"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_19), _translate("Form", "Пятидневка"))


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

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())