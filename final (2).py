import cv2
import tkinter as tk
from PIL import Image, ImageTk
import pandas as pd
import colorsys
import math


def capture_image():
    # Read a frame from the webcam
    ret, frame = cap.read()

    # Convert the frame to RGB color space
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Create a PIL Image object from the frame
    image = Image.fromarray(frame_rgb)

    # Save the captured image
    image.save("captured_image.jpg")

    # Close the webcam and the window
    cap.release()
    window.destroy()



def show_frame():
    # Read a frame from the webcam
    ret, frame = cap.read()

    if ret:
        # Convert the frame to RGB color space
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Create a PIL ImageTk object from the frame
        image = Image.fromarray(frame_rgb)
        image_tk = ImageTk.PhotoImage(image)

        # Update the label with the new image
        label.configure(image=image_tk)
        label.image = image_tk

    # Schedule the next frame update
    label.after(10, show_frame)


# Open the webcam
cap = cv2.VideoCapture(0)

# Create a Tkinter window
window = tk.Tk()

# Create a label to display the video feed
label = tk.Label(window)



label.pack()

# Start displaying the video feed
show_frame()

# Create a button to capture an image
capture_button = tk.Button(window, text="Capture Image", command=capture_image)
capture_button.pack()

# Start the Tkinter event loop
window.mainloop()

#####################################################################
# opening the saved image and gets the hex code from left mouse button click


def get_hex_color(event):
    # Get the x and y coordinates of the mouse pointer
    x = event.x
    y = event.y

    # Fetch the color code at the clicked position
    color = image.getpixel((x, y))

    # Convert the color code to hex format
    hex_code = '#{:02x}{:02x}{:02x}'.format(*color)

    # Store the fetched hex color code
    global fetched_hex
    fetched_hex = hex_code

    # Close the Tkinter window
    root.destroy()

# Create a Tkinter window
root = tk.Tk()

# Load the image using PIL
image_path = "captured_image.jpg"
image = Image.open(image_path)

# Get the width and height of the image
width, height = image.size

# Create a PhotoImage from the PIL image
image_tk = ImageTk.PhotoImage(image)

# Create a canvas to display the image
canvas = tk.Canvas(root, width=width, height=height)
canvas.pack()

# Display the image on the canvas
canvas.create_image(0, 0, anchor=tk.NW, image=image_tk)

# Bind the left mouse button click event
root.bind('<Button-1>', get_hex_color)

# Start the Tkinter event loop
root.mainloop()

# Print the fetched hex color code
print("Fetched Hex Color Code:", fetched_hex)

###########################################################################
###########################################################################

def hex_to_hsv(fetched_hex):
    # Remove the '#' character from the hex value
    fetched_hex = fetched_hex.lstrip('#')

    # Convert the hex value to RGB
    rgb_value = tuple(int(fetched_hex[i:i+2], 16) for i in (0, 2, 4))

    # Normalize RGB values to the range [0, 1]
    normalized_rgb = [x / 255.0 for x in rgb_value]

    # Convert RGB to HSV
    hsv_value = colorsys.rgb_to_hsv(*normalized_rgb)

    # Convert hue to degrees
    hue = int(hsv_value[0] * 360)

    # Convert saturation and value to percentages
    saturation = int(hsv_value[1] * 10)
    value = int(hsv_value[2] * 10)

    return hue, saturation, value

    
def find_optimal_product_brands(hue, saturation, value, num_matches=10):
    matches = []

    # Iterate over the dataset
    for index, row in dataset.iterrows():
        # Get HSV values from the dataset
        h = row['H']
        s = row['S']
        v = row['V']
        
        # Calculate Euclidean distance
        distance = math.sqrt((h - hue)**2 + (s - saturation)**2 + (v - value)**2)
        
        # Add the match to the list
        matches.append((row['brand'], row['product'], distance))

    # Sort the matches by distance in ascending order
    matches.sort(key=lambda x: x[2])

    # Return the top N matches
    return matches[:num_matches]


# Load the dataset
dataset = pd.read_csv(r"D:\Pranav_Vignesh\Personal\Anjna\shades.csv")

# Prompt the user to enter the hex value
# fetched_hex = input("Enter your skin color's hex value: ")

# Convert hex value to HSV
hue, saturation, value = hex_to_hsv(fetched_hex)

# Find the top 10 matching products and brands
top_matches = find_optimal_product_brands(hue, saturation, value, num_matches=10)

# Display the top matching products
print("Top 10 matching foundation products:")
print()
print()
for match in top_matches:
    brand = match[0]
    product_name = match[1]
    distance = match[2]
    print("Brand:", brand)
    print("Product Name:", product_name)
    #print("Distance:", distance)
    print()
