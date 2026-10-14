from tkinter import *

def update_color():
    # Get the current values of the sliders
    r = red_slider.get()
    g = green_slider.get()
    b = blue_slider.get()
    
    # Convert to hexadecimal color code
    colorHex = f'#{r:02x}{g:02x}{b:02x}'
    
    # Update the preview and hex code display
    color_preview.config(bg=colorHex)
    color_entry.delete(0, END)
    color_entry.insert(0, colorHex)

def adjust_slider(slider, step=1):
    # Adjust the slider value, ensuring it stays within bounds
    new_value = slider.get() + step
    new_value = max(0, min(255, new_value))  # Keep within 0-255
    slider.set(new_value)
    update_color()

def key_press(event):
    # Determine which slider is focused and adjust accordingly
    if event.keysym in ["Up", "Down"]:
        step = 1 if event.keysym == "Up" else -1
        if focused_slider.get() == red_slider.get():
            adjust_slider(red_slider, step)
        elif focused_slider.get() == green_slider.get():
            adjust_slider(green_slider, step)
        elif focused_slider.get() == blue_slider.get():
            adjust_slider(blue_slider, step)

def key_press_shift(event):
    # Handle Shift + Up/Down for larger adjustments
    if event.keysym in ["Up", "Down"]:
        step = 10 if event.keysym == "Up" else -10
        if focused_slider.get() == red_slider.get():
            adjust_slider(red_slider, step)
        elif focused_slider.get() == green_slider.get():
            adjust_slider(green_slider, step)
        elif focused_slider.get() == blue_slider.get():
            adjust_slider(blue_slider, step)

# Main window setup
window = Tk()
window.geometry("600x520")  # Wider window size
window.title("Modern RGB Color Picker")
window.configure(bg="#2E2E2E")

# Title label
title_label = Label(window, text="RGB Color Picker", font=("Arial", 20, "bold"), fg="#F0F0F0", bg="#2E2E2E")
title_label.pack(pady=20)

# Preview box to show selected color
color_preview = Label(window, width=40, height=10, bg="#FFFFFF", relief="sunken", borderwidth=2)
color_preview.pack(pady=20)

# Sliders for Red, Green, and Blue channels
red_slider = Scale(window, from_=0, to=255, orient=HORIZONTAL, label="Red", font=("Arial", 10), fg="#F0F0F0", bg="#2E2E2E", troughcolor="#FF4C4C", command=lambda x: update_color())
red_slider.pack(fill=X, padx=20, pady=5)

green_slider = Scale(window, from_=0, to=255, orient=HORIZONTAL, label="Green", font=("Arial", 10), fg="#F0F0F0", bg="#2E2E2E", troughcolor="#4CFF4C", command=lambda x: update_color())
green_slider.pack(fill=X, padx=20, pady=5)

blue_slider = Scale(window, from_=0, to=255, orient=HORIZONTAL, label="Blue", font=("Arial", 10), fg="#F0F0F0", bg="#2E2E2E", troughcolor="#4C4CFF", command=lambda x: update_color())
blue_slider.pack(fill=X, padx=20, pady=5)

# Focused slider variable
focused_slider = red_slider  # Start with red slider focused

# Bind slider focus and key events
for slider in [red_slider, green_slider, blue_slider]:
    slider.bind("<FocusIn>", lambda event, s=slider: set_focused_slider(s))
    slider.bind("<FocusOut>", lambda event: clear_focused_slider())
    slider.bind("<Key>", key_press)
    slider.bind("<Shift-Key>", key_press_shift)

def set_focused_slider(slider):
    global focused_slider
    focused_slider = slider

def clear_focused_slider():
    global focused_slider
    focused_slider = None

# Entry widget to display and copy the hex color code
color_entry = Entry(window, font=("Arial", 12), width=15, justify='center', fg="#333333")
color_entry.pack(pady=20)
color_entry.insert(0, "#FFFFFF")

# Button to close the app
close_button = Button(window, text="Close", font=("Arial", 12), bg="#333333", fg="#FFFFFF", command=window.quit, padx=10, pady=5)
close_button.pack(pady=10)

window.mainloop()
