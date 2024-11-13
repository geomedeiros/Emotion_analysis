import cv2
import numpy as np
from deepface import DeepFace
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/detect_emotion', methods=['POST'])
def detect_emotion():
    # Verifica se uma imagem foi enviada na requisição
    if 'image' not in request.files:
        return jsonify({"error": "Nenhuma imagem foi enviada"}), 400

    # Lê a imagem enviada
    file = request.files['image']
    image_data = np.frombuffer(file.read(), np.uint8)
    frame = cv2.imdecode(image_data, cv2.IMREAD_COLOR)

    try:
        # Detecta emoção usando DeepFace
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        emotion = result[0].get('dominant_emotion', "Emoção não detectada")
        return jsonify({"emotion": emotion})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Inicializa o servidor Flask
if __name__ == '__main__':
    app.run(debug=True)
