<<<<<<< HEAD
# EmotionD
=======
Emotion Detection System (Local Transformer Edition)
Project Description
This is a comprehensive AI-based Web Application developed as part of the Software Engineering curriculum. Originally designed for Watson NLP, this version has been upgraded to use a Local Transformer Model (j-hartmann/emotion-english-distilroberta-base) via the Hugging Face library.

This architectural shift ensures 100% availability by removing external API dependencies, allowing the application to perform fine-grained emotion analysis—identifying anger, disgust, fear, joy, and sadness—entirely on the host machine.

Key Features
Backend: Python 3.13 and Flask.

AI Engine: Local Hugging Face Transformer pipeline (DistilRoBERTa).

Offline Capable: No external API calls or internet required after the initial model download.

Testing: Automated unit testing using the unittest framework.

Code Quality: Static code analysis achieving a 10/10 Pylint score.

Project Structure
Plaintext
.
├── EmotionDetection/        # Core logic package
│   ├── __init__.py          # Package initializer
│   └── emotion_detection.py # Local Model loading and formatting logic
├── static/                  # Web assets
│   ├── mywebscript.js       # AJAX handling
│   └── style.css            # Responsive UI styling
├── templates/               # Frontend HTML
│   └── index.html           # Main user interface
├── server.py                # Flask application deployment script
├── test_emotion_detection.py# Unit testing suite
└── README.md                # Project documentation
Installation & Setup
Clone the repository:

Bash
git clone <your-github-repo-url>
cd EmotionD
Install Dependencies:
This project requires flask for the web server and transformers with torch for the AI model:

Bash
pip install flask transformers torch
Run the Application:
Execute the server script. Note: The first run will take a moment to download the model (~300MB).

Bash
python server.py
Access the Web UI:
Open your browser and navigate to http://127.0.0.1:5000.

Testing & Quality Assurance
Unit Tests: Run python test_emotion_detection.py to verify that the local model correctly identifies dominant emotions for test strings.

Static Analysis: Run pylint server.py and pylint EmotionDetection/emotion_detection.py to verify PEP8 compliance.

Error Handling: The system is designed to handle blank inputs gracefully, returning None values and a user-friendly "Invalid text" message.
>>>>>>> 9ce26ed (Initial commit of Emotion Detection System)
