
from gtts import gTTS
import os
import winsound
import platform
winsound.PlaySound(r"welc.wav", winsound.SND_ASYNC)
winsound.PlaySound( None, winsound.SND_ASYNC)
winsound.PlaySound(r"name.wav", winsound.SND_ASYNC)
winsound.PlaySound( None, winsound.SND_ASYNC)
Name = input("Enter your Name:")
winsound.PlaySound(r"color.wav", winsound.SND_ASYNC)
winsound.PlaySound( None, winsound.SND_ASYNC)
Color = input("Enter your Favorite Color: ")
winsound.PlaySound(r"inter.wav", winsound.SND_ASYNC)
winsound.PlaySound( None, winsound.SND_ASYNC)
Interest = input("What do you like:  ")
x = "Hey" + Name + "How's your day?"
tts = gTTS(text="x", lang='en')
tts.save("n.wav")         #creates a file named n.wav
winsound.Playsound( r'n.wav' , winsound.SND_ASYNC) #plays n.wav
winsound.Playsound( None, winsound.SND_ASYNC)
answer = input("good or bad: ")

if (answer == "good"):
	print("Awesome", Name,"Enjoy the rest of it!")
if (answer == "Bad"):
	print("Sorry", Name,"Lets hope it will get better!")
if (answer == "bad"):
	print("Sorry", Name,"Lets hope it will get better!")

if (answer == "Good"):
	print("Awesome", Name,"Enjoy the rest of it!")
if (answer == "GOOD"):
	print("Awesome", Name,"Enjoy the rest of it!")
if (answer == "gooD"):
	print("Awesome", Name,"Enjoy the rest of it!")
if (answer == "gOod"):
	print("Awesome", Name,"Enjoy the rest of it!")
if (answer == "gOOd"):
	print("Awesome", Name,"Enjoy the rest of it!")
if (answer == "goOd"):
	print("Awesome", Name,"Enjoy the rest of it!")

	
input("**Press Enter to Continue**: ")

print("Lets see if I still remember your favorite color! **Press Enter to continue**")

input()

print("I think its",Color,)

Color_input = input("Yes or No: ")

if(Color_input == "Yes"):
	print("Yeyy!! I got it right.... Im the most intelligent computer-bot!! :)")
if(Color_input == "yes"):
	print("Yeyy!! I got it right.... Im the most intelligent computer-bot!! :)")
if(Color_input == "YES"):
	print("Yeyy!! I got it right.... Im the most intelligent computer-bot!! :)")
if(Color_input == "bad"):
	print("Oh no! This is not good.. I may have to go back to bot school :( ")
if(Color_input == "Bad"):
	print("Oh no! This is not good.. I may have to go back to bot school :( ")
if(Color_input == "BAD"):
	print("Oh no! This is not good.. I may have to go back to bot school :( ")
	
input("**Press Enter to Continue**: ")

print("It has been awesome interacting with you ",Name, "... Oh, and by the way I also like ", Interest,)
input()

	
