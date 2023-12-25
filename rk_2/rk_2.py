#!/usr/bin/python
# -*- coding: cp1251 -*-

import unittest
from rk_1_refactored import *

# Тестирование класса «Автопарк»
class TestPark(unittest.TestCase):

    def test_park(self):
        park_ex = Park(1, 'Нижегородский автопарк')
        self.assertEqual(park_ex.id, 1)
        self.assertEqual(park_ex.name, 'Нижегородский автопарк')

# Тестирование класса «Водитель»
class TestDriver(unittest.TestCase):

    def test_driver(self):
        driver_ex =  Driver(1, 'Петров', 10000, 1)
        self.assertEqual(driver_ex.id, 1)
        self.assertEqual(driver_ex.fio, 'Петров')
        self.assertEqual(driver_ex.sal, 10000)
        self.assertEqual(driver_ex.park_id, 1)

# Тестирование класса для реализация связи многие ко многим
class TestDriver_Park(unittest.TestCase):

    def test_driver_park(self):
        driver_park_ex =  Driver_Park(1,1)
        self.assertEqual(driver_park_ex.driver_id, 1)
        self.assertEqual(driver_park_ex.park_id, 1)


class TestFunctions(unittest.TestCase):
    # Генерация данных
    def setUp(self):
        self.one_to_many, self.many_to_many = data()

    # Тестирование задания №1
    def test_task_1(self):
        result = task_1(self.one_to_many)
        self.assertEqual(result, [('Иванов', 20000, 'Костромской автопарк'), ('Сидоров', 15000, 'Московский автопарк'), ('Больков', 30000, 'Московский автопарк'),
                                  ('Петров', 10000, 'Нижегородский автопарк'), ('Абакумов', 25000, 'Нижегородский автопарк')])

    # Тестирование задания №2
    def test_task_2(self):
        result = task_2(self.one_to_many)
        self.assertEqual(result, [('Московский автопарк', 45000), ('Нижегородский автопарк', 35000), ('Костромской автопарк', 20000)])

    # Тестирование задания №3
    def test_task_3(self):
        word = 'Московский'
        result = task_3(self.many_to_many, word)
        self.assertEqual(result, {'Московский автопарк': ['Сидоров', 'Больков'], 'Московский (другой) автопарк': ['Петров', 'Абакумов']})

if __name__ == '__main__':
    unittest.main()
