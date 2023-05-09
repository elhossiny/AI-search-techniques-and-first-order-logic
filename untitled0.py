# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 13:41:02 2021

@author: workstation
"""

import aima.utils
import aima.logic
from aima.utils import *
clauses = []
clauses.append(expr("Man(John)"))
clauses.append(expr("Women(Jia)"))
clauses.append(expr("Healthy(John)"))
clauses.append(expr("(Wealthy(x) & Healthy(x)) ==> Traveler(x)"))
clauses.append(expr("Wealthy(John)"))
clauses.append(expr("Healthy(Jia)"))



KB = aima.logic.FolKB(clauses)


Wealthy = aima.logic.fol_fc_ask(KB, aima.logic.expr('Wealthy(x)'))
Healthy = aima.logic.fol_fc_ask(KB, aima.logic.expr('Healthy(x)'))
Traveler = aima.logic.fol_fc_ask(KB, aima.logic.expr('Traveler(x)'))
# Print answers

print('\nWealthy?')
print(list(Wealthy))
print('\nHealthy?')
print(list(Healthy))
print('\nTraveler?')
print(list(Traveler))