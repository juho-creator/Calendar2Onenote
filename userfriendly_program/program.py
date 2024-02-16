import tkinter as tk
from modules.G_OAuth import get_credentials
from modules.M_OAuth import microsoft_login
from modules.main import create_schedule



def move_to_next_screen(current_window):
    global next_window
    
    # Destroy the current window
    current_window.destroy()
    
    # Create the next window
    next_window = tk.Tk()
    next_window.title("Next Screen")
    

def on_google_sign_in_click():
    google_credentials = get_credentials()
    if google_credentials:
        google_sign_in_button.config(text="Logged in with Google account", state="disabled")
    return google_credentials

def on_microsoft_sign_in_click():
    global headers
    global access_token
    headers, access_token = microsoft_login()
    if headers:
        microsoft_sign_in_button.config(text="Logged in with Microsoft account", state="disabled")
        next_button.config(state="active")
    return headers




def main_screen():
    global root 
    global google_sign_in_button
    global microsoft_sign_in_button
    global next_button

    root = tk.Tk()
    root.title("Google Sign-In")

    google_sign_in_button = tk.Button(root, text="Sign in with Google", command=on_google_sign_in_click)
    microsoft_sign_in_button = tk.Button(root, text="Sign in with Microsoft", command=on_microsoft_sign_in_click)
    next_button = tk.Button(root, text="Next", state="disabled", command=second_screen)

    google_sign_in_button.pack(pady=10)
    microsoft_sign_in_button.pack(pady=10)
    next_button.pack(pady=10)

    root.mainloop()

def second_screen():
    global year_entry

    move_to_next_screen(root)

    # Add widgets to the next window
    label = tk.Label(next_window, text="Type in the year")
    label.pack()

    year_entry = tk.Entry(next_window)
    year_entry.pack()

    button = tk.Button(next_window, text="Save Year", command=third_screen)
    button.pack()

    # Run the next window's event loop
    next_window.mainloop()



def third_screen():
    global year_entry
    global year
    
    # Get the value from the entry widget
    year = year_entry.get()

    move_to_next_screen(next_window)

    label = tk.Label(next_window, text=f"Creating Notebook for {year}")
    label.pack()


    create_schedule(year, next_window, headers, access_token)

main_screen()