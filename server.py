"""
server.py

A Flask application for detecting emotions from text input.
The application provides an endpoint to analyze text and return emotion scores.
"""

from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/emotion_detector', methods=['POST'])
def emotion_detector_endpoint():
    """
    Endpoint to detect emotions from text.
    
    Expects a JSON body with a 'text' field.
    Returns a JSON response with emotion scores and dominant emotion,
    or an error message if the input is invalid.
    """
    data = request.json
    text_to_analyze = data.get('text', '').strip()
    result = emotion_detector(text_to_analyze)
    # Handle case where dominant_emotion is None
    if result['dominant_emotion'] is None:
        return jsonify({'error': 'Invalid text! Please try again!'}), 400
    return jsonify(result)
if __name__ == '__main__':
    app.run(debug=True)
