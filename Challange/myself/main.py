from items import buys
from difflib import get_close_matches 
print(buys)
game_is_on = True

user_choice = input("Enter name:  ").lower()
user_cart = []
user = user_choice.replace(" ", "")
splitted = []

close_match = []
# def closeMatches(buys,user): 
#     close_match.append())


value = "Tanmay"

value = get_close_matches(user,buys)



# value = get_close_matches(buys,user)
# print(value)
# print(close_match)
def items_finder():
    if user == "cart":
        print(f"You have{user_cart} in your cart")
    elif user == "clear cart" or user == "clearcart":
        user_cart.clear()
        print("Cart Cleared")
    for i in buys:
        if user == i or value == i:
            print(f"{user} is there in the list and is added to the cart👍")
            user_cart.append(user)
            break
    else:
        print("Sorry we dont have that yet!")

items_finder()
# print(approx)
# print(get_close_matches(user,buys))
while game_is_on:
    user_choice = input("Enter name:  ").lower()
    user = user_choice.replace(" ", "")
    items_finder()