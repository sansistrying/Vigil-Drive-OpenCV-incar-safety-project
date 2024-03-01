import tkinter as tk
from tkinter import filedialog
import cv2
import torch
import numpy as np

# Load your trained PyTorch model here
model = torch.load(r"C:\Users\sansi\Downloads\best (4).pt")
model.eval()

# Define a function for live camera detection
def live_cam_detection():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Preprocess the frame (resize, normalize, etc.)
        # Perform object detection using your model
        # Display the results on the frame

        # Update the GUI with the processed frame (you can use OpenCV's imshow here)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Define a function for video input
def video_input():
    file_path = filedialog.askopenfilename()
    if file_path:
        cap = cv2.VideoCapture(file_path)

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Preprocess the frame (resize, normalize, etc.)
            # Perform object detection using your model
            # Display the results on the frame

            # Update the GUI with the processed frame (you can use OpenCV's imshow here)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

# Define a function for image input
def image_input():
    file_path = filedialog.askopenfilename()
    if file_path:
        image = cv2.imread(file_path)

        # Preprocess the image (resize, normalize, etc.)
        # Perform object detection using your model
        # Display the results on the image or in a separate window

# Create the main GUI window
root = tk.Tk()
root.title("Object Detection GUI")

# Create buttons for live cam detection, video input, and image input
live_cam_button = tk.Button(root, text="Live Cam Detection", command=live_cam_detection)
video_button = tk.Button(root, text="Video Input", command=video_input)
image_button = tk.Button(root, text="Image Input", command=image_input)

live_cam_button.pack()
video_button.pack()
image_button.pack()

root.mainloop()
