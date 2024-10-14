import tkinter as tk
from tkinter import filedialog, messagebox
from functools import wraps
from PIL import Image, ImageTk, ImageDraw, ImageFont
# Importing the AI model class from separate file
from ai_model import AIModel
import os

# Suppressing TensorFlow info and warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


# Using a decorator to log method calls
def log_method_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling method: {func.__name__}")
        return func(*args, **kwargs)

    return wrapper


# The base class for general UI tasks
class GeneralUI:
    def __init__(self):
        self.window_title = "AI Image Classifier"
        self.window_size = "800x600"

    def setup_window(self, app):
        app.title(self.window_title)
        app.geometry(self.window_size)
        app.configure(bg='#1768ac')
        app.resizable(False, False)


# Base class for image processing
class ImageProcessing:
    def __init__(self):
        # Encapsulation of the model
        self.model = AIModel()

    # Encapsulation used here in the form of internal AI model prediction method
    def _predict_image(self, file_path):
        return self.model.predict(file_path)


# The derived class combining UI and Image Processing, use of Multiple Inheritance here
class MyApp(tk.Tk, GeneralUI, ImageProcessing):
    def __init__(self):
        tk.Tk.__init__(self)
        GeneralUI.__init__(self)
        ImageProcessing.__init__(self)

        # Window setup
        self.setup_window(self)

        # Creating Frames for layout organization
        self.top_frame = tk.Frame(self, bg='#1768ac')
        self.top_frame.pack(pady=20)
        self.bottom_frame = tk.Frame(self, bg='#1768ac')
        self.bottom_frame.pack(pady=10)

        # The title Label
        self.title_label = tk.Label(self.top_frame, text="AI Image Classifier", font=("Helvetica", 26, 'bold'),
                                    fg="#ffffff", bg='#1768ac')
        self.title_label.pack()

        # The button to Upload Image
        self.upload_button = tk.Button(self.bottom_frame, text="Upload Image", font=("Helvetica", 14), bg='#06bee1',
                                       fg='#ffffff', command=self.upload_image, activebackground='#06bee1',
                                       cursor="hand2", relief="flat")
        self.upload_button.pack(pady=10)

        # The predict button
        self.predict_button = tk.Button(self.bottom_frame, text="Predict", font=("Helvetica", 14), bg='#06bee1',
                                        fg='#ffffff', command=self.predict_image, activebackground='#06bee1',
                                        cursor="hand2", relief="flat")
        self.predict_button.pack(pady=10)
        # Hiding the predict button initially
        self.predict_button.pack_forget()

        # The image preview
        self.image_label = tk.Label(self.bottom_frame, text="No Image Uploaded", font=("Helvetica", 12), fg="#ffffff",
                                    bg='#1768ac', width=60, height=20, relief="solid", bd=2,
                                    highlightbackground="#ffffff", highlightcolor="#ffffff", highlightthickness=2)
        self.image_label.pack(pady=5)

        # The Prediction Result Area
        self.prediction_label = tk.Label(self.bottom_frame, text="Prediction Results:", font=("Helvetica", 16, 'bold'),
                                         fg="#ffffff", bg='#1768ac')
        self.prediction_label.pack(pady=10)

        self.result_box = tk.Label(self.bottom_frame, text="", font=("Helvetica", 12), fg="#ffffff", bg='#1768ac',
                                   wraplength=400, justify="center")
        self.result_box.pack(pady=10)

        # File path
        self.file_path = None

    # Uploading and displaying image
    @log_method_call
    def upload_image(self):
        self.file_path = filedialog.askopenfilename()

        if not self.file_path:
            messagebox.showerror("Error", "Please upload an image!")
            return

        print(f"Image path: {self.file_path}")

        # Displaying image before Prediction
        try:
            self.display_image(self.file_path)
        except Exception as e:
            print(f"Error displaying image: {e}")
            messagebox.showerror("Error", f"Failed to display image: {e}")

        # Showing the Predict button once an image is uploaded
        self.predict_button.pack(pady=10)

    # Handling the prediction process
    @log_method_call
    def predict_image(self):
        if not self.file_path:
            messagebox.showerror("Error", "No image uploaded!")
            return

        # Getting Predictions from AI Model
        predictions = self._predict_image(self.file_path)

        # Updating image with labels based on prediction
        self.label_image(self.file_path, predictions)

        # Displaying the prediction results
        result_text = "\n".join([f"{p[1]}: {p[2] * 100:.2f}%" for p in predictions])
        self.result_box.config(text=result_text)

    # Displaying the image before prediction
    def display_image(self, img_path):
        print("Loading image for display...")

        # Trying to open and display the image
        img = Image.open(img_path)
        img.thumbnail((400, 400))

        # Debug image size and format
        print(f"Image size: {img.size}, format: {img.format}")

        img = ImageTk.PhotoImage(img)

        # Force size of the image label
        self.image_label.config(width=img.width(), height=img.height())

        # Updating the label with the image
        self.image_label.config(image=img, text="")
        self.image_label.image = img

    # Adding label on the image
    def label_image(self, img_path, predictions):
        img = Image.open(img_path)
        draw = ImageDraw.Draw(img)

        try:
            font = ImageFont.truetype("arial.ttf", 30)
        except IOError:
            font = ImageFont.load_default()

        # Getting the top prediction
        top_prediction = predictions[0][1]
        label_text = f"Predicted: {top_prediction}"

        # Adding label to image using textbbox to calculate size
        text_bbox = draw.textbbox((0, 0), label_text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]

        # Drawing a rectangle behind the text for better visibility
        draw.rectangle([0, 0, text_width + 20, text_height + 20], fill="black")
        draw.text((10, 10), label_text, font=font, fill="white")

        # Saving the labeled image in memory for Tkinter display
        img.thumbnail((400, 400))
        img = ImageTk.PhotoImage(img)

        # Updating the label with the new image with label
        self.image_label.config(image=img, text="")
        self.image_label.image = img


# Main
if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
