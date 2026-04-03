import requests
import json

def emotion_detector(text_to_analyze):
    """
    Analyzes text using the Watson NLP API via POST request.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    # Send the POST request
    response = requests.post(url, json=myobj, headers=header)
    
    # Task 7: Handling status code 400 (Blank Input)
    if response.status_code == 400:
        return {
            'anger': None, 
            'disgust': None, 
            'fear': None, 
            'joy': None, 
            'sadness': None, 
            'dominant_emotion': None
        }

    # Format the response
    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    anger = emotions['anger']
    disgust = emotions['disgust']
    fear = emotions['fear']
    joy = emotions['joy']
    sadness = emotions['sadness']
    
    # Task 3: Identify dominant emotion
    emotion_list = [anger, disgust, fear, joy, sadness]
    emotion_names = ['anger', 'disgust', 'fear', 'joy', 'sadness']
    dominant_emotion = emotion_names[emotion_list.index(max(emotion_list))]
    
    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
    }
from transformers import pipeline

# Load the model once at the top of the file to be efficient
# The first run will download the model (~300MB) to your machine
emotion_classifier = pipeline(
    'text-classification', 
    model='j-hartmann/emotion-english-distilroberta-base', 
    return_all_scores=True
)

def emotion_detector(text_to_analyze):
    """
    Analyzes text emotion locally using Hugging Face.
    Maintains compatibility with existing Flask server and Unit Tests.
    """
    # Task 7: Handle Blank/Invalid Input
    if not text_to_analyze or not text_to_analyze.strip():
        return {
            'anger': None, 'disgust': None, 'fear': None, 
            'joy': None, 'sadness': None, 'dominant_emotion': None
        }
    
    # Run the local classifier
    results = emotion_classifier(text_to_analyze)[0]
    
    # Map Hugging Face labels to your required keys
    # Hugging Face provides: anger, disgust, fear, joy, neutral, sadness, surprise
    emo_map = {res['label']: res['score'] for res in results}
    
    # Extract only the 5 required emotions for the course
    output = {
        'anger': emo_map.get('anger', 0),
        'disgust': emo_map.get('disgust', 0),
        'fear': emo_map.get('fear', 0),
        'joy': emo_map.get('joy', 0),
        'sadness': emo_map.get('sadness', 0)
    }
    
    # Task 3: Identify dominant emotion
    dominant_emotion = max(output, key=output.get)
    output['dominant_emotion'] = dominant_emotion
    
    return output
