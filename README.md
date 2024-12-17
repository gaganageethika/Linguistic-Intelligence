# Linguistic Intelligence

Linguistic Intelligence is a Flask-based web application that provides users with advanced text correction and translation capabilities. The application leverages Google's Gemini AI model to correct grammatical and spelling errors in user-inputted text and translate it into various target languages.

## Features
- **Text Correction**: Automatically detects and corrects grammatical and spelling errors while retaining the original meaning.
- **Language Translation**: Translates the corrected text into a wide range of supported languages.
- **Predefined Language Options**: Supports multiple languages, including Spanish, French, German, Japanese, Telugu, and more.

## How It Works
1. **User Input**: Enter text and select a target language.
2. **Correction**: The app uses Google's Gemini AI to correct grammatical errors.
3. **Translation**: The corrected text is translated into the selected language.
4. **Output**: Users receive both corrected and translated text.

## Technologies Used
- **Backend**: Flask (Python)
- **AI Model**: Google's Gemini AI
- **Frontend**: HTML templates (rendered using Flask)
- **APIs**: Google AI SDK

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/gaganageethika/linguistic-intelligence.git
    cd linguistic-intelligence
    ```
2. Install dependencies:
    ```bash
    pip install flask
    ```
3. Set up the Google API key:
    - Add your API key to an environment variable named `GOOGLE_API_KEY`.

4. Run the application:
    ```bash
    python app.py
    ```

5. Open your browser and visit `http://127.0.0.1:5000/`.

## Project Structure-
`app.py` Main Application File
`requirements.txt` Dependencies for the Project
`index.html` HTML file for the User Interface

## Future Enhancements
- Add more languages for translation.
- Improve UI/UX for a seamless user experience.
- Enable text-to-speech support for translated text.

## License
This project is open-source and available under the MIT License.


