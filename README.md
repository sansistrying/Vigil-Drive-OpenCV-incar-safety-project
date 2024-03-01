# Object Detection GUI using Tkinter and OpenCV

This Python script utilizes the Tkinter library for creating a graphical user interface (GUI) to perform object detection using a pre-trained PyTorch model. The GUI allows users to choose between live camera detection, video input, or image input.

## Requirements
- Python 3.x
- OpenCV
- PyTorch

Install the required libraries using the following command:
```
pip install opencv-python torch
```
## Usage
- Clone the repository or download the script.
- Run the script in a Python environment.
## Functionality
### Live Camera Detection
- Click the "Live Cam Detection" button to open a live camera feed.
- Press 'q' to exit the live camera feed.
### Video Input
- Click the "Video Input" button to choose a video file using a file dialog.
- Press 'q' to exit the video playback.
### Image Input
- Click the "Image Input" button to choose an image file using a file dialog.
- Image input functionality is not fully implemented. You can complete the code in the image_input function.
- Model Loading
- The script loads a pre-trained PyTorch model using torch.load. Please replace the model file path with your actual model file path.
```
model = torch.load(r"your_model_path.pt")
model.eval()
```
## Notes
Ensure that the required libraries are installed before running the script.
Replace the model file path with the path to your trained PyTorch model.
The script currently lacks complete implementation for image input. You may need to add the necessary code in the image_input function.
Feel free to modify the script according to your specific use case and model requirements.
