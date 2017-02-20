#Lesson 5
#By Brian Lundell

#-----------------------------------IMPORTING-------------------------------------
#Importing other files from the same directory is simple
import moretest
#now you have access to all functions and variables
#they are opened using dot notation
moretest.apple()

print moretest.moretestVar

#Class example

#The items passes to the song are the lyrics
#The lyrics is initialized to the class by self.lyrics = lyrics
#self is the variable for the instance being called inside the class
#This essentially means self assigns the objects onto the class objects
class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

#passing self in these function will assign this function to the class
    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

#This will create the class X that inherits properties from Song
class X(Song):
