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
    if elem[:11].upper() == "�����������":
        return True
    else:
        return False

def f2(arg):
   return list(filter(check, arg))

def add_stroka(elem):
    return str(elem+" � ������ python")

def f3(arg):
   return list(map(add_stroka, arg))

def add_stroka_1(elem):
    return str(elem+" , �������� " + str(random.randint(100000,200000)) + " ���")

@print_result
def f4(arg):
   return list(map(add_stroka_1, arg))

 
with open("./data_light.json",encoding='utf-8') as f:
    data = json.load(f)
    with cm_timer_1():
        print("������ ������� 1")
        f1(data)
        print("����� ������� 1")
    print(" ")
    with cm_timer_1():
        print("������ ������� 2")
        f2(f1(data))
        print("����� ������� 2")
    print(" ")
    with cm_timer_1():
        print("������ ������� 3")
        f3(f2(f1(data)))
        print("����� ������� 3")
    with cm_timer_1():
        print("������ ������� 4")
        f4(f3(f2(f1(data))))
        print("����� ������� 4")