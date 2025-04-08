from flask import Flask, render_template, request, jsonify
import numpy as np
import tensorflow as tf
from PIL import Image
import base64
import io
import re

app = Flask(__name__)
model = tf.keras.models.load_model('modelo_simple.h5')  # Cargar el modelo entrenado

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Obtener la imagen desde la solicitud
    data = request.json['image']
    
    # Quitar el encabezado de la imagen base64
    image_data = re.sub('^data:image/.+;base64,', '', data)
    
    # Decodificar la imagen base64
    decoded = base64.b64decode(image_data)
    
    # Abrir la imagen con PIL y convertirla a escala de grises
    image = Image.open(io.BytesIO(decoded)).convert('L')  # Convertir a escala de grises
    image = image.resize((28, 28))  # Redimensionar a 28x28 píxeles

    # Convertir la imagen a un arreglo de numpy
    img_array = np.array(image)
    
    # Si la imagen tiene un fondo blanco y el número es negro, no es necesario invertirla
    img_array = 255 - img_array  # Invertir si el fondo es blanco y el número negro

    # Normalizar la imagen (convertir los valores a [0, 1])
    img_array = img_array / 255.0
    
    # Asegurarnos de que la imagen tiene la forma correcta (1, 28, 28, 1)
    img_array = img_array.reshape(1, 28, 28, 1)

    # Realizar la predicción
    prediction = model.predict(img_array)
    
    # Obtener el dígito predicho (el índice con la mayor probabilidad)
    predicted_digit = int(np.argmax(prediction))
    
    # Retornar el resultado como un JSON
    return jsonify({'prediction': predicted_digit})

if __name__ == '__main__':
    app.run(debug=True)
