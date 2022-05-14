#
# Author: Julianne Murdock
#
# Date: May 14th 2022
#
# Purpose: Create a class that uses encapsulation.
#
#step 2 use a protected class
class Protected:
    def __init__(self):
        self._protectedVar = 24
#step 3 make a object that uses protected
obj = Protected ()
obj._protectedVar = 25 #what's better than 24?
print(obj._protectedVar)



class Protected:
    def __init__(self):
        #Step 1 use a private function
        self.__privateVar = 9000 #over 9000!
    def getPrivate(self):
        print(self.__privateVar)
    def setPrivate(self,private):
        self.__privateVar = private
#step three make an object that uses private
obj = Protected()
obj.getPrivate()
obj.setPrivate(16)
obj.getPrivate()