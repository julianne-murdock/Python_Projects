#
# Author: Julianne Murdock
#
# Date: May 13th 2022
#
# Purpose: Create two classes that inherit from a another class
#

class Art_World:
    Instagram_username = 'rising.horizons'
    Artist = 'Julianne Murdock'
    Password = '12345678910hackme'

    def getArtWorldLogin(self):
        login_name = input('Enter your First and Last name here ')
        login_password = input('Enter your Art World Password ')
        if (login_name == self.name and login_password == self.password):
            print("Welcome, {} to Art World! I can't wait to see what you create!".format(entry_name))
        else:
            print('A wrong Name or Password was entered. Please try again.')
#child class for Art Gallery
class Art_Gallery(Art_World):
    Experience = 'Sponge Paintings with Jellyfish Jelly'
    name = 'Spongebob Squarepants'
    Expected_Graduation = 'Unknown, Student for 20 years'
    Student_ID = '15963'

    #this will use the same method from the prior parent class but using the entry pin
    def getArtWorldLogin(self):
         login_name = input('Enter your First and Last name here:   ')
         login_password = input('Enter your Art World Password:  ')
         login_ID = input('Enter your Student ID: ')
         if (login_name == self.name and _pin == self.login_ID):
             print("Welcome back to Art World, {}. I can't wait to see the new things you create today!".format(entry_name))


#second child class for Art Club
class Art_Club(Art_World):
    monthly_fee = 5.00 #footlong
    music_of_the_day = 'ghostbusters'
    Art_Challenge = 'Not Sponge Paintings'

    def getArtWorldLogin(self):
         login_name = input('Enter your First and Last name here:   ')
         login_password = input('Enter your Art World Password:  ')
         login_ID = input('Enter your Student ID: ')
         if (login_name == self.name and _pin == self.login_ID):
             print("Welcome back to Art Club, {}. It is time to take on the challenge of the day!".format(entry_name))


Art_Club = Art_World()
Art_Club.getArtWorldLogin










