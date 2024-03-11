#Taking Audio as input from user
import speech_recognition as sr

def record_audio():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something...")
        audio = recognizer.listen(source, timeout=7)

    return audio

def get_language_code():
    language_code = "ta"
    return language_code

def convert_audio_to_text(audio, language="en-US"):
    recognizer = sr.Recognizer()

    try:
        print("Converting audio to text...")
        response = recognizer.recognize_google(audio, show_all=True, language=language)
        if 'alternative' in response:
            result = response['alternative'][0]
            text = result['transcript']
            detected_language = result.get('language', None)
            
            return text, detected_language
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

if __name__ == "__main__":
    language_code = get_language_code()
    audio_data = record_audio()
    text_result, detected_language = convert_audio_to_text(audio_data, language=language_code)


#Translating the audio collected from the user into english text.

from googletrans import Translator
translator = Translator()
output = translator.translate(text_result, dest = "en")
print("Process Completed")
print("Translated text : ")
print("Query-->",output.text)
print("X-------Fetching Results based on query posted-------X")

#Searching Query in ChatGPT

import openai

openai.api_key = "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"

print("Fetching Results based on query posted...")
print("")
completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": output.text}])
print(completion.choices[0].message.content)
print("")
