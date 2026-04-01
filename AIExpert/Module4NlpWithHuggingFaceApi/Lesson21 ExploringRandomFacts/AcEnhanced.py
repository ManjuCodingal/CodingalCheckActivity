import requests
import time

url = "https://uselessfacts.jsph.pl/api/v2/facts/random?language=en"

shown_facts = set()
fact_count = 0

def get_random_fact():
    global fact_count
    
    try:
        response = requests.get(url, timeout=5)
        
        if response.status_code == 200:
            fact_data = response.json()
            fact = fact_data['text']
            
            # Avoid duplicate facts
            if fact in shown_facts:
                print("⚠️ Duplicate fact skipped!\n")
                return
            
            shown_facts.add(fact)
            fact_count += 1
            
            print(f"\n💡 Fact #{fact_count}:")
            print(fact)
            
            # Save to file
            with open("facts.txt", "a") as file:
                file.write(fact + "\n")
                
        else:
            print("❌ Failed to fetch fact (Status Code:", response.status_code, ")")
    
    except requests.exceptions.RequestException:
        print("🌐 Network error! Please check your connection.\n")


def auto_mode():
    print("\n⏱ Auto mode started (Ctrl+C to stop)\n")
    try:
        while True:
            get_random_fact()
            time.sleep(5)
    except KeyboardInterrupt:
        print("\n⛔ Auto mode stopped.\n")


# Main menu loop
while True:
    print("\n===== FACT GENERATOR MENU =====")
    print("1. Get a fact")
    print("2. Auto mode (fact every 5 sec)")
    print("3. Show total facts fetched")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        get_random_fact()
    
    elif choice == "2":
        auto_mode()
    
    elif choice == "3":
        print(f"\n📊 Total unique facts shown: {fact_count}")
    
    elif choice == "4":
        print("👋 Goodbye!")
        break
    
    else:
        print("❗ Invalid choice. Try again.")


# 🔥 What’s New (Explained)
# 🛡 Error Handling
# try:
#     response = requests.get(url, timeout=5)
# Prevents crashes if internet fails

# 🔁 Duplicate Prevention
# shown_facts = set() - set is a python data structure that avoids duplicates. (Python data structure includes : lists, tuples, dictionary, set, array)

# Stores previously shown facts

# 💾 File Saving
# with open("facts.txt", "a") as file:
# Saves all facts to a file

# 📊 Fact Counter
# fact_count += 1
# Tracks how many facts you've seen

# ⏱ Auto Mode
# Fetches a fact every 5 seconds automatically

# 🎮 Menu System
# Makes your app interactive and user-friendly        