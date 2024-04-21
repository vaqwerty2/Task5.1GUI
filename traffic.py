import tkinter as tk
from gpiozero import LED
import sys

# LEDs connected to specific GPIO pins
red_led = LED(17)  # Connect red LED to GPIO pin 17
green_led = LED(27)  # Connect green LED to GPIO pin 27
blue_led = LED(22)  # Connect blue LED to GPIO pin 22

def turn_off_leds():
    """Turn off all LEDs."""
    red_led.off()
    green_led.off()
    blue_led.off()

def select_led(led):
    """Turn off all LEDs and then turn on the selected LED."""
    turn_off_leds()
    led.on()

def exit_app():
    """Cleanup GPIO pins and close the GUI window."""
    turn_off_leds()
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("LED Control Panel")

# Frame for the radio buttons
frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

# Radio button selection variable
selected_led = tk.IntVar()

# Radio buttons for each LED
tk.Radiobutton(frame, text="Red LED", variable=selected_led, value=1, command=lambda: select_led(red_led)).grid(row=0, column=0)
tk.Radiobutton(frame, text="Green LED", variable=selected_led, value=2, command=lambda: select_led(green_led)).grid(row=1, column=0)
tk.Radiobutton(frame, text="Blue LED", variable=selected_led, value=3, command=lambda: select_led(blue_led)).grid(row=2, column=0)

# Exit button
exit_button = tk.Button(root, text="Exit", command=exit_app)
exit_button.pack(pady=10)

# Start the GUI event loop
root.protocol("WM_DELETE_WINDOW", exit_app) 
root.mainloop()
