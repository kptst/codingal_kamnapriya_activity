# ACTIVITY BASED ON cv, opencv


# Install opencv-python if not already installed
# !pip install opencv-python matplotlib requests numpy

import cv2
import matplotlib.pyplot as plt
import requests
import numpy as np

# Load an image from a URL
image_url = 'https://images.contentstack.io/v3/assets/bltcedd8dbd5891265b/blt5f18c2119ce26485/6668df65db90945e0caf9be6/beautiful-flowers-lotus.jpg?q=70&width=3840&auto=webp'

try:
  # Download the image
  response = requests.get(image_url)
  response.raise_for_status()  # Raise an exception for bad status codes

  # Read the image from the downloaded content
  image_array = np.frombuffer(response.content, dtype=np.uint8)
  img = cv2.imdecode(image_array,
                     cv2.IMREAD_COLOR)  # Use cv2.IMREAD_COLOR for color image

  if img is not None:
    # Display the image
    plt.imshow(cv2.cvtColor(
        img,
        cv2.COLOR_BGR2RGB))  # OpenCV reads in BGR, Matplotlib displays in RGB
    plt.title('Loaded Image')
    plt.axis('off')  # Hide axes
    plt.show()

    # Explore image properties
    height, width, channels = img.shape
    print(f"Image Dimensions: Width = {width}, Height = {height}")
    print(f"Number of Channels: {channels}")

    # You can also access individual pixel values
    # pixel_value = img[100, 150] # Get pixel value at row 100, column 150
    # print(f"Pixel value at (150, 100): {pixel_value}")

  else:
    print(
        f"Error: Unable to decode image from {image_url}. Please check the URL or image format."
    )

except requests.exceptions.RequestException as e:
  print(f"Error downloading image: {e}")
except Exception as e:
  print(f"An error occurred: {e}")


