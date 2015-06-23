__author__ = 'sdeshpande'

import copy

parent = {"a":1, "b":[{"b1":1}], "d":[{"d1":1}]}
child = {"a": 0, "c":0, "b":0, "d":[{"d1":0}]}

temp = copy.deepcopy(child)
parent.update(temp)

print parent
