#
# Author: Julianne Murdock
#
# Date: May 14th 2022
#
# Purpose: Create a class that uses encapsulation.
#

from abc import ABC, abstractmethod
class dress(ABC):
    def garmentReceipt(self, amount):
        print("Your total is: ", amount)
#This function passes intructions to the argument, but doesn't tell us how the data will be
        @abstractmethod
        def payment(self, amount):
            pass

class VisaPayment(dress):
    #this is where we implement the payment method type
    def payment(self, amount):
        print('Your purchase amount of {} is within youu $1,000,000.00 limit'.format(amount))

obj = VisaPayment()
obj.garmentReceipt('$24,000')
obj.payment('$24,000')