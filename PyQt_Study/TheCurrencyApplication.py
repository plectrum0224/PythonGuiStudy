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
        self.rates = {}
        # date rates dateLabel不是类的实例变量，所以不能使用类的实例去引用它们
        super(Form, self).__init__(parent)
        # this method gets the exchange rates, populates the self.rates dictionary
        # returns a string holding the date the rates were in force
        date = self.getdata()
        # self.rates is dictionary, The dictionary’s keys are currency names,
        # and the values are the conversion factors
        # self.rate.keys()返回字典的键列表，然后使用sorted对其排序，rates是一个排序的键列表
        rates = sorted(self.rates.keys())
        dateLabel = QLabel(date)
        # begin
        # 创建两个ComboBox，from和to，分别放置rates列表
        self.fromComboBox = QComboBox()
        self.fromComboBox.addItems(rates)
        self.toComboBox = QComboBox()
        self.toComboBox.addItems(rates)
        # end
        # begin
        # 创建一个SpinBox控件，分别设置最小值、最大值、初始值
        self.fromSpinBox = QDoubleSpinBox()
        self.fromSpinBox.setRange(0.01, 10000000.00)
        self.fromSpinBox.setValue(1.00)
        # end
        self.toLabel = QLabel("1.00")
        # layout
        # dateLabel (0, 0)        |
        # self.fromComboBox (1, 0)|self.fromSpinBox (1, 1)
        # self.toComboBox (2, 0)  |self.toLabel (2, 1)
        grid = QGridLayout()
        grid.addWidget(dateLabel, 0, 0)
        grid.addWidget(self.fromComboBox, 1, 0)
        grid.addWidget(self.fromSpinBox, 1, 1)
        grid.addWidget(self.toComboBox, 2, 0)
        grid.addWidget(self.toLabel, 2, 1)
        self.setLayout(grid)
        # setup behavior
        self.connect(self.fromComboBox, SIGNAL("currentIndexChanged(int)"), self.updateUi)
        self.connect(self.toComboBox, SIGNAL("currentIndexChanged(int)"), self.updateUi)
        self.connect(self.fromSpinBox, SIGNAL("valueChanged(double)"), self.updateUi)
        self.setWindowTitle("Currency")

    def updateUi(self):
        to = str(self.toComboBox.currentText())
        from_ = str(self.fromComboBox.currentText())
        amount = (self.rates[from_] / self.rates[to]) * self.fromSpinBox.value()
        self.toLabel.setText("%0.2f" % amount)

    def getdata(self):
        try:
            date = "Unknown"
            fh = urllib.request.urlopen("http://www.bankofcanada.ca/stats/assets/csv/fx-seven-day.csv")
            for item in fh:
                line = item.decode()
                if not line or line.startswith("#"):
                    continue
                # 返回分割后的字符串列表
                fields = line.split(",")
                if line.startswith("Date "):
                    date = fields[-1]
                else:
                    try:
                        value = float(fields[-1])
                        self.rates[str(fields[0])] = value
                    except ValueError:
                        pass
            return "Exchange Rates Date: " + date
        except Exception as e:
            return "Failed to download:\n%s" % e


app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()







