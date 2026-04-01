import requests # Requests library in python. This allows python to send HTTP requests and interact with web services. It simplifies the process of making requests and handling responses.

# Technology category fact endpoint
url = "https://uselessfacts.jsph.pl/api/v2/facts/random?language=en" # random facts api: offers random facts about various topics

# Function to fetch and display a random technology-related fact
def get_random_technology_fact():
    response = requests.get(url)
    if response.status_code == 200:
        fact_data = response.json() # parse JSON response
        print(f"Did you know? {fact_data['text']}") # print the text; accessing individual piece of info using the keys after parsing the data.

# Eg for accessing values in case of nested data : simply chain the keys
# fact_data = response.json()
# print(fact_data['response']['fact'])  # Outputs: Honey never spoils.

    else:
        print("Failed to fetch fact")

# Main loop to interact with the user
while True:
    user_input = input("Press Enter to get a random technology fact or type 'q' to quit...")
    if user_input.lower() == 'q':
        break
    get_random_technology_fact()