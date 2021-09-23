import random
import os
result=random.randint(1,100)
n=int(input("Enter Your Choice between 1 to 100: "))
while True:
    if(n==result):
        print("You guessed it correct")
        break
    else:
        print("Wrong Choice. Change the input")
        n=int(input("Enter Your Choice between 1 to 100: "))

os.system("pause")  #This has been included to avoid shell from closing. Its optional