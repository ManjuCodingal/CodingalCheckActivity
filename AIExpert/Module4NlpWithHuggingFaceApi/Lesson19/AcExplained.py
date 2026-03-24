# pip install requests

import requests # requests library to fetch data from public api (eg. joke api, trivia api) and display the result in a user friendly way.
# “trivia” refers to interesting factual questions or facts—usually small, standalone pieces of knowledge that can be asked as a question.

def get_random_joke():
    """Fetch a random joke from the Official Joke API."""
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url) # fetch a joke from the joke api
# requests.get(url) → Sends a GET request to the specified url.
# GET requests are used to fetch data from a serve
    
# response → An object containing the server’s reply, including:
# response.status_code → HTTP status (200 = OK, 404 = Not Found)
# response.text → Response body as a string
# response.json() → Response parsed as JSON (if the server sends JSON)    
    if response.status_code == 200:
        # One line to print the JSON response:
        print(f"Full JSON Response: {response.json()}")
        
        joke_data = response.json()
        return f"{joke_data['setup']} - {joke_data['punchline']}" # extract the setup and punchline from the JSON response and print them
    else:
        return "Failed to retrieve joke."

def main():
    print("Welcome to the Random Joke Generator!")
    
    while True:
        user_input = input("Press Enter to get a new joke, or type 'q'/'exit' to quit: ").strip().lower()
        
        if user_input in ("q", "exit"):
            print("Goodbye!")
            break
        
        joke = get_random_joke()
        print(joke)

if __name__ == "__main__": # Every Python file (module) has a special built-in variable called __name__
    main() # Directly run (python file.py)
# Run main() if this file is executed directly.