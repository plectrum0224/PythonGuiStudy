#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: phpergao
@license: Apache Licence 
@contact: endoffight@gmail.com
@site: http://
@software: PyCharm
@file: TestCode.py
@time: 2016/3/5 22:55
"""


# class A:
#     def __init__(self):
#         self.rates = {}
#         date = self.getdata()
#         rates = sorted(self.rates.keys())
#     def getdata(self):
#         pass
d = {}
with open("Components MW") as f:
    for line in f:
        key, value = line.rsplit(None, 1)
        d[key] = float(value)

print(d)