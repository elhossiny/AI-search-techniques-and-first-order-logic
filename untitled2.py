# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 14:21:35 2022

@author: workstation
"""

from logic2 import *
carrots = Symbol("carrots")
orange = Symbol("orange")
knowledge = And(
 Implication(carrots,orange),
)
print(knowledge.formula())

#the English mean is [carrots color is orange]
#-------------------------------------------------------------------------------------------
from logic import *
person = Symbol("person")
vegetarian = Symbol("vegetarian(x)")
like = Symbol("like")
like_person_carrots = Symbol("like(x, carrots)")
knowledge_for_question2 = And(Implication(vegetarian, like_person_carrots))
print(knowledge_for_question2.formula())  
print(model_check(knowledge, carrots))
print(knowledge.formula())

#the English mean is [person likes carrot then if person is vegetarian]
#-------------------------------------------------------------------------------------------
from logic import *
pass_exam = Symbol("pass(x)")
study_hard = Symbol("study_hard(x)")
knowledge_for_question3 = Implication(study_hard, pass_exam)
print(knowledge_for_question3.formula())  

#the English mean is [if student study hard then he will pass]
#-------------------------------------------------------------------------------------------

from logic2 import *
print(model_check(knowledge_for_question3, pass_exam))

# in English : " who will pass? "
Pass = Symbol("? pass(who)")
knowledge_for_question4 = And(Pass)
print(knowledge_for_question4.formula()) 
#---------------------------------------------------
from logic import *
teaches = Symbol("? teaches(course, which)")
knowledge_for_question5 = And(teaches)
print(knowledge_for_question5.formula())  

#the English mean is [who will pass?]
#-------------------------------------------------------------------------------------------
x = Symbol("x")
y = Symbol("y")
enemies = Symbol(f"enemies({x}, {y})")
hates = Symbol(f"hates({x}, {y})")
fight = Symbol(f"fight({x}, {y})")
knowledge_for_question6 = And(Implication(enemies, And(hates, fight)))
print(knowledge_for_question6.formula())
#the English mean is [which course professor teachecs?]
#-------------------------------------------------------------------------------------------

#the English mean is [if x and y are enemies then x hates y then y,x fight]
#-------------------------------------------------------------------------------------------

from logic2 import *
# in English : " if x & y are enemies, x hate y and x fight y "
x = Symbol("x")
y = Symbol("y")
enemies = Symbol(f"enemies({x}, {y})")
hates = Symbol(f"hates({x}, {y})")
fight = Symbol(f"fight({x}, {y})")
knowledge_for_question6 = And(Implication(enemies, And(hates, fight)))
print(knowledge_for_question6.formula())
#print the output formula of knowledge base
#-------------------------------------------------------------------------------------------

from utils import *
from logic2 import *
#  read(maria, logic programming book) ==> by(peter lucas)
maria = Symbol("maria")
peter_lucas = Symbol("peter lucas")
read = Symbol(f" read ({maria}, logic programming book)")
by = Symbol(f"by ({peter_lucas})")
knowledge_for_question1 = And(Implication(read, by))
print(knowledge_for_question1.formula())
#-------------------------------------------------------------------------------------------

from utils import *
from logic2 import *
# is_girl(x) ==> like(x, shopping)
is_girl = Symbol("is_girl(x)")
shopping = Symbol("shopping")
like = Symbol(f"like(x, {shopping} )")
knowledge_for_question2 = And(Implication(is_girl, like))
print(knowledge_for_question2.formula())
#-------------------------------------------------------------------------------------------

from utils import *
from logic2 import *
# ? likes( x , shopping)
who = Symbol("?")
knowledge_for_question3  = And(who ,like)
print(knowledge_for_question3.formula())
#-------------------------------------------------------------------------------------------

# city( x ,big , crowdy) ==> hates(kirke, x)
city = Symbol("city(x, big, crowdy)")
hates = Symbol("kirke, x")
knowledge_for_question4 = And(Implication(city, hates))
print(knowledge_for_question4.formula())
#-------------------------------------------------------------------------------------------

from utils import *
from logic2 import *
x = Symbol("x")
y = Symbol("y")
enemies = Symbol(f"enemies({x}, {y})")
hates1 = Symbol(f"hates({x}, {y})")
hates2 = Symbol(f"hates({y}, {x})")
knowledge_for_question1 = And(Implication(enemies, And(hates1, hates2)))
# print(knowledge_for_question1.formula())

#------------------------------------------------------------------------
p = Symbol("p(x)")
q = Symbol("q(x)")
r = Symbol("r(x)")
knowledge_for_question2 = And(Implication(p , And(q, r)))
# print(knowledge_for_question2.formula())
#-------------------------------------------------------------------------------------------

import utils
from logic import *
clauses = [expr("Man(John)"), expr("Women(Jia)"), expr("Healthy(John)"), expr("Wealthy(John)"), expr("Wealthy(Jia)")
    ,expr("(Wealthy(x) & Healthy(x)) ==> Traveler(x)")]

KB = FolKB(clauses)
wealthy = fol_bc_ask(KB, expr("Wealthy(x)"))
healthy = fol_bc_ask(KB, expr("Healthy(x)"))
traveler = fol_bc_ask(KB, expr("Traveler(x)"))
print('Who are healthy ?')
print(list(healthy), '\n')
print('Who are wealthy ?')
print(list(wealthy), '\n')
print('Who can travel ?')
print(list(traveler))
#-------------------------------------------------------------------------------------------

