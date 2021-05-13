#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 13 01:27:20 2021

@author: anandamohonghosh
"""

from lib import A 

class B(A):
    def __init__(self, v):
        self.lvar = v
        pass
    
    def aSecFunc(self, pVal):
        print('Printing from Class B, vala ', pVal)
    
    def printFromLocal(self):
        print('Printing from local B, vala ', self.lvar)
        


objB = B("Mampi")
objB.printFromLocal()
objB.aFuncInA("Suji")
objB.aSecFunc("Ananda")
 
