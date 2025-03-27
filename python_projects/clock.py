import tkinter as tk
import time
import math

# Create the main application window
root = tk.Tk()
root.title("Stylish Round Analog Clock")  # Set window title
root.geometry("400x400")  # Square window
root.resizable(False, False)  # Disable resizing to maintain proportions

# Create a canvas for drawing the clock
canvas = tk.Canvas(root, width=400, height=400, bg="black")
canvas.pack()

# Clock center and radius
CENTER_X, CENTER_Y = 200, 200  # Clock center coordinates
CLOCK_RADIUS = 150  # Clock radius

def gradient_background():
    """
    Draw a smooth gradient background on the canvas.
    """
    for i in range(CLOCK_RADIUS):
        # Calculate color with a smooth gradient from blue to purple
        r = int(50 + i * 0.5)
        g = int(50 + i * 0.5)
        b = int(255 - i * 0.8)
        color = f"#{r:02x}{g:02x}{b:02x}"
        canvas.create_oval(
            CENTER_X - CLOCK_RADIUS + i, CENTER_Y - CLOCK_RADIUS + i,
            CENTER_X + CLOCK_RADIUS - i, CENTER_Y + CLOCK_RADIUS - i,
            outline='', fill=color
        )

def draw_clock_face():
    """
    Draw the circular clock face with tick marks and hour markings.
    """
    # Draw the outer circle
    canvas.create_oval(
        CENTER_X - CLOCK_RADIUS, CENTER_Y - CLOCK_RADIUS,
        CENTER_X + CLOCK_RADIUS, CENTER_Y + CLOCK_RADIUS,
        outline="white", width=4
    )

    # Draw hour markings (12 hours)
    for i in range(12):
        angle = math.radians(i * 30)  # Each hour marking is 30 degrees apart
        x_start = CENTER_X + (CLOCK_RADIUS - 30) * math.sin(angle)
        y_start = CENTER_Y - (CLOCK_RADIUS - 30) * math.cos(angle)
        x_end = CENTER_X + CLOCK_RADIUS * math.sin(angle)
        y_end = CENTER_Y - CLOCK_RADIUS * math.cos(angle)
        canvas.create_line(x_start, y_start, x_end, y_end, fill="white", width=3)

    # Draw minute tick marks
    for i in range(60):
        if i % 5 != 0:  # Skip hour ticks to avoid overlap
            angle = math.radians(i * 6)
            x_start = CENTER_X + (CLOCK_RADIUS - 20) * math.sin(angle)
            y_start = CENTER_Y - (CLOCK_RADIUS - 20) * math.cos(angle)
            x_end = CENTER_X + (CLOCK_RADIUS - 10) * math.sin(angle)
            y_end = CENTER_Y - (CLOCK_RADIUS - 10) * math.cos(angle)
            canvas.create_line(x_start, y_start, x_end, y_end, fill="white", width=1)

def update_clock():
    """
    Update the clock hands based on the current time.
    """
    # Clear the previous hands
    canvas.delete("hands")

    # Get the current time
    current_time = time.localtime()
    hour = current_time.tm_hour % 12  # Convert to 12-hour format
    minute = current_time.tm_min
    second = current_time.tm_sec

    # Calculate angles for the hands
    second_angle = math.radians(second * 6)  # Each second is 6 degrees
    minute_angle = math.radians(minute * 6 + second * 0.1)  # Each minute is 6 degrees, add seconds
    hour_angle = math.radians(hour * 30 + minute * 0.5)  # Each hour is 30 degrees, add minutes

    # Draw the second hand (red, thin with glow effect)
    draw_hand(second_angle, CLOCK_RADIUS - 20, "red", 2, 8)
    # Draw the minute hand (white, medium)
    draw_hand(minute_angle, CLOCK_RADIUS - 40, "white", 4, 6)
    # Draw the hour hand (white, thick)
    draw_hand(hour_angle, CLOCK_RADIUS - 60, "white", 6, 4)

    # Schedule the function to run again after 100ms
    canvas.after(100, update_clock)

def draw_hand(angle, length, color, width, glow_radius):
    """
    Draw a clock hand based on angle, length, color, width, and glow effect.
    """
    x_end = CENTER_X + length * math.sin(angle)
    y_end = CENTER_Y - length * math.cos(angle)

    # Add a glow effect around the hand (a larger semi-transparent line)
    canvas.create_line(
        CENTER_X, CENTER_Y, x_end, y_end, fill=color, width=glow_radius,
        capstyle=tk.ROUND, tag="hands"
    )
    
    # Draw the actual hand with defined width
    canvas.create_line(
        CENTER_X, CENTER_Y, x_end, y_end, fill=color, width=width,
        capstyle=tk.ROUND, tag="hands"
    )

gradient_background()
draw_clock_face()
update_clock()
root.mainloop()
