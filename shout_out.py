import win32com.client as win
speaker = win.Dispatch("SAPI.SpVoice")

while True:
    print("Enter the text you want to speak it by computer: ")
    s = input()
    speaker.Speak(s)
    
# press Ctrl + C to stop the program