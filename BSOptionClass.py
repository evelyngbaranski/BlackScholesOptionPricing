# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 11:12:19 2022

@author: evely
"""

####Evelyn Baranski
# 3/14/22

 #this file is creating an options class, with European call and put options subclasses

import math
from scipy.stats import norm

class BSOption:
    """creating the BSOption class"""
    
    def __init__(self, s, x, t, sigma, rf, div):
        """Here I am initializing the parameters of
        BSOption class
        
        s = current stock price
        x - option strike price
        t = option maturity in years
        sigma = annaulzied standard dev of returns
        rf = annualized risk free rate of return
        div = annaulized dividend rate, assuming cont. div rate"""
        
        
        #initializing all the parameters
        self.s = s
        self.x = x
        self.t = t
        self.sigma = sigma
        self.rf = rf
        self.div = div
        
    
    def __repr__(self):
        """this method creates a formatted string representation
        of BSOption"""
        
        #creating and returning s string
        s = f's = $ {self.s:.2f}, x = ${self.x:.2f}, t = \
{self.t:.2f} (years), sigma = {self.sigma:.3f}, rf = \
{self.rf:.3f}, div = {self.div:.3f}'
    
        return s
    
    #importing math
    import math
    
    def d1(self):
        """This method calculates and returns d1 of the option
        = (ln(S0 / X) + (r - sigma + 1/2 sd^2)*T) / sd * sqrt(T)"""
        
        
        #getting numerator of d1
        d1 = math.log(self.s / self.x) + ((self.rf \
                         - self.div + (.5 * self.sigma**2))  * self.t)
        
        
        #dividing by denom.
        d1 = d1 / (self.sigma * math.sqrt(self.t))
        
        return d1
    
    
        
    
    def d2(self):
        """This method calculates and returns d2 of the option
        = d1 - sd * sqrt(T)"""
        
        d2 = self.d1() - (self.sigma * math.sqrt(self.t))
        
        return d2
    
    
    
    
    
    def nd1(self):
        """This method returns the normal cumulative probability
        density of d1"""
        
        #returning norm cumulative prob
        nd1 = norm.cdf(self.d1())
        
        return nd1       
    
    
    
    def nd2(self):
        """This method returns the normal cumulative probability
        density of d2"""
        
        #returning norm cumulative prob
        nd2 = norm.cdf(self.d2())
        
        return nd2
    
    
    
    
    def value(self):
        """This method returns value of the BSOption. Cannot
        return at base class."""
        
        return 0
        print("Cannot calculate vaue for base class BSOption")
        
        
    
    def delta(self):
        """This method returns value of the BSOption. Cannot
        return at base class."""
        
        return 0
        print("Cannot calculate vaue for base class BSOption")


    
    
#Creating BSEuroCallOption class
class BSEuroCallOption(BSOption):
    """Creating European call option class within the
    BSOption class"""
    
        
    def __init__(self, s, x, t, sigma, rf, div):
        """Here I am initializing the parameters of
        BSEuroCallOption class overriding the original BSOption class"""
    
        #initializing all the parameters from previous Superclass
        super().__init__(s, x, t, sigma, rf, div)
    
    
    def __repr__(self):
        """this method creates a formatted string representation
        of BSOption"""
            
        #creating and returning s string for BSEuroCallOption
        s = f'BSOEuroCallOption, value = ${self.value():.2f} \n s = $ {self.s:.2f}, x = ${self.x:.2f}, t = \
{self.t:.2f} (years), sigma = {self.sigma:.3f}, rf = \
{self.rf:.3f}, div = {self.div:.3f}'
    
        return s
        
        
    def value(self):
        """This method returns value of the BSOption. Cannot
        return at base class."""
        
        #using math.e to calculate value    
        val = self.s * self.nd1() * math.e ** (- self.t * self.div)
        sub = (self.x * (math.e**(- self.rf * self.t)) * self.nd2()) 
        val = val - sub


        return val
    
    
    
    def delta(self):
        """This method is overriding the delta of the base class
        implementation. Delta used to to help with creating a 
        hedging portfolio. Option's delta = approx. the change in
        the value of the option for a $1 change in price in the
        underlying stock"""
        
        #delta value = e^(-t * div) *nd1
        ans = (math.e**(-self.t * self.div)) * (self.nd1())
        
        return ans    
    


    
#Creating BSEuroPutOption class as subclass of call option
class BSEuroPutOption(BSEuroCallOption):
    """creating put version of call option"""
    
    
    def __init__(self, s, x, t, sigma, rf, div):
        """Here I am initializing the parameters of
        BSEuroCallOption class overriding the original BSOption class"""
    
        #initializing all the parameters from previous Superclass
        super().__init__(s, x, t, sigma, rf, div)
        
    
    def value(self):
        """This method returns value of the BSOption. Cannot
        return at base class."""
     
        #using math.e to get put value        
        val = self.s * (1 -self.nd1()) * math.e ** (- self.t * self.div)
        p1 = (self.x * (math.e**(- self.rf * self.t)) * (1 -self.nd2()))
        val = p1 - val
        
        
        return val
    
    
    def __repr__(self):
        """this method creates a formatted string representation
        of BSOption"""
            
        #returning string representation
        s = f'BSOEuroPutOption, value = ${self.value():.2f} \n s = $ {self.s:.2f}, x = ${self.x:.2f}, t = \
{self.t:.2f} (years), sigma = {self.sigma:.3f}, rf = \
{self.rf:.3f}, div = {self.div:.3f}'

        return s
    
    
    def delta(self):
        """This method is overriding the delta of the base class
        implementation. Delta used to to help with creating a 
        hedging portfolio. Option's delta = approx. the change in
        the value of the option for a $1 change in price in the
        underlying stock"""
        
        # put delta = -e^(-t * div) * (-nd1)
        ans = (-math.e**(-self.t * self.div)) * (1 - self.nd1())
        
        return ans
        
        



if __name__ == '__main__':
    option = BSOption(100, 100, .25, .3, .06, 0)
    print(option)
    
    print(option.d1())
    print(option.d2())
    
    print(option.nd1())
    print(option.nd2())
    
    a = BSEuroCallOption(100, 100, 1, .3, .06, 0)
    print(a)
    
    put2 = BSEuroPutOption(100, 90, 1, .3, .06, 0)
    print("value should be $5.009", put2.value())
    
    put2 = BSEuroPutOption(90, 100, 1, .3, .06, .04)
    print("value should be 15.05", put2.value())
    
    
    put = BSEuroPutOption(100, 100, .5, .25, .04, .02)
    
    print(put)
    
    print(put.delta())
    
    call = BSEuroCallOption(100, 100, .5, .25, .04, .02)
    
    print(call.delta())
    
