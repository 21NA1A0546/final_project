import requests
import json

def emotion_detector(text_to_analyze):
    # Define the URL for the emotion detection API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Set the headers with the required model ID for the API
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Create the payload with the text to be analyzed
    payload = {"raw_document": {"text": text_to_analyze}}
    
    try:
        # Make a POST request to the API with the payload and headers
        response = requests.post(url, json=payload, headers=headers)
        
        # Check if the request was successful
        if response.status_code != 200:
            print(f"Error: API request failed with status code {response.status_code}")
            return None
        
        # Convert the response text into a dictionary
        response_dict = json.loads(response.text)
        
        # Print the response for debugging
        print("API Response:", response_dict)
        
        # Ensure the expected structure is present in the response
        if 'emotionPredictions' not in response_dict or not response_dict['emotionPredictions']:
            print("Error: 'emotionPredictions' key not found or empty in the response")
            return None
        
        # Extract the emotions and their scores from the first item in the emotionPredictions list
        emotions = response_dict['emotionPredictions'][0]['emotion']
        anger_score = emotions.get('anger', 0)
        disgust_score = emotions.get('disgust', 0)
        fear_score = emotions.get('fear', 0)
        joy_score = emotions.get('joy', 0)
        sadness_score = emotions.get('sadness', 0)
        
        # Determine the dominant emotion based on the highest score
        emotion_scores = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score
        }
        
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
        
        # Return the formatted output
        return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }
    
    except requests.exceptions.RequestException as e:
        print(f"Error: Failed to connect to the API - {e}")
        return None

