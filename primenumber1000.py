# -*- coding: utf-8 -*-
"""

This is a script to find prime numbers under 1000. 
"""

minIdx =1;
maxIdx =1001;
for i in range(minIdx,maxIdx):
    isPrime = True;
    for j in range(2,i):
            if (i % j == 0):
                isPrime = False;
                break
    if (isPrime == True):
        print i
