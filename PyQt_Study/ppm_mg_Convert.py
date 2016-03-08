#!/usr/bin/env python
# encoding: utf-8


"""
@version: 1.00
@author: phpergao
@license: Apache Licence
@contact: endoffight@gmail.com
@site: http://
@software: PyCharm
@file: TheCurrencyApplication.py
@time: 2016/3/5 19:37
"""
import sys
import urllib.request
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.components = {}
        self.components = self.getData()
        titleLabel = QLabel("ppm and mg/m3 单位转换")
        componentsList = sorted(self.components.keys())
        self.componComboBox = QComboBox()
        self.componComboBox.addItems(componentsList)
        self.componSpinBox = QDoubleSpinBox()
        self.componSpinBox.setRange(0.01, 10000000.00)
        self.componSpinBox.setValue(1.00)
        self.calLabel = QLabel("0.00")

        grid = QGridLayout()
        grid.addWidget(titleLabel, 0, 0)
        grid.addWidget(self.componComboBox, 1, 0)
        grid.addWidget(self.componSpinBox, 1, 1)
        grid.addWidget(self.calLabel, 2, 1)
        self.setLayout(grid)
        # setup behavior
        self.connect(self.componComboBox, SIGNAL("currentIndexChanged(int)"), self.updateUi)
        self.connect(self.componSpinBox, SIGNAL("valueChanged(double)"), self.updateUi)
        self.setWindowTitle("ppm and mg/m3 unitConvert")

    def updateUi(self):
        MW = str(self.componComboBox.currentText())
        amount = (self.components[MW] / 22.4) * self.componSpinBox.value()
        self.calLabel.setText("%0.2f" % amount)

    def getData(self):
        with open("Components MW") as f:
            for line in f:
                key, value = line.rsplit(None, 1)
                self.components[key] = float(value)
        return self.components

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()







