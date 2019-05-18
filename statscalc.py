# -*- coding: utf-8 -*-
"""
Created on Sat May  4 15:03:50 2019

@author: Winchester
"""

class Stats:
    """
    Calculate means and variances
    """
    
    def __init__(self,x,y):
        """
        This is a constructor
        """
        self.mn = 0
        
    def calc_mean(self,arr):
        """
        Calculate mean.
        
        Input:
            arr: list of int or float
        Output:
            mn: float
        """
        for elem in arr:
            self.mn += elem
        self.mn = self.mn/len(arr)
        return self.mn
        
    def calc_std(self,arr):
        """
        Calculate std.
        
        Input:
            arr: list of int or float
        Output:
            sd: float
        """
        sd = 0
        self.mn = self.calc_mean(arr)
        for elem in arr:
            sd += (elem-self.mn)**2
        sd = (sd/len(arr))**0.5
        return sd
    
stats_obj = Stats(3,4)
print(stats_obj.calc_std([2,3,4]))

            
        
        