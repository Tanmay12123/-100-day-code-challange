#TODO: Create a letter using starting_letter.docx 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("C:/Users/home/Desktop/Tanmay The Entirety/Python Stuff/#100 day code challange/challange_10/Input/Names/invited_names.txt", mode = 'r') as datas:
    print(datas.readlines(1))

with open("C:/Users/home/Desktop/Tanmay The Entirety/Python Stuff/#100 day code challange/challange_10/Input/Letters/starting_letter.docx", mode = 'r+') as data:
    date = data.readlines(1)
    date.replace("[name]",datas.readlines(1))