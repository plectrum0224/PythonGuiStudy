#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: phpergao
@license: Apache Licence 
@contact: endoffight@gmail.com
@site: http://
@software: PyCharm
@file: SignalAndSlot_002.py
@time: 2016/3/6 15:02
"""
from PyQt4.QtCore import *


class TaxRate(QObject):
    def __init__(self):
        super(TaxRate, self).__init__()
        self.__rate = 17.5

    def getRate(self):
        return self.__rate

    def setRate(self, rate):
        if rate != self.__rate:
            self.__rate = rate
            # self.emit(SIGNAL("rateChanged"), self.__rate)
            self.emit(SIGNAL("rateChanged(float)"), self.__rate)

def rateChanged(value):
    print("TaxRate changed to %.2f%%" % value)

vat = TaxRate()
vat.connect(vat, SIGNAL("rateChanged(float)"), rateChanged)
vat.setRate(16.5)
vat.setRate(8.5)
