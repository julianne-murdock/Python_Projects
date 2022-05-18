#
# Author: Julianne Murdock
#
# Date: May 13th 2022
#
# Purpose: Create two classes that inherit from a another class
#

class Art_World:
    username = 'rising.horizons'
    artist = 'Julianne Murdock'
    password = '12345678910hackme'

    def getArtWorldLogin(self):
        login_name = input('Enter your Art World Username')
        login_password = input('Enter your Art World Password ')
        if (login_name == self.username and login_password == self.password):
            print("Welcome, {} to Art World! I can't wait to see what you create!".format(self.artist))
        else:
            print('A wrong Name or Password was entered. Please try again.')
#child class for Art Gallery
class art_gallery(Art_World):
    experience = 'Sponge Paintings with Jellyfish Jelly'
    name = 'Spongebob Squarepants'
    password = 'jellyfish'
    username = 'spongey'
    expected_Graduation = 'Unknown, Student for 20 years'
    student_ID = '15963'

    #this will use the same method from Art_World class but using the login_ID
    def getArtWorldLogin(self):
         login_name = input('Enter your Art Gallery Username')
         login_password = input('Enter your Art Gallery Password:  ')
         login_ID = input('Enter your Student ID: ')
         if (login_name == self.username and login_ID == self.student.ID and login_password == self.password):
             print("Welcome back to Art World, {}. I can't wait to see the new things you create today!".format(self.name))


#second child class for Art Club
class Art_Club(Art_World):
    monthly_fee = 5.00 #footlong
    music_of_the_day = 'ghostbusters'
    art_challenge = 'Not Sponge Paintings'

    def getArtWorldLogin(self):
         login_name = input('Enter your Art Gallery Username')
         login_password = input('Enter your Art Gallery Password:  ')
         login_ID = input('Enter your Student ID: ')
         if (login_name == self.username and login_ID == self.student.ID and login_password == self.password):
             print("Welcome back to Art Club, {}. It is time to take on the challenge of the day!".format(self.name))


artNow = Art_World()
artNow.getArtWorldLogin()










