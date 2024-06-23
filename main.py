import pyperclip as clip
import time
import wmi
import json2dict as j2d
import google.generativeai as genai

path = None
module = None

# Search Function to search answers with questions
def search(question):
    global module
    print("Searching")
    for i in module:
        if i == question:
            return module[i]

# Define WMI Batter Class     
def battery():
    c = wmi.WMI()
    battery_info = c.Win32_Battery()[0]
    return battery_info

def json():
    while True:
        event = battery()
        # Battery Discharging State
        if event.BatteryStatus == 1:
            question = str(clip.paste())
            ans = str(search(question))
            clip.copy(ans)
            print("Done")
            time.sleep(5)
            continue

def gemini(key):
    genai.configure(api_key=key)
    model = genai.GenerativeModel('gemini-1.5-pro')
    chat = model.start_chat(history=[])
    while True:
        event = battery()
        # Battery Discharging State
        if event.BatteryStatus == 1:
            question = str(clip.paste())
            response = chat.send_message(question)
            clip.copy(str(response.text))
            time.sleep(5)
            continue

# Main function
def main():
    global path, module
    print("""Choose modes:
           1. JSON
           2. GEMINI""")
    mode = int(input("Enter mode: "))

    if mode == 1:
        path = str(input("Enter Module to be used : "))
        module = j2d.load_json(path)
        json()
    elif mode == 2:
        api_key = str(input("Enter API Key: "))
        gemini(api_key)
    else:
        print("Invalid Mode")

# Main
if __name__ == "__main__":
    main()

        
