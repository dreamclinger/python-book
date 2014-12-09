#!/usr/local/bin/env python
# Create: dreamclinger@gmail.com, 2014/12/08
# Cited from: https://github.com/michaelliao
# Class's attribution can be overrided.
# More details: http://igorsobreira.com/2010/09/16/difference-between-one-underline-and-two-underlines-in-python.html

class Custom(object):
    def __init__(self, n):
        self.n = n
    def __add__(self, other):  ## override
        return self.n - other
    def __printnum(self):   ## private
        return self.n
    def shownum(self):
        return self.__printnum()   ## public, call private

if __name__ == '__main__':
    num = Custom(10)
    print 'show num:', num.shownum()
    print 'override num + 3, (which is redefined as minus), so now results is',num + 3
