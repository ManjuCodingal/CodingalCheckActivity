# “trivia” refers to interesting factual questions or facts—usually small, standalone pieces of knowledge that can be asked as a question.
import requests
import random
import html

# Education-focused categories (General Knowledge, Science, History, etc.)
EDUCATION_CATEGORY_ID = 9  # General Knowledge category (most educational)

# 17 Science & Nature
# 18 Computers
# 19 Mathematics
# 22 Geography
# 23 History
# 10 Books
# 11 Film
# 12 Music
# 21 Sports

API_URL = f"https://opentdb.com/api.php?amount=10&category={EDUCATION_CATEGORY_ID}&type=multiple"
# Why the length of questions is 10? amount=10 in api url => API sends → 10 questions; questions list contains → 10 items
# type=multiple → Multiple choice questions => Each question has 1 correct answer + 3 incorrect answers (so 4 options total).
# 💡 Tip: If you want True/False quizzes instead, you can change:
# &type=boolean
# Then options will only have 2 items. But then may have to change some sections of code to handle correct/incorrect answers...

def get_education_questions():
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json() # converts the HTTP response from the OpenTDB API into a Python dictionary so the program can work with it easily. The API sends data in JSON format, which looks like a text string.
# response.json() parses this JSON string into a Python object:
# JSON object → Python dictionary (dict)
# JSON array → Python list (list)

        if data['response_code'] == 0 and data['results']:
# data['response_code'] == 0 👉 This checks API status, 👉 “API call was successful”
# | Value | Meaning                        |
# | ----- | ------------------------------ |
# | `0`   | ✅ Success (questions received) |
# | `1`   | ❌ No results                   |
# | `2`   | ❌ Invalid parameters           |
# | `3`   | ❌ Token error                  |
# | `4`   | ❌ No questions left            |

# data['results'] 👉 This checks if questions actually exist
# data['results'] is a list of questions
            return data['results']
    return None

def run_quiz():
    questions = get_education_questions()
    if not questions:
        print("Failed to fetch educational questions")
        return
    score = 0
    print("Welcome to the Education Quiz!\n")

    for i, q in enumerate(questions, 1):
# enumerate() is a Python function that:
# loops through a list and gives index + value together
# EXAMPLE:: enumerate(questions, 1)
# 👉 Start counting from 1 instead of 0
# OUTPUT= 1 Q1
# 2 Q2
# 3 Q3

# 🔹 i
# 👉 The question number (1, 2, 3...)
# 🔹 q
# 👉 The actual question data (dictionary)

        # Decode HTML entities and prepare options
        # Fix special characters using unescape()
# unescape() is to convert escaped/encoded text back into its original, readable form.
# Why do we even need escaping?
# In many contexts, certain characters have special meaning or might break things. So they get escaped (encoded):
# In HTML: < → &lt; (so it doesn’t get treated as a tag)
# In URLs: space → %20 (since spaces aren’t allowed in URLs)
# In strings: newline → \n (so it can be stored safely in one line)

# let a question looks like:: q = {
#     'question': "What is 2+2?",
#     'correct_answer': "4",
#     'incorrect_answers': ["3", "5", "6"]
# }
        question = html.unescape(q['question']) # 👉 API sometimes returns text like: "What is 5 &amp; 3?"
        # 👉 html.unescape() converts: &amp; → &
        # ✔ Makes question readable
        correct = html.unescape(q['correct_answer'])
        incorrects = [html.unescape(a) for a in q['incorrect_answers']]
        # Create and shuffle options
        options = incorrects + [correct] # Combine options. eg incorrects = ["2", "3", "5"]
# correct = "4"
# options = ["2", "3", "5", "4"]
        random.shuffle(options) # 👉 Mixes the order randomly

        # Display question
        print(f"Question {i}: {question}")
        for idx, option in enumerate(options, 1): # 1️⃣ enumerate(options, 1) 👉 Loops through the list with numbering starting from 1
# 2️⃣ idx 👉 This is the option number
# 1, 2, 3, 4
# 3️⃣ option 👉 This is the actual answer text
# "2", "3", "4", etc.

            print(f"  {idx}. {option}") # Prints in formatted style:
#   1. 2
#   2. 3
#   3. 4
#   4. 5

        # Get and validate answer
        while True: 
# 👉 Keeps asking until user enters:
# A number
# Between 1 and 4
            try:
                choice = int(input("\nYour answer (1-4): "))
                if 1 <= choice <= 4: # 👉 Ensures: Only numbers 1 to 4 allowed
                    break
            except ValueError: # Eg if user enters: abc
                pass
            print("Invalid input! Please enter 1-4")

        # Check answer
        if options[choice-1] == correct: 
# 🧠 Why choice - 1?
# User enters: 1, 2, 3, 4
# List index starts from: 0 , 👉 So:  
# | User input | Index |
# | ---------- | ----- |
# | 1          | 0     |
# | 2          | 1     |
# | 3          | 2     |
# | 4          | 3     |
         
            print("✓ Correct!\n")
            score += 1
        else:
            print(f"✗ Wrong! Correct answer: {correct}\n")

    print(f"Final Score: {score}/{len(questions)}")
    print(f"Percentage: {score/len(questions)*100:.1f}%")

if __name__ == "__main__":
    run_quiz()