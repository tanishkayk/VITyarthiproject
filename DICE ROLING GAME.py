#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 24 21:32:26 2025

@author: tyk
"""

import random 
 
while True:
    choice=input('Roll the dice? (yes/no): ').lower()
    if choice =='yes':
       die1 = random.randint(1,6)
       die2 = random.randint(1,6)
       print(f'({die1},{die2})')
    elif choice =='no':
     print('Thanks for Playing!')
     break
else:
    print("Invalid Choice")
    
    
    