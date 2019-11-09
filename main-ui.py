# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main-ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(575, 322)
        Form.setMinimumSize(QtCore.QSize(575, 322))
        Form.setMaximumSize(QtCore.QSize(575, 322))
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(521, 292, 31, 20))
        self.pushButton_5.setStyleSheet(".QPushButton {\n"
"background-color:red;\n"
"color: white;\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(11, 21, 251, 41))
        self.label_3.setObjectName("label_3")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(261, 11, 20, 351))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(290, 20, 271, 265))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.textEdit = QtWidgets.QTextEdit(self.verticalLayoutWidget_2)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_2.addWidget(self.textEdit)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.textEdit_2 = QtWidgets.QTextEdit(self.verticalLayoutWidget_2)
        self.textEdit_2.setObjectName("textEdit_2")
        self.verticalLayout_2.addWidget(self.textEdit_2)
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(-69, 1, 811, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 300, 131, 16))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(30, 150, 211, 51))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("HTTP-Scanner", "HTTP-Scanner"))
        self.pushButton_5.setText(_translate("Form", "C"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Статус-сканер</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p>Введите http сслыку.</p></body></html>"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">Вывод</span></p></body></html>"))
        self.label_4.setText(_translate("Form", "by сссайнт лох, 2019"))
        self.pushButton.setText(_translate("Form", "Просканировать"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
