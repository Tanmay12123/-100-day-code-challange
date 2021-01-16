# from tkinter import *
import requests
from datetime import datetime

# def get_quote():
#     request = requests.get(url= "https://api.kanye.rest")
#     data = request.json()["quote"]
#     canvas.itemconfig(quote_text,text = data)
#     #Write your code here.


# window = Tk()
# window.title("Kanye Says...")
# window.config(padx=50, pady=50)

# canvas = Canvas(width=300, height=414)
# background_img = PhotoImage(file="C:/Users/home/Desktop/Tanmay The Entirety/Python Stuff/#100 day code challange/challange_19/background.png")
# canvas.create_image(150, 207, image=background_img)
# quote_text = canvas.create_text(150, 207, text="Press the Kenye button to get the quote", width=250, font=("Arial", 30, "bold"), fill="white")
# canvas.grid(row=0, column=0)

# kanye_img = PhotoImage(file="C:/Users/home/Desktop/Tanmay The Entirety/Python Stuff/#100 day code challange/challange_19/kanye.png")
# kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
# kanye_button.grid(row=1, column=0)

# window.mainloop()

MY_LAT = 13.012180
MY_LNG = 77.516480


parameters = {
    "lat": MY_LAT,
    "lng":MY_LNG,
    "formatted": 0
}
response = requests.get(" https://api.sunrise-sunset.org/json",params= parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)


time_now = datetime.now()
print(time_now.hour)








