import random
word=["watermelon","banana","python"]
word=random.choice(word)
guessed =""
attempts=5
print("HANGMAN GAME")
while attempts>0:
   for letter in word:
      if letter in guessed:
         print(letter,end=" ") 
      else:
             print("_",end=" ")
               
      print("\nattempts left:",attempts) 
      
      guess=input("enter a letter:").lower()
         
      if guess in guessed:
             print("already guessed!")
             continue
             
      guessed += guess
           
      if guess in word:
         print("correct!")
      else:
         print("wrong!")
         attempts -=1 
      if all(letter in guessed for letter in word):  
         print("you won!")
         break
      if attempts==0:
         print("GAME OVER!")
         print("The word was:",word)  
              
                
                  
               
             
         