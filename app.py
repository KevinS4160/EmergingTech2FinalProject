import streamlit as st
import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np

# Set page config
st.set_page_config(page_title="Emerging Technology 2 in CpE", layout="wide")

# Title and student details
st.title("Emerging Technology 2 in CpE")
st.markdown("""
Name:
- Kevin Roi A. Sumaya
- Daniela D. Rabang

Course/Section: CPE019/CPE32S5

Date Submitted: May 17, 2024
""")

# Load the trained model
@st.cache(allow_output_mutation=True)
def load_model():
    model = tf.keras.models.load_model("fashion_mnist_model.h5")
    return model

# Define the class names for fashion_MNIST
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

model = load_model()

# Streamlit app
st.title("Fashion Item Classification")
st.write("Upload an image to classify the type of fashion item.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

def import_and_predict(image_data, model):
    size = (28, 28)  # FashionMNIST images are 28x28
    image = ImageOps.fit(image_data, size)
    img = np.asarray(image.convert('L'))  # Convert image to grayscale
    img = np.expand_dims(img, axis=0)
    img = np.expand_dims(img, axis=-1)
    img = img / 255.0
    prediction = model.predict(img)
    return prediction

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    st.write("")
    st.write("Classifying...")

    prediction = import_and_predict(image, model)
    predicted_class = class_names[np.argmax(prediction)]
    confidence = np.max(prediction)

    st.write(f"Prediction: {predicted_class}")
    st.write(f"Confidence: {confidence:.2f}")
