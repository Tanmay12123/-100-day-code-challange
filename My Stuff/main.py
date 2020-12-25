letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
name = input('Enter the name:  ')
broker = input('Enter th name of the broker:  ')
switches = input("Enter the number of switches: ")
brokers = []

def button_adder(name,broker, switches):
    
    print(f"The name of the room is {name}")
    for letter in letters:
        brokers.append(str(broker) + str(letter))
    print(f"The number of switches are {switches}")

button_adder(name,brokers,switches)
print(brokers)