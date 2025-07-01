import webbrowser
from datetime import datetime

n = ""
while n.lower() != 'bye':
    n = input("Enter command/text: ").lower().strip()

    if n == 'hello':
        print("Hi")
    elif n == 'how are you':
        print("I'm fine")
    elif n == 'what is the time' or n == "what's the time":
        current_time = datetime.now().strftime("%H:%M:%S")
        print("Current time is:", current_time)
    elif n == 'what is the date' or n == "what's the date":
        current_date = datetime.now().strftime("%d %B %Y")
        print("Today's date is:", current_date)
    elif n == 'open google':
        print("Opening Google...")
        webbrowser.open("https://www.google.com")
    elif n == 'open youtube':
        print("Opening YouTube...")
        webbrowser.open("https://www.youtube.com")
    elif n == 'bye':
        print("Thanks for chatting!")
        print("Goodbye 👋")
    else:
        print("I didn't understand that. Try 'hello', 'how are you', 'what's the time', 'open google', or 'bye'.")

