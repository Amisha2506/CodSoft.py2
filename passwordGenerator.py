import string
import random
   
length = int(input("Enter password length: "))
 
print('''choose any character from the following given set : 
         1.digits
         2.letters
         3.special characters
         4.exit''')
 
characterList = ''
 
 
while(True):
    choice = int(input("take any number "))
    if(choice == 1):
         characterList += string.ascii_letters
    elif(choice == 2):
         characterList += string.digits
    elif(choice == 3):
         characterList += string.punctuation
    elif(choice == 4):
        break
    else:
        print("Please choose a valid option!")
 
password = []
 
for i in range(length):
   
    
    randomchar = random.choice(characterList)
     
    
    password.append(randomchar)
 
 
print("The random password is " + "".join(password))    
