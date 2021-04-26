import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


print(Fore.MAGENTA + "Complete the following madlib to read a letter from an important historical figure!")

pl_noun1=input("Enter a plural noun:")
occupation=input("Enter a occupation:")
place1=input("Enter a place:")
numb=input("Enter a number:")
adj1=input("Enter an adjective:")
ingverb1=input("Enter a verb ending in 'ing':")
pl_noun2=input("Enter a plural noun:")
place2=input("Enter a place:")
adj2=input("Enter an adjective:")
pl_noun3=input("Enter a plural noun:")
ingverb2=input("Enter a verb ending in 'ing':")
pl_noun4=input("Enter a plural noun:")
adj3=input("Enter an adjective:")
noun=input("Enter a noun:")
body=input("Enter a part of the body:")
verb=input("Enter a verb:")
adj4=input("Enter an adjective:")
body2=input("Enter a part of the body:")

print("Hello, my fellow ", Fore.BLUE + pl_noun1, " in 2020, it is me, George Washington, the first ", Fore.BLUE + occupation,". ")
print("I am writing from (the) ", Fore.BLUE + place1, ", where I have been secretly living for the past ", Fore.BLUE + numb, "years. ")
print("I am concerned by the ", Fore.BLUE + adj1, " state of affairs in America these days. ")
print("It seems that your politicians are more concerned with ", Fore.BLUE + ingverb1, "one another than with listening to the ", Fore.BLUE + pl_noun2, " of the people. ")
print("When we declared our independence from the ", Fore.BLUE +place2, ", we set forth on a/an ", Fore.BLUE + adj2, " path guided by the voices "
      "of the everyday ", Fore.BLUE + pl_noun3, ". ")
print("If we're going to keep ", Fore.BLUE + ingverb2, ", then we need to learn how to respect all ", Fore.BLUE + pl_noun4, ". ")
print("Don't get me wrong; we had ", Fore.BLUE + adj3, " problems in my day, too. ")
print("Benjamin Franklin once called me a/an ", Fore.BLUE + noun, " and kicked me in the ", Fore.BLUE + body, ". ")
print("But at the end of the day, we were able to ", Fore.BLUE + verb, " in harmony. ")
print("Let us find that ", Fore.BLUE + adj4, " spirit again, or else I'm taking my ", Fore.BLUE + body2, " off the quarter! ")

print(Fore.MAGENTA+"Thanks for playing!")

