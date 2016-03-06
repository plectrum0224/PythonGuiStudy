#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: phpergao
@license: Apache Licence 
@contact: endoffight@gmail.com
@site: http://
@software: PyCharm
@file: SignalAndSlotEx.py
@time: 2016/3/6 16:29
"""
import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *



class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.yearsDict = {"1 years" : 1,
                 "2 years": 2,
                 "3 years" : 3,
                 "4 years": 4,
                 "5 years" : 5,
                 "6 years": 6,
                 "7 years" : 7,
                 "8 years": 8,
                 "9 years" : 9,
                 "10 years": 10,
                 }
        yearList = sorted(self.yearsDict.keys())
        principle = QLabel("Principal: ")
        rate = QLabel("Rate: ")
        years = QLabel("Years: ")
        amount = QLabel("Amount")

        self.principleSpin = QDoubleSpinBox()
        self.principleSpin.setRange(0.01, 1000000.00)
        self.principleSpin.setValue(0.00)
        self.principleSpin.setPrefix("$ ")
        self.rateSpin = QDoubleSpinBox()
        self.rateSpin.setRange(0.01, 1000000.00)
        self.rateSpin.setValue(0.00)
        self.rateSpin.setSuffix(" %")
        self.yearsBox = QComboBox()
        self.yearsBox.addItems(yearList)


        self.calLabel = QLabel("$ 0.00")


        grid = QGridLayout()
        grid.addWidget(principle, 0, 0)
        grid.addWidget(rate, 1, 0)
        grid.addWidget(years, 2, 0)
        grid.addWidget(amount, 3, 0)

        grid.addWidget(self.principleSpin, 0, 1)
        grid.addWidget(self.rateSpin, 1, 1)
        grid.addWidget(self.yearsBox, 2, 1)
        grid.addWidget(self.calLabel, 3, 1)

        self.setLayout(grid)
        self.setWindowTitle("Rate Calculate")

        self.connect(self.principleSpin, SIGNAL("valueChanged(double)"), self.updateUI)
        self.connect(self.rateSpin, SIGNAL("valueChanged(double)"), self.updateUI)
        self.connect(self.yearsBox, SIGNAL("currentIndexChanged(int)"), self.updateUI)

    def updateUI(self):
        principleValue = self.principleSpin.value()
        rateValue = self.rateSpin.value()
        yearValue = self.yearsDict[self.yearsBox.currentText()]

        amountValue = principleValue * ((1 + rateValue/100.0)** yearValue)

        self.calLabel.setText('$ ' + "%.2f" % amountValue)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    app.exec_()



