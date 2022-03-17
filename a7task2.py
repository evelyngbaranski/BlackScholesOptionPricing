# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 13:21:48 2022

@author: evely
"""

####Evelyn Baranski
# 3/14/22
#assingment 7: Black Scholes Options

 #this file, assignment 7 task 2 is creating client applications
 #using black scholes
 


#importing everything from task1
from a7task1 import *



#Function 1'
def generate_option_value_table(s, x, t, sigma, rf, div):
    """This function is not a class method. This function will
    generate  printout illustrating the change in option prices
    with respect to the change in the underlying stock price.
    Will require all parameters from BSOption class.
    
    Creates two option objects call and put. Inside function
    there is a loop iterating over a range of possible prices
    at each price changing the objects stock price and using 
    methods to obtain option's value and delta"""
    
    
    #creating variables for call and put
    call = BSEuroCallOption(s, x, t, sigma, rf, div)
    put = BSEuroPutOption(s, x, t, sigma, rf, div)
    
    print(call)
    print(put)
    
    
    #Printing title for table
    print()
    print("Change in option values with w.r.t change in stock price: ")
    
    
    #variables to have columns lined up with headers
    one = "price"
    two = "call value"
    three = "put value"
    four = "call delta"
    five = "put delta"
    
    print(f"{one:^12} {two:^15} {three:^15} {four:^15} {five:^15}")
    
    #for loop to iterate through
    for x in range(s - 10, s + 11):
        
        #changing the call and put price to value of x
        call.s = x
        put.s = x
        
        
        #variables to print column
        price = f"{x:.2f}"
        cv = f"{call.value():.4f}"
        pv = f"{put.value():.4f}"
        dc = f"{call.delta():.4f}"
        dp = f"{put.delta():.4f}"
        
        dollar = "$"
        
        
        
        print(f"{dollar:<4} {price:<11} {cv:<15} {pv:<15} {dc:<15} {dp:<15}")
    
    



#Function 2:
def calculate_implied_volatility(option, value):
    """This client function calculates the implied volatility
    of an observed option. This function will iterate through
    and change the option's sigma until the option's value is 
    close enough to the observed price using an acceptable margin
    of error"""
    
    #creating acceptable margin of error
    error = .0001
    
    
    #variables upper and lower bound and creating sigma value
    upperb = 1
    lowerb = 0
    
    
    sig = .5
    option.sigma = sig
    
    
    
    #indefenite loop to iterate through
    while True:
        
        #case that absolute dif. between values less than error
        if abs(option.value() - value) <= error:
            
            #returning value and breaking
            return sig
            break
            
        
        
        #scenario that option value greater than inputed
        elif option.value() > value:
            
            #changing up bound to current sigma
            upperb = sig
            
            #changing sigma to average of upper bound and lower
            sig = (upperb + lowerb) / 2
            option.sigma = sig
        
        
        #scenario that option value less than inputed
        elif option.value() < value:
            
            #changing lower bound to sigma
            lowerb = sig 
            
            #new sigma = average upper and lower bound
            sig = (upperb + lowerb) / 2
            option.sigma = sig
    
            
        
        


    
    
    
    
if __name__ == '__main__':
    generate_option_value_table(100, 100, .5, .25, .04, .02)
    
    option = BSEuroCallOption(92.76, 90, 100/365, .5, 0.01, 0)
    print(calculate_implied_volatility(option, 7.4))
    
    