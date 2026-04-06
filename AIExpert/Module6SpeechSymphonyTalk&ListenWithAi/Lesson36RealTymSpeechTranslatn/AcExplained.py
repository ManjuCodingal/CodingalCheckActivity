import speech_recognition as sr # This library is used for converting spoken language into text (speech recognition).
# Important Classes:
# Recognizer: A class that listens to audio input and processes it.
# Microphone: A class that handles microphone input.
# API Integration:
# Uses Google’s Web Speech API for recognizing speech.
import pyttsx3 # This library is used for text-to-speech functionality, enabling the computer to read out loud text that is passed to it.
# Important Classes and Methods:
# pyttsx3.init(): Initializes the speech engine.
# engine.setProperty(): Used to set properties such as speech rate and voice.
# engine.say(): Speaks the given text.
# engine.runAndWait(): Runs the speech engine to complete the speaking task.
from googletrans import Translator  # Google Translate API. Google Translate API library used to translate text between different languages.
# Important Classes and Methods:
# Translator(): Initializes a translator object.
# translator.translate(): Translates the text from source language to target language.

# Initialize text-to-speech engine
def speak(text, language="en"):
# This function converts text into speech, and it takes two parameters: the text to be spoken and the language of the speech.
    engine = pyttsx3.init() # pyttsx3.init(): Initializes the pyttsx3 engine.
    engine.setProperty('rate', 150)  # Speed of speech. engine.setProperty('rate', 150): Adjusts the rate of speech (speed). 150 is a moderate speed.

    voices = engine.getProperty('voices') # engine.getProperty('voices'): Retrieves available voices on the system. This helps in setting the voice for different languages (English or other languages).    

    # Set voice for English or other language if supported by pyttsx3
    if language == "en": # Sets the voice to be used. If the language is English ("en"), it selects the first available voice (usually English). If the language is something else, it selects the second available voice.
        engine.setProperty('voice', voices[0].id)  # Default English voice
# voices[0].id is typically the default voice (usually English).
# voices[1].id would be another voice (could be another language or accent) available on the system.
    else:
        engine.setProperty('voice', voices[1].id)  # Fallback to another voice if available    

    engine.say(text) # engine.say(text): Converts the text into speech.
    engine.runAndWait() # engine.runAndWait(): Processes the speech request, making sure the engine completes the task before moving on.

# Speech-to-Text: Recognize spoken language (English)
def speech_to_text():
# Convert Speech to Text. This function listens to the user’s speech using the microphone and converts it into text.
    recognizer = sr.Recognizer() # sr.Recognizer(): Initializes the recognizer object, which is responsible for processing audio data.
    with sr.Microphone() as source: # sr.Microphone() as source: Initializes the microphone as the audio source. This context manager ensures that the microphone is properly initialized and closed.
        print("???? Please speak now in English...")
        audio = recognizer.listen(source) # recognizer.listen(source): Listens for speech and stores the audio input in the audio variable.

    try: # Uses Google’s Web Speech API (recognizer.recognize_google) to process the audio and convert it into text.
        print("???? Recognizing speech...")

        text = recognizer.recognize_google(audio, language="en-US")  # Use English for speech recognition. recognizer.recognize_google(audio, language="en-US"): Sends the audio data to Google’s servers and returns the recognized text. The language is set to English ("en-US").

        print(f"✅ You said: {text}")

        return text # The transcribed text is printed and returned.

    except sr.UnknownValueError: # Catches errors that may occur during the speech recognition process.
# sr.UnknownValueError: This error is raised when the speech is not recognized (e.g., due to background noise or unclear speech).
        print("❌ Could not understand the audio.")

    except sr.RequestError as e: # sr.RequestError: This error is raised when there is an issue with the API request, such as no internet connection.

        print(f"❌ API Error: {e}") 

    return ""  # The function returns an empty string "" if there are errors.

# Translate text using Google Translate API. This function translates the given text into the target language using the Google Translate API.
def translate_text(text, target_language="es"):  # Default target language is Spanish (es)
# text: The text to be translated.
# target_language: The language code to which the text should be translated (defaults to "es" for Spanish).

    translator = Translator() 

    translation = translator.translate(text, dest=target_language) # # translator.translate(text, dest=target_language): Translates the text to the specified language. The dest parameter specifies the target language.

    print(f"???? Translated text: {translation.text}") # The translated text. print(f"🌐 Translated text: {translation.text}"): Displays the translated text for the user.

    return translation.text

# Display language options to the user

def display_language_options(): # Supported languages are identified using language codes like "es" (Spanish), "fr" (French), etc.
# Displays lists of available translation languages to user. The function simply prints out the available languages and prompts the user to select one by entering a number corresponding to the language. The function returns the language code for the selected language, which is used later for translation.
    print("???? Available translation languages: ")

    print("1. Hindi (hi)")

    print("2. Tamil (ta)")

    print("3. Telugu (te)")

    print("4. Bengali (bn)")

    print("5. Marathi (mr)")

    print("6. Gujarati (gu)")

    print("7. Malayalam (ml)")

    print("8. Punjabi (pa)")



    # User selects language

    choice = input("Please select the target language number (1-8): ")

    language_dict = {

        "1": "hi",

        "2": "ta",

        "3": "te",

        "4": "bn",

        "5": "mr",

        "6": "gu",

        "7": "ml",

        "8": "pa"

    }
# A language dictionary is used to map the user’s choice (number) to the corresponding language code. The function returns the language code based on the user’s input, defaulting to Spanish ("es") if the input is invalid.

    return language_dict.get(choice, "es")  # Default to Spanish if invalid input



# Main function to combine all steps

def main():
# Steps:
# Step 1: The user selects the target language using display_language_options().
# Step 2: The program listens for spoken input using speech_to_text() and stores the recognized text in original_text.
# Step 3: If speech recognition is successful, the text is translated into the selected target language using translate_text().
# Step 4: The translated text is spoken aloud using the speak() function.

    # Step 1: Display language options and get user's choice
    target_language = display_language_options()

    # Step 2: Speech-to-Text (recognizing English speech)
    original_text = speech_to_text()

    if original_text:
        # Step 3: Translate to selected target language
        translated_text = translate_text(original_text, target_language=target_language)

        # Step 4: Text-to-Speech (Translate output and speak it)
        speak(translated_text, language="en")  # Speak the translation in English

        print("✅ Translation spoken out!")

if __name__ == "__main__": # Ensures that the main() function is executed when the script is run directly.
# This is a standard Python construct that prevents the main function from running if the script is imported as a module in another program.

    main()
# Key Features and Workflow
# 1. Speech-to-Text:
# The speech_to_text() function listens to the user’s spoken input, converts it into text using Google’s Speech Recognition API, and handles potential errors gracefully.

# 2. Text Translation:
# The recognized text is translated to the user’s selected language using the googletrans library’s Translator class.

# 3. Text-to-Speech:
# The translated text is read aloud in English using pyttsx3.

# 4. Interactive User Interface:
# The user selects the language for translation, provides speech input, and receives a spoken translation as output. This interaction is looped until the user exits.
# Conclusion
# This activity uses Python’s libraries to implement a fully interactive speech-to-speech translation system, handling input, translation, and output all within a simple program.
