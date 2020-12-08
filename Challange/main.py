import random
from game_data import data
from logo import logo,vs


randomised = random.choice(data)
randomised_b = random.choice(data)
# print(randomised_b)
# print(randomised)

randomised_name_b = randomised_b['name']
randomised_description_b = randomised_b['description']
randomised_count_b = randomised_b['country']

randomised_name = randomised['name']
randomised_description = randomised['description']
randomised_count = randomised['country']

def checker():
    if randomised["follower_count"] > randomised_b["follower_count"]:
        return("a").lower()
    else:
        return("b").lower()




def main():
    print(logo)
    option_a = print(f" Name: {randomised_name} , a {randomised_description}, from {randomised_count}")
    print(vs)
    option_b = print(f" Name: {randomised_name_b} , a {randomised_description_b}, from {randomised_count_b}")
    user_choice = input("Enter A or B").lower() 
    points = 0
    has_made_a_mistake = False
    while has_made_a_mistake == False:
        if checker() == user_choice:
            points  += 1000
            print(f"Your points are {points}")
            print("That is absolutely right buddy")
            main()
        elif checker != user_choice:
            has_made_a_mistake = True
            print(f"You have chosen the incorrect answer and your total points are {points}")
            

main()
