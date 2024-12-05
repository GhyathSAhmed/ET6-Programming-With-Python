#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 5 Dec 2024

@author: Ghyath Ibarhim
"""


def add(first_num:int, second_num:int):
    """
    this function adds two numbers together
    
    parameters:
        a : int, the first number
        b : int, the second number
    
    returns -> int, the summation of the two numbers

        
    >>> add(2,2)
    4
    >>> add(205,195)
    400
    """
    # the the arguments must be integers
    assert isinstance(first_num, int),"the first argument is not integer"
    assert isinstance(second_num, int),"the second argument is not integer"
    
    return first_num + second_num
