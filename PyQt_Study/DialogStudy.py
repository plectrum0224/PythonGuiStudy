#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-03-08 12:28:39
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys


class PenPropertiesDlg(QDialog):

    def __init__(self, parent=None):
        super(PenPropertiesDlg, self).__init__(parent)
# =====================界面布局BEGIN==========================================#
        widthLabel           = QLabel("&Width")
        self.widthSpinBox    = QSpinBox()
        widthLabel.setBuddy(self.widthSpinBox)
        self.widthSpinBox.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.widthSpinBox.setRange(0, 24)
        self.beveledCheckBox = QCheckBox("&Beveled edges")
        styleLabel           = QLabel("&Style:")
        self.styleComboBox   = QComboBox()
        styleLabel.setBuddy(self.styleComboBox)
        self.styleComboBox.addItems(
        ["Solid", "Dashed", "Dotted", "DashDotted", "DashDotDotted"])
        okButton             = QPushButton("&OK")
        cancelButton         = QPushButton("Cancel")

        buttonLayout = QHBoxLayout()
        buttonLayout.addStretch()
        buttonLayout.addWidget(okButton)
        buttonLayout.addWidget(cancelButton)
        layout       = QGridLayout()
        layout.addWidget(widthLabel, 0, 0)
        layout.addWidget(self.widthSpinBox, 0, 1)
        layout.addWidget(self.beveledCheckBox, 0, 2)
        layout.addWidget(styleLabel, 1, 0)
        layout.addWidget(self.styleComboBox, 1, 1, 1, 2)
        layout.addLayout(buttonLayout, 2, 0, 1, 3)
        self.setLayout(layout)
# =====================界面布局 END===========================================#
#==========================连接signal and slot BEGIN=========================#
        self.connect(okButton, SIGNAL("clicked()"),
                     self, SLOT("accept()"))
        self.connect(cancelButton, SIGNAL("clicked()"),
                     self, SLOT("reject()"))
        self.setWindowTitle("Pen PenProperties")
#==========================连接signal and slot END=========================#


class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
#创建实例参数
        self.width        = 10
        self.beveled      = False
        self.style        = "Solid"
#界面布局BEGIN
        penButton         = QPushButton("Set Pen....Dumb Dialog Panel")
        self.label        = QLabel("The Pen has not been set")
        self.label.setTextFormat(Qt.RichText)
        layout            = QVBoxLayout()
        layout.addWidget(penButton)
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.setWindowTitle("Pen")
#界面布局END
#连接signal and slot BEGIN
        self.connect(penButton, SIGNAL("clicked()"),
        self.setPenProperties)
#连接signal and slot END
        self.updateData()

    def updateData(self):
        bevel = ""
        if self.beveled:
            bevel = "<br>Beveled"
        self.label.setText("Width = %d<br>Style = %s%s" %
                           (self.width, self.style, bevel))
#slot BEGIN
    def setPenProperties(self):
        dialog       = PenPropertiesDlg(self)
        dialog.widthSpinBox.setValue(self.width)
        dialog.beveledCheckBox.setChecked(self.beveled)
        dialog.styleComboBox.setCurrentIndex(
        dialog.styleComboBox.findText(self.style))
        if dialog.exec_():
#final value directly from the dialog's widget
            self.width   = dialog.widthSpinBox.value()
            self.beveled = dialog.beveledCheckBox.isChecked()
            self.style   = str(dialog.styleComboBox.currentText())
            self.updateData()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    app.exec_()
