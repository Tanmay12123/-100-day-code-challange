from data import question_data
from question_model import Question
import random
is_correct = True
points = 0
question_number = 0

while is_correct:
    print("""
          
 ________  ___  ___  ___  ________     
|\   __  \|\  \|\  \|\  \|\_____  \    
\ \  \|\  \ \  \\\  \ \  \\|___/  /|   
 \ \  \\\  \ \  \\\  \ \  \   /  / /   
  \ \  \\\  \ \  \\\  \ \  \ /  /_/__  
          """)
    i = random.choice(question_data)
    text = i['text']
    answer = i['answer']
    question_1 = Question(text,answer)
    question_number+=1
    choice = input(f"Q{question_number}: {question_1.text} (True/False)" ).lower()
    if choice[0] == "t":
        choice = "True"
    elif choice[0] == "f":
        choice = "False"
    if choice == question_1.answer:
        print("That is correct")
        points += 1
    else:
        print("That is incorrect")
        is_correct = False
        print(f"Your points are {points}/{question_number}, Good Job!!")
