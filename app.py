from flask import Flask, render_template, request, jsonify
import google.generativeai as genai 
import os

app = Flask(__name__) 
#Configure the Google AI SDK with your API key 
genai.configure(api_key=os.getenv('GOOGLE_API_KEY')) 
#Initialize the Gemini model 
model = genai.GenerativeModel('gemini-pro') 

@app.route('/') 
def index(): 
    #For simplicity, we'll use a predefined list of languages 
    languages = { 
        "es": "Spanish", 
        "fr": "French", 
        "de": "German", 
        "it": "Italian", 
        "ja": "Japanese", 
        "ko": "Korean", 
        "zh": "Chinese (Simplified)",
        "te": "Telugu"
    } 
    return render_template('index.html', languages=languages)

@app.route('/process', methods=['POST'])
def process(): 
    input_text = request.form['text'] 
    target_language = request.form['language'] 

    try:
       #Correct the text
       correction_prompt = (
            f"Please correct any grammatical or spelling errors in the following text, "
            f"but keep the meaning the same: '{input_text}'"
        )
       correction_response = model.generate_content(correction_prompt) 
       corrected_text = correction_response.text 

       # Check if the corrected text is identical to the input text
       if corrected_text.strip().lower() == "no errors found in the provided text.":
            corrected_text = input_text  # Use the original text if no corrections
       
       #Translate the corrected text 
       translation_prompt = f"Translate the following text to {target_language}: '{corrected_text}'" 
       translation_response = model.generate_content(translation_prompt) 
       translated_text = translation_response.text 
    
       return jsonify({
           'corrected': corrected_text,
           'translated': translated_text,
           'success': True 
    })
    except Exception as e:
        return jsonify({
           'error': str(e), 
           'success': False
    })

if __name__ == '__main__': 
    app.run(debug=True)