import speech_recognition as sr # Lib used for converting speech to text, allowing the assistant to understand spoken commands.
import pyttsx3 # lib used for text-to-speech conversion, enabling the assistant to respond verbally to the user.
from datetime import datetime # Used to get the current time, allowing the assistant to provide time-related responses when asked.

def speak(text):
# • Purpose: This function takes a string (text) as input and makes the assistant speak it out loud.
# • Details:
# pyttsx3.init() initializes the text-to-speech engine.
# engine.setProperty('rate', 150) sets the speed of speech to 150 words per minute.
# engine.say(text) converts the text into speech.
# engine.runAndWait() processes the speech and waits until it finishes.
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()

def get_audio():
# • Purpose: This function listens for the user's speech and converts it into text using Google’s speech recognition API.
# • Details:
# r = sr.Recognizer() creates an instance of the recognizer.
# with sr.Microphone() as source: sets up the microphone to listen for the user's speech.
# audio = r.listen(source) captures the audio input from the microphone.
# r.recognize_google(audio) sends the captured audio to Google's speech-to-text API to get the recognized text.
# If successful, it returns the recognized text in lowercase. If it fails, it prints an error message and returns an empty string.
# Error Handling:
# ▪ **sr.UnknownValueError**: Raised when speech is not understood.  
# ▪ **sr.RequestError**: Raised when there’s an issue with the API request (like network problems).
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("???? Speak now...")
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio)
            print(f"✅ You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("❌ Could not understand.")
        except sr.RequestError as e:
            print(f"❌ API Error: {e}")
    return ""

def respond_to_command(command):
# • Purpose: This function processes the recognized command and makes the assistant respond accordingly.
# • Details:
# The if-elif blocks check if specific keywords (like "hello", "your name", or "time") exist in the command string.
# If the command matches one of the conditions:
# ▪ "hello": Greets the user.  
# ▪ "your name": Provides the assistant's name.  
# ▪ "time": Tells the current time using **datetime.now().strftime("%H:%M")**.  
# ▪ "exit" or "stop": Exits the program with a goodbye message.  
# ▪ If none of the conditions are met, it informs the user that it doesn’t understand the command.  
# The function returns False if the command is "exit" or "stop", causing the program to terminate. Otherwise, it returns True to continue listening for more commands.
    if "hello" in command:
        speak("Hi there! How can I help you today?")
    elif "your name" in command:
        speak("I am your Python voice assistant.")
    elif "time" in command:
        now = datetime.now().strftime("%H:%M")
        speak(f"The time is {now}")

    elif "exit" in command or "stop" in command:
# If the user says "exit" or "stop", the assistant will say "Goodbye!" and terminate the loop, ending the program.
        speak("Goodbye!")
        return False
    else:
        speak("I'm not sure how to help with that.")
    return True



def main():
# • Purpose: This is the main function that runs the entire voice assistant.
# • Details:
# speak("Voice assistant activated. Say something!") prompts the user that the assistant is ready to receive commands.
# while True: creates an infinite loop to keep listening for user input until the "exit" or "stop" command is given.
# command = get_audio() listens for the user's voice command.
# if command and not respond_to_command(command): checks if a valid command is received and processes it through the respond_to_command() function. If the response is False (i.e., the user wants to exit), it breaks out of the loop and ends the program.
    speak("Voice assistant activated. Say something!")

    while True:
        command = get_audio()
        if command and not respond_to_command(command):
            break

if __name__ == "__main__":

    main()

# How the Program Works:
# The program starts by speaking, "Voice assistant activated. Say something!"
# The assistant listens for a voice command.
# If the command matches specific phrases like "hello", "your name", or "time", it will respond accordingly.
# If the command is "exit" or "stop", the assistant will say "Goodbye!" and stop listening.
# If the command is not recognized, the assistant will say, "I'm not sure how to help with that."

# Error Handling:
# • If the speech recognition fails (e.g., unclear speech or no internet), the assistant handles the error gracefully by printing "❌ Could not understand" or "❌ API Error" without crashing the program.

# Extensions:
# This program can be extended by:
# • Adding more voice commands and responses.
# • Integrating additional APIs (e.g., for weather updates, controlling smart devices).
# • Adding more robust error handling for various edge cases.
# Conclusion:
# This is a simple yet effective voice assistant using Python that demonstrates the integration of speech recognition and text-to-speech functionalities. It showcases the ability to recognize voice commands, respond with speech, and handle basic commands like telling the time and greetings.    