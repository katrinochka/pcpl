#!/usr/bin/python
# -*- coding: cp1251 -*-

import unittest
from rk_1_refactored import *

# ������������ ������ ���������
class TestPark(unittest.TestCase):

    def test_park(self):
        park_ex = Park(1, '������������� ��������')
        self.assertEqual(park_ex.id, 1)
        self.assertEqual(park_ex.name, '������������� ��������')

# ������������ ������ ����������
class TestDriver(unittest.TestCase):

    def test_driver(self):
        driver_ex =  Driver(1, '������', 10000, 1)
        self.assertEqual(driver_ex.id, 1)
        self.assertEqual(driver_ex.fio, '������')
        self.assertEqual(driver_ex.sal, 10000)
        self.assertEqual(driver_ex.park_id, 1)

# ������������ ������ ��� ���������� ����� ������ �� ������
class TestDriver_Park(unittest.TestCase):

    def test_driver_park(self):
        driver_park_ex =  Driver_Park(1,1)
        self.assertEqual(driver_park_ex.driver_id, 1)
        self.assertEqual(driver_park_ex.park_id, 1)


class TestFunctions(unittest.TestCase):
    # ��������� ������
    def setUp(self):
        self.one_to_many, self.many_to_many = data()

    # ������������ ������� �1
    def test_task_1(self):
        result = task_1(self.one_to_many)
        self.assertEqual(result, [('������', 20000, '����������� ��������'), ('�������', 15000, '���������� ��������'), ('�������', 30000, '���������� ��������'),
                                  ('������', 10000, '������������� ��������'), ('��������', 25000, '������������� ��������')])

    # ������������ ������� �2
    def test_task_2(self):
        result = task_2(self.one_to_many)
        self.assertEqual(result, [('���������� ��������', 45000), ('������������� ��������', 35000), ('����������� ��������', 20000)])

    # ������������ ������� �3
    def test_task_3(self):
        word = '����������'
        result = task_3(self.many_to_many, word)
        self.assertEqual(result, {'���������� ��������': ['�������', '�������'], '���������� (������) ��������': ['������', '��������']})

if __name__ == '__main__':
    unittest.main()
