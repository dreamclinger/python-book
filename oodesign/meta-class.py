#!/usr/local/bin/env python
# Create: dreamclinger@gmail.com, 2014/12/08
# Cited from: https://github.com/michaelliao
# Metaclass is the template of class

class ListMetaclass(type): ## meta-class must be derived from class type
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value) ## lambda 
        return type.__new__(cls, name, bases, attrs) ## base ?

class MyList(list):
    __metaclass__ = ListMetaclass

if __name__ == '__main__':
    L = MyList()
    L.add(1)
    print L
