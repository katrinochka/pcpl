#!/usr/bin/python
# -*- coding: cp1251 -*-

import json
import sys
from unique_file import Unique
from print_result import print_result
from cm_timer import cm_timer_1
from field_file import field
import random

def f1(arg):
    mas_1=[]
    mas_2=[]
    for result in field(arg, 'job-name'):
        mas_1.append(result['job-name'])
    for i in Unique(mas_1, register=True):
        mas_2.append(i)
    return sorted(mas_2)
        
def check(elem):
    if elem[:11].upper() == "ПРОГРАММИСТ":
        return True
    else:
        return False

def f2(arg):
   return list(filter(check, arg))

def add_stroka(elem):
    return str(elem+" с опытом python")

def f3(arg):
   return list(map(add_stroka, arg))

def add_stroka_1(elem):
    return str(elem+" , зарплата " + str(random.randint(100000,200000)) + " руб")

@print_result
def f4(arg):
   return list(map(add_stroka_1, arg))

 
with open("./data_light.json",encoding='utf-8') as f:
    data = json.load(f)
    with cm_timer_1():
        print("НАЧАЛО ЗАДАНИЕ 1")
        f1(data)
        print("КОНЕЦ ЗАДАНИЕ 1")
    print(" ")
    with cm_timer_1():
        print("НАЧАЛО ЗАДАНИЕ 2")
        f2(f1(data))
        print("КОНЕЦ ЗАДАНИЕ 2")
    print(" ")
    with cm_timer_1():
        print("НАЧАЛО ЗАДАНИЕ 3")
        f3(f2(f1(data)))
        print("КОНЕЦ ЗАДАНИЕ 3")
    with cm_timer_1():
        print("НАЧАЛО ЗАДАНИЕ 4")
        f4(f3(f2(f1(data))))
        print("КОНЕЦ ЗАДАНИЕ 4")