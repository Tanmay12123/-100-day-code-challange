MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 150,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 225,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 300,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
######################################################################################################################
next_coustomer = True


user_request = input("What would you like? (espresso/latte/cappuccino):  ").lower()# Taking request from user
# import os


coffee_type = MENU[user_request]# searching for the coffee that the user wants in our menue
ingredients_used = coffee_type["ingredients"]# checking for the ingridients used in making that coffee requested by the user

# def cost_calculator(name_of_coffee):
#     """ calculates the cost of the coffee"""
#     price = MENU[name_of_coffee]
#     value = price["cost"]
#     return(value)

espresso_cost = 150
latte_cost = 225
cappuccino = 300

# calculates the ingredients from the coffee to the ingredients that we have and uses and subtracts the ingridients after use
def calculations(ingredient):
    """ TO ADD THE VALUES OF THE INGREDIENTS TO BE CALCULATED ACCORDING THO THE NAME OF THE COFFEE"""
    value =resources[ingredient] - ingredients_used[ingredient]
    resources[ingredient]  =  value 
    return(value)
    # print(resources)

payment_mode = input("How would you like to pay? UPI or Cash?").lower()
#checking the type of coffee whih the user wants and using our calculations based on it and even checking for payment
if payment_mode == "upi" or payment_mode == "cash" :
    print("OK, sure! ")
    
    if user_request == "espresso":
            if resources["water"] != 0 or resources["milk"] != 0 or resources["coffee"] != 0:
                print(f"It costs {espresso_cost}")
                user_pay = int(input("Please pay the amount here:  ₹"))
                if user_pay >= espresso_cost:
                    # print(user_pay)
                    print("Hang on! Till we prepare your espresso!")
                    calculations("water")
                    calculations("coffee")
                    # print(resources)
                    # os.system('clear')
                    print(
                            """
                            
                '━━━━━━━━━━━━
                ┃╱╲┃╱╲┃╱╲┃╱╲┊
                ┃╲╱┃╲╱┃╲╱┃╲╱┊━━━━╮
                ┃╱╲┃╱╲┃╱╲┃╱╲┊━━━╮┃
                ┃╲╱┃╲╱┃╲╱┃╲╱┊┈┈┈┃┃
                ┃╱╲┃╱╲┃╱╲┃╱╲┊━━━╯┃
                ┃╲╱┃╲╱┃╲╱┃╲╱┊━━━━╯
                ┈╲╲┃╱╲┃╱╲┃╱╱
                ┈┈╲┃╲╱┃╲╱┊╱
                ┻┻┻┻┻┻┻┻┻┻┻┻┻
                            """)
                    print("Enjoy your coffee! here you go!")
                else:
                    print("Sorry,you paid less")
        
            else:
                print("Sorry, we do not have enough ingridents left! Come back tommorow for a fresh one!")
        
    elif user_request == "latte" or user_request == "cappuccino":
        if resources["water"] != 0 or resources["milk"] != 0 or resources["coffee"] != 0:
            print(f"It costs ₹300")
            user_pay = int(input("Please pay the amount here:  ₹"))
            if user_pay >= cappuccino or user_pay >= latte_cost:
                # print(user_pay)
                print("Hang on! Till we prepare your coffee")
                calculations("water")
                calculations("milk")
                calculations("coffee")
                # os.system('clear')
                print(
                            """
                            
                '━━━━━━━━━━━━
                ┃╱╲┃╱╲┃╱╲┃╱╲┊
                ┃╲╱┃╲╱┃╲╱┃╲╱┊━━━━╮
                ┃╱╲┃╱╲┃╱╲┃╱╲┊━━━╮┃
                ┃╲╱┃╲╱┃╲╱┃╲╱┊┈┈┈┃┃
                ┃╱╲┃╱╲┃╱╲┃╱╲┊━━━╯┃
                ┃╲╱┃╲╱┃╲╱┃╲╱┊━━━━╯
                ┈╲╲┃╱╲┃╱╲┃╱╱
                ┈┈╲┃╲╱┃╲╱┊╱
                ┻┻┻┻┻┻┻┻┻┻┻┻┻
                            """)
                print("Here you go !Enjoy your coffee! ")
            else:
                print("Sorry you paid less")
        else:
                print("Sorry, we do not have enough ingridents left! Come back tommorow for a fresh one!")

elif payment_mode == "off":
        next_coustomer = False
else:
        print("Sorry, payment was not issued by you")