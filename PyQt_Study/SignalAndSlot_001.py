#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: phpergao
@license: Apache Licence 
@contact: endoffight@gmail.com
@site: http://
@software: PyCharm
@file: SignalAndSlot_001.py
@time: 2016/3/6 14:09
"""
import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *


class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        dial = QDial()
        dial.setNotchesVisible(True)

        spinBox = QSpinBox()
        zeroSpin = ZeroSpinBox()

        layout = QHBoxLayout()
        layout.addWidget(dial)
        layout.addWidget(spinBox)
        layout.addWidget(zeroSpin)
        self.setLayout(layout)

        self.connect(dial, SIGNAL("valueChanged(int)"),
                     spinBox.setValue)
        self.connect(spinBox,SIGNAL("valueChanged(int)"),
                     dial, SLOT("setValue(int)"))
        self.connect(zeroSpin,SIGNAL("atZero"),
                     self.announce)

        self.setWindowTitle("Signal and Slot")

    def announce(self, zeros):
        print("ZeroSpinBox has been at zero %d times" % zeros)

class ZeroSpinBox(QSpinBox):
    zeros = 0
    def __init__(self, parent=None):
        super(ZeroSpinBox, self).__init__(parent)
        self.connect(self, SIGNAL("valueChanged(int)"), self.checkZero)
    def checkZero(self):
        if self.value() == 0:
            self.zeros += 1
            self.emit(SIGNAL("atZero"), self.zeros)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    app.exec_()



