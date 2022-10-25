#!/usr/bin/env python
# coding: utf-8

# In[1]:


# -------------------------
# This initializes the User class/object, as it needs the username and password of the user.
class User:
   def __init__(self, username, password):
       username = username.lower()
       self.user_login = {
       "username": username,
       "password": password}
    
# -------------------------
# This function checks the login details entered by the user.
   def login_info(self, response):
       if (response["username"] == self.user_login["username"] and
           response["password"] == self.user_login["password"]):
           return "Login successful!!!"

       else:
           return "Invalid username and/or password"

# -------------------------
# User login information
def login():
   login_user = User("PGR211", "Python")


   user_response1 = input("Username: ")
   user_response2 = input("Password: ")
   user_response1=user_response1.lower()


   response = {}
   response["username"] = user_response1
   response["password"] = user_response2
   ret = login_user.login_info(response)
   print(ret)
   if ret == "Login successful!!!":
       return True
   else:
       return False

# -------------------------
# Quiz game
def quiz_game():
  guesses = []
  correct_guesses = 0
  question_num = 1

  for key in questions:
      print("-------------------------")
      print(key)
      print("-------------------------")
    
      for i in options[question_num-1]:
          print(i)
      while(True):
          guess = input("Enter (a, b, c, or d): ")
          guess = guess.lower()
          if(guess !="a" and guess !="b" and guess !="c" and guess !="d"):
              print("Invalid input")
          else:
              break
                
      guesses.append(guess)
      ans_dict ={"a":0,"b":1,"c":2,"d":3}        
      full_answer = options[question_num-1][ans_dict[questions.get(key)]] 
      correct_guesses += check_answer(questions.get(key), guess, full_answer) 
      question_num += 1
    
  display_score(correct_guesses, guesses)

# -------------------------
# Quiz answer check
def check_answer(answer, guess, full_answer=""): 
  if answer == guess:
      print("\n-Correct! Good job!")
      return 1
  else:
      print("\n-Wrong! Better luck next time!")
      print("\n-The correct answer is:", full_answer, "\n") 
      return 0

# -------------------------
# Score display
def display_score(correct_guesses, guesses):
  print("-------------------------")
  print("Final results")
  print("-------------------------")
  print("Correct answers: ", end="")
  for i in questions:
      print(questions.get(i), end=" ")
  print()
  print("Your guesses:    ", end="")
  for i in guesses:
      print(i, end=" ")
  print()
  score = int(correct_guesses)
  print("\nYour scored: "+str(score) + " / " + str(len(questions)))

# -------------------------
# Play the quiz again
def quiz_again():
  response = input("Do you want to play again? (y / n): ")
  response = response.lower()
  if response == "y":
      return True
  else:
      return False
    
# -------------------------
# # Our quiz questions
questions = {
"1. What is the capital of Norway?: ": "b",
"2. What is the currency of Norway?: ": "c",
"3. What is the largest city in Norway? : ": "a",
"4. When is constitution day (the national day) of Norway? : ": "b",
"5. What color is the background of the Norwegian flag? : ": "a",
"6. How many countries does Norway border? : ": "c",
"7. What is the name of the university in Trondheim? : ": "d",
"8. How long is the border between Norway and Russia? : ": "b",
"9. Where in Norway is Stavanger? : ": "c",
"10. From which Norwegian city did the world famous composer Edvard Grieg come?": "b"}

# -------------------------
# Our quiz options
options = [["a. Bergen", "b. Oslo", "c. Stavanger", "d. Trondheim"],
          ["a. Euro", "b. Pound", "c. Krone", "d. Deutsche Mark"],
          ["a. Oslo", "b. Stavanger", "c. Bergen", "d. Trondheim"],
          ["a. 27th May", "b. 17th May", "c. 17th April", "d. 27th April"],
          ["a. Red", "b. White", "c. Blue", "d. Yellow"],
          ["a. 1", "b. 2", "c. 3", "d. 4"],
          ["a. UiS", "b. UIO", "c. NMBU", "d. NTNU"],
          ["a. 96 km", "b. 196 km", "c. 296 km", "d. 396 km"],
          ["a. North", "b. South", "c. South-west", "d. South-east"],
          ["a. Oslo", "b. Bergen", "c. Stavanger", "d. Tromsø"]]

# -------------------------
print("\n~~~ Welcome to this multiple choice quiz! ~~~\n")

while login() == False:
   print("-Unable to play")
   print ('\nPlease retry login again..\n')

quiz_game()

while quiz_again():
    quiz_game()

print("\n~~~Hope you had a great time, and thank you for playing!~~~")


# In[ ]:




