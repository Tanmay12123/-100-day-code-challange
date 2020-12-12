from data import question_data
from question_model import Question
import random
is_correct = True
points = 0

while is_correct:
    i = random.choice(question_data)
    text = i['text']
    answer = i['answer']
    question_1 = Question(text,answer)
    choice = input(f"{question_1.text} (true/false)" )
    if choice == question_1.answer:
        print("That is correct")
        points += 1
    else:
        print("That is incorrect")
        is_correct = False
        print(f"Your points are {points}")
