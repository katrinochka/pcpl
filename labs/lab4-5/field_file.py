#!/usr/bin/python
# -*- coding: cp1251 -*-

def field(goods,*args):
    fields = args
    for good in goods:
        result = dict([(field, good[field]) for field in fields if good.get(field) is not None])
        if any(result.values()):
            yield result

if __name__ == '__main__':
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'color': 'black'}
    ]

    for result in field(goods, "title"):
        print(result)
    print(" ")
    for result in field(goods, "title", "price"):
        print(result)
