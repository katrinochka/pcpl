#!/usr/bin/python
# -*- coding: cp1251 -*-
class Unique:
    def __init__(self, data, **params):
        self.used_elements = set() 
        self.data = data
        self.index = 0
        if len(params)>0:
            for param,valueOfParam in params.items():
                self.register = valueOfParam
        else:
            self.register = False
        #Если True - игнорируем регистр, False - не игнорируем

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if self.index >= len(self.data):
                raise StopIteration
            else:
                current = self.data[self.index]      
                self.index = self.index + 1
                flag = str(current).isdigit()
                if self.register == True and flag == False:
                    if current not in self.used_elements and current.upper() not in self.used_elements and current.lower() not in self.used_elements:
                            self.used_elements.add(current)
                            return current
                else:
                    if current not in self.used_elements:
                        self.used_elements.add(current)
                        return current                    
if __name__ == '__main__':
    lst1 = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    lst2 = [1,3,2,3,2,1,4,3,3,3]
    lst3 = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B',1,3,2,3,2,1,4,3,3,3]
    for i in Unique(lst1, register=False):
        print(i) 
    print(' ')
    for i in Unique(lst1, register=True):
        print(i) 
    print(' ')
    for i in Unique(lst2):
        print(i) 
    print(' ')
    for i in Unique(lst3, register=False):
        print(i) 
    print(' ')
    for i in Unique(lst3, register=True):
        print(i) 
