#Generalized Python3 Program for Stone Paper Scissors Game(Single and Multiplayer Game).

import random

def MainMenu():
 print("\nWelcome To Stone Paper Scissor Game : ")
 choice = int(input("\nEnter 1. for Single Player Game \nEnter 2. for Multiplayer Game \nEnter 9. for Exit \n"))
 if(choice == 1):
  single_player()
 elif(choice == 9):
  exit()
 else:
  two_player()

def single_player():
 while (True):
  print("\nPlease Enter 1. for Stone \nPlease Enter 2. for Paper \nPlease Enter 3. for Scissors ")
  ch = int(input("\nNow its User's Turn..!! \nEnter the Valid Choice : "))
  while (ch > 3 or ch < 1):
   ch = int(input("Enter valid choice"))
  if(ch == 1):
   print("\nUser Input = 1 ")
   user_name = 'Stone'
  elif(ch == 2): 
   print("\nUser Input = 2 ")
   user_name = 'Paper'
  else:
   print("\nUser Input = 3 ")
   user_name = 'Scissors'

  print("User's Choice is " + user_name) 
  print("\nNow its Computer Turn...")

  comp_choice = random.randint(1, 3)
  while(comp_choice == ch):
   comp_choice = random.randint(1, 3)
  if(comp_choice == 1):
   print("Computer's Input = 1 ")
   comp_name = 'Stone'
  elif(comp_choice == 2): 
   print("Computer's Input = 2 ")
   comp_name = 'Paper'
  else:
   print("Computer's Input = 3 ")
   comp_name = 'Scissors'
 
  print("The Computer Input is : " + comp_name)
  print("\nTherefore the Match Is Between ", end ="") 
  print(user_name + " and " + comp_name)

  if((ch == 1 and comp_choice == 2) or (ch == 2 and comp_choice == 1)):
    result = "Paper"
  elif((ch == 1 and comp_choice == 3) or (ch == 3 and comp_choice == 1)):
    result= "Stone"
  else:
    result = "Scissors"

  if(result == user_name):
   print("\nUser has Won the Game ")
  else:
   print("\nComputer has Won The Game ")

  print("\nDo You Want to play Single Player Game Again..? (Y/N)") 
  ans = input() 
  if(ans == 'y' or ans == 'Y'): 
   single_player()
  else:
    MainMenu()

  MainMenu()

def two_player():
 while (True):
  print("\nPlease Enter 1. for Stone \nPlease Enter 2. for Paper \nPlease Enter 3. for Scissors ")
  ch = int(input("\nNow its First Player's Turn..!! \nEnter the Valid Choice : "))
  while (ch > 3 or ch < 1):
   ch = int(input("Enter valid choice"))
  if(ch == 1):
   print("\nFirst Player's Input = 1 ")
   user_name = 'Stone'
  elif(ch == 2): 
   print("\nFirst Player's Input = 2 ")
   user_name = 'Paper'
  else:
   print("\nFirst Player's Input = 3 ")
   user_name = 'Scissors'

  print("First Player's is " + user_name) 
  print("\nPlease Enter 1. for Stone \nPlease Enter 2. for Paper \nPlease Enter 3. for Scissors ")  
  ch1 = int(input("\nNow its Second Player's Turn..!! \nEnter the Valid Choice : "))
  while (ch1 > 3 or ch1 < 1):
   ch = int(input("Enter valid choice"))
  if(ch1 == 1):
   print("Second Player's Input = 1 ")
   comp_name = 'Stone'
  elif(ch1 == 2): 
   print("Second Player's Input = 2 ")
   comp_name = 'Paper'
  else:
   print("Second Player's Input = 3 ")
   comp_name = 'Scissors'
 
  print("The Second Player's Input is : " + comp_name)
  print("\nTherefore the Match Is Between ", end ="") 
  print(user_name + " and " + comp_name)

  if((ch == 1 and ch1 == 2) or (ch == 2 and ch1 == 1)):
    result = "Paper"
  elif((ch == 1 and ch1 == 3) or (ch == 3 and ch1 == 1)):
    result= "Stone"
  else:  
    result = "Scissors"

  if(result == user_name):
   print("\nFirst Player has Won the Game ")
  else:
   print("\nSecond Player has Won The Game ")
  
  print("\nDo You Want to play Multiplayer Game Again..? (Y/N)") 
  ans = input() 
  if(ans == 'y' or ans == 'Y'): 
   two_player()
  else:
    MainMenu()
  
  MainMenu()

def exit():
 print("\nDo You Want to End the Program..? (yes /no ) ") 
 end = input() 
 if(end == 'y' or end == 'Y'): 
  print("Thanks for Playing.. :) ")
  quit()
 else:
  MainMenu()

MainMenu()

'''
Output : 
mahesh@mahesh-System:~$ python3 Paper.py

Welcome To Stone Paper Scissor Game : 

Enter 1. for Single Player Game 
Enter 2. for Multiplayer Game 
Enter 9. for Exit 
1

Please Enter 1. for Stone 
Please Enter 2. for Paper 
Please Enter 3. for Scissors 

Now its User's Turn..!! 
Enter the Valid Choice : 2

User Input = 2 
User's Choice is Paper

Now its Computer Turn...
Computer's Input = 1 
The Computer Input is : Stone

Therefore the Match Is Between Paper and Stone

User has Won the Game 

Do You Want to play Single Player Game Again..? (Y/N)
y

Please Enter 1. for Stone 
Please Enter 2. for Paper 
Please Enter 3. for Scissors 

Now its User's Turn..!! 
Enter the Valid Choice : 3

User Input = 3 
User's Choice is Scissors

Now its Computer Turn...
Computer's Input = 2 
The Computer Input is : Paper

Therefore the Match Is Between Scissors and Paper

User has Won the Game 

Do You Want to play Single Player Game Again..? (Y/N)
y

Please Enter 1. for Stone 
Please Enter 2. for Paper 
Please Enter 3. for Scissors 

Now its User's Turn..!! 
Enter the Valid Choice : 1

User Input = 1 
User's Choice is Stone

Now its Computer Turn...
Computer's Input = 2 
The Computer Input is : Paper

Therefore the Match Is Between Stone and Paper

Computer has Won The Game 

Do You Want to play Single Player Game Again..? (Y/N)
n

Welcome To Stone Paper Scissor Game : 

Enter 1. for Single Player Game 
Enter 2. for Multiplayer Game 
Enter 9. for Exit 
2

Please Enter 1. for Stone 
Please Enter 2. for Paper 
Please Enter 3. for Scissors 

Now its First Player's Turn..!! 
Enter the Valid Choice : 1

First Player's Input = 1 
First Player's is Stone

Please Enter 1. for Stone 
Please Enter 2. for Paper 
Please Enter 3. for Scissors 

Now its Second Player's Turn..!! 
Enter the Valid Choice : 3
Second Player's Input = 3 
The Second Player's Input is : Scissors

Therefore the Match Is Between Stone and Scissors

First Player has Won the Game 

Do You Want to play Multiplayer Game Again..? (Y/N)
y

Please Enter 1. for Stone 
Please Enter 2. for Paper 
Please Enter 3. for Scissors 

Now its First Player's Turn..!! 
Enter the Valid Choice : 2

First Player's Input = 2 
First Player's is Paper

Please Enter 1. for Stone 
Please Enter 2. for Paper 
Please Enter 3. for Scissors 

Now its Second Player's Turn..!! 
Enter the Valid Choice : 1
Second Player's Input = 1 
The Second Player's Input is : Stone

Therefore the Match Is Between Paper and Stone

First Player has Won the Game 

Do You Want to play Multiplayer Game Again..? (Y/N)
y

Please Enter 1. for Stone 
Please Enter 2. for Paper 
Please Enter 3. for Scissors 

Now its First Player's Turn..!! 
Enter the Valid Choice : 3

First Player's Input = 3 
First Player's is Scissors

Please Enter 1. for Stone 
Please Enter 2. for Paper 
Please Enter 3. for Scissors 

Now its Second Player's Turn..!! 
Enter the Valid Choice : 3
Second Player's Input = 3 
The Second Player's Input is : Scissors

Therefore the Match Is Between Scissors and Scissors

First Player has Won the Game 

Do You Want to play Multiplayer Game Again..? (Y/N)
y

Please Enter 1. for Stone 
Please Enter 2. for Paper 
Please Enter 3. for Scissors 

Now its First Player's Turn..!! 
Enter the Valid Choice : 1

First Player's Input = 1 
First Player's is Stone

Please Enter 1. for Stone 
Please Enter 2. for Paper 
Please Enter 3. for Scissors 

Now its Second Player's Turn..!! 
Enter the Valid Choice : 2
Second Player's Input = 2 
The Second Player's Input is : Paper

Therefore the Match Is Between Stone and Paper

Second Player has Won The Game 

Do You Want to play Multiplayer Game Again..? (Y/N)
n

Welcome To Stone Paper Scissor Game : 

Enter 1. for Single Player Game 
Enter 2. for Multiplayer Game 
Enter 9. for Exit 
9

Do You Want to End the Program..? (yes /no ) 
n

Welcome To Stone Paper Scissor Game : 

Enter 1. for Single Player Game 
Enter 2. for Multiplayer Game 
Enter 9. for Exit 
2

Please Enter 1. for Stone 
Please Enter 2. for Paper 
Please Enter 3. for Scissors 

Now its First Player's Turn..!! 
Enter the Valid Choice : 3

First Player's Input = 3 
First Player's is Scissors

Please Enter 1. for Stone 
Please Enter 2. for Paper 
Please Enter 3. for Scissors 

Now its Second Player's Turn..!! 
Enter the Valid Choice : 1
Second Player's Input = 1 
The Second Player's Input is : Stone

Therefore the Match Is Between Scissors and Stone

Second Player has Won The Game 

Do You Want to play Multiplayer Game Again..? (Y/N)
nn

Welcome To Stone Paper Scissor Game : 

Enter 1. for Single Player Game 
Enter 2. for Multiplayer Game 
Enter 9. for Exit 
9

Do You Want to End the Program..? (yes /no ) 
y
Thanks for Playing.. :) 
'''
