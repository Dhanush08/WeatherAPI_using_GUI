import tkinter as tk
import requests
import config

window = tk.Tk()

window.geometry("800x650")


def format_response(weather):
    try:
        name = weather["name"]
        desc = weather["weather"][0]["description"]
        temp = weather["main"]["temp"]
        final = f"""City: {name}\nConditions: {desc}\nTemperature(°C): {str(temp)}"""
    except:
        final = "There was a problem retrieving the data"
    return final


def get_weather(entry):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"APPID": config.key, "q": entry, "units": "metric"}
    response = requests.get(url, params=params)
    weather = response.json()
    label["text"] = format_response(weather)


background_image = tk.PhotoImage(file="skybackground.png")
background_Label = tk.Label(window, image=background_image)
background_Label.pack()


frame = tk.Frame(window, bg="#fcdf03", bd=5)
frame.place(relx=0.1, rely=0.15, relheight=0.07, relwidth=0.8)

entry = tk.Entry(frame, font=("System", 15))
entry.place(relheight=1, relwidth=0.8)

button = tk.Button(frame, text="Get Weather",
                   command=lambda: get_weather(entry.get()))
button.place(relx=0.8, relheight=1, relwidth=0.2)

lower_frame = tk.Frame(window, bg="#fcdf03", bd=5)
lower_frame.place(relx=0.1, rely=0.3, relheight=0.6, relwidth=0.8)

label = tk.Label(lower_frame, font=("Microsoft Himalaya", 30),
                 anchor="nw", justify="left", bd=5)
label.place(relheight=1, relwidth=1)

window.mainloop()
