import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image 
plt.rcParams['image.cmap'] = 'gray'

#######Everyonce can change according to their own requirement##########
image_path = 'Signatures.png'
threshold = 100
color = (255, 0, 0)

def make_signature_transparent(image_path, threshold, color):
    sig_org = cv2.imread(image_path, cv2.IMREAD_COLOR)

    plt.figure(figsize = [5, 5])
    plt.imshow(sig_org[:, :, ::-1])
    plt.show()
    response = input("Do you want to proceed with cropping? (y/n): ")

    # Check user response
    if response.lower() == 'y':
        while True:
        # Ask the user for cropping values
            y1 = int(input("Enter the y1-coordinate : "))
            y2 = int(input("Enter the y2-coordinate : "))
            x1 = int(input("Enter the x1-coordinate : "))
            x2 = int(input("Enter the x2-coordinate : "))

            # Perform cropping based on user input
            sig = sig_org[y1:y2, x1:x2, :]
            plt.imshow(sig [:, :, ::-1])
            plt.show()

            # Ask the user if the cropping is correct
            response = input("Is the cropping correct? (y/n): ")
            if response.lower() == 'y':
                break  # Break the loop and proceed with the rest of the code
            else:
                print("Please enter the cropping values again.")

    sig_gray = cv2.cvtColor(sig, cv2.COLOR_BGR2GRAY)
    ret, alpha_mask = cv2.threshold(sig_gray, threshold, 255, cv2.THRESH_BINARY_INV)
    blue_mask = sig.copy()
    blue_mask[:, :] = color
    sig_color = cv2.addWeighted(sig, 1, blue_mask, 0.5, 0)
    b, g, r = cv2.split(sig_color)
    # Create a list of the four arrays with the alpha channel as the 4th member. These are four separate 2D arrays.
    new = [b, g, r, alpha_mask]

    # Use the merge() function to create a single, multi-channel array.
    png = cv2.merge(new, 4)

    # Save the transparent signature a PNG file to retain the alpha channel.
    cv2.imwrite('extracted.png', png)
make_signature_transparent(image_path, threshold, color)