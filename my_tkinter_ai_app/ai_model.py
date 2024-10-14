from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
from PIL import Image, ImageOps
import numpy as np


class AIModel:
    def __init__(self):
        # Loading the pretrained MobileNetV2 model with ImageNet weights
        self.model = MobileNetV2(weights='imagenet')

    def predict(self, img_path):
        # Opening the image and preprocessing it
        img = Image.open(img_path)
        # Resizing the image to 224x224
        img = ImageOps.fit(img, (224, 224), Image.Resampling.LANCZOS)
        # Converting the image to numpy array
        img_array = np.asarray(img)
        # Adding the batch dimension
        img_array = np.expand_dims(img_array, axis=0)
        # Preprocessing the image for MobileNetV2
        img_array = preprocess_input(img_array)
        # Making the predictions
        predictions = self.model.predict(img_array)
        # Only getting the top 3 predictions
        decoded_predictions = decode_predictions(predictions, top=3)[0]
        return decoded_predictions

