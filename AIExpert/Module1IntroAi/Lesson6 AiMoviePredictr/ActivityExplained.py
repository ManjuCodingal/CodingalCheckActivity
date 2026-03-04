# Analyse mood and recommend movies based on genre, mood, and rating using TextBlob for sentiment analysis and pandas for data handling.

# Pandas is used to read csv file and filter data based on Genre and IMDB_Rating. TextBlob is used to analyze the sentiment of movie overviews to determine if they are positive, negative, or neutral. Colorama is used to add colored text output for better user experience in the terminal.

import time, pandas as pd
from textblob import TextBlob
from colorama import init, Fore

init(autoreset=True) # reset color after each print in terminal, to avoid formatting issues.

# TextBlob(text).sentiment.polarity returns a float in range -1.0 (negative) to 1.0 (positive) indicating the sentiment of the text. A value of 0 indicates neutral sentiment.
# time.sleep(seconds) is used to create a delay in the program, which can be used to simulate the AI "thinking" effect when generating recommendations. This can enhance the user experience by making it feel more interactive and engaging.It pausesexecution to create animation effects.

# Listing using Genres
# This loads dataset safely and creates a clean list of genre options for user. The try/except ensures the pgm fails safely if dataset file is missing, bcz nothing else can run without it.
# After loading genres is built by taking Genre column from dataset, splitting by comma, stripping whitespace, and creating a sorted set of unique genres. This allows the user to choose from valid genre options when requesting movie recommendations.
try: df = pd.read_csv("imdb_top_1000.csv") # loads dataset into a DataFrame named df
except FileNotFoundError:
    print(Fore.RED + "Error: The file 'imdb_top_1000.csv' was not found."); raise SystemExit # raise SystemExit is used to exit the program gracefully after printing the error message in red color using Colorama. This prevents further execution of the program when the required dataset file is missing, which would otherwise lead to errors later on when trying to access the data.

genres = sorted({g.strip() for xs in df["Genre"].dropna().str.split(", ") for g in xs}) # dropna() removes any missing values from the Genre column, str.split(", ") splits the genre string into a list of genres, and the set comprehension creates a unique set of genres by stripping whitespace. Finally, sorted() sorts the genres alphabetically for better user experience when displaying options. This allows the program to present a clean and organized list of genres for the user to choose from when requesting movie recommendations. 

def dots(): # for short animated '...' effect to simulate AI thinking. It denotes a pause in the program to enhance user experience by making it feel more interactive and engaging.
    for _ in range(3): print(Fore.YELLOW + ".", end="", flush=True); time.sleep(0.5) # end="" keeps the dots on the same line, flush=True ensures they appear immediately, and time.sleep(0.5) creates a half-second delay between each dot for a simple animation effect.

def senti(p): return "Positive 😊" if p > 0 else "Negative 😞" if p < 0 else "Neutral 😐"

def recommend(genre=None, mood=None, rating=None, n=5): # This filters movies by genre and rating, checks content overview and returns upto n recommendations that match the users preferences.
    d = df
    # If genre is provided, it keeps only movies whose Genre text contains that genre (case-insensitive) and ignores missing genre values safely.
    if genre: d = d[d["Genre"].str.contains(genre, case=False, na=False)] # case=False makes genre matching case-insensitive (Drama matches drama)
    # na=False prevents errors when Genre has missing values

    # If rating is provided, it keeps only movies whose IMDB_Rating meets or exceeds the threshold.
    if rating is not None: d = d[d["IMDB_Rating"] >= rating]
    # If filtering removes everything, it returns a clear message instead of failing.
    if d.empty: return "No suitable movie recommendations found." # d.empty avoids running sentiment scoring when no movies remain

    # The remaining movies are shuffled using sample(frac=1) so users get variety on repeated runs.
    d, need_nonneg, out = d.sample(frac=1).reset_index(drop=True), bool(mood), [] # sample(frac=1) shuffles rows; frac=1 means shuffle 100% of the rows
    # reset_index(drop=True) cleans the index after shuffling for smooth iteration
    
    # Then the function loops through the shuffled list, extracts the Overview, skips missing overviews, computes sentiment polarity using TextBlob, and applies a simple mood rule: when mood is provided, it allows only movies whose overview polarity is neutral/positive (pol >= 0). It collects up to n movies and returns them as a list of (title, polarity) tuples.
    for _, r in d.iterrows():
        ov = r.get("Overview")
        if pd.isna(ov): continue
        pol = TextBlob(ov).sentiment.polarity 
# • iterrows() loops row-by-row; simple for beginners but slower for huge datasets
# • r.get("Overview") safely accesses overview text even if a column is missing
# • pd.isna(ov) skips movies without overviews so polarity calculation does not break
# • TextBlob(ov).sentiment.polarity computes overview sentiment in [-1.0, +1.0]
        # TextBlob(text).sentiment.polarity returns a float in range -1.0 (negative) to 1.0 (positive) indicating the sentiment of the text. A value of 0 indicates neutral sentiment.
        if (not need_nonneg) or pol >= 0: # • need_nonneg = bool(mood) turns mood filtering on if any mood text is entered
# • pol >= 0 keeps neutral/positive overview movies when mood filtering is active
            out.append((r["Series_Title"], pol))
            if len(out) == n: break
    return out if out else "No suitable movie recommendations found."

def show(recs, name):
    print(Fore.YELLOW + f"\n🍿 AI-Analyzed Movie Recommendations for {name}:")
    for i, (t, p) in enumerate(recs, 1): # starts recommendation numbering from 1 for better user experience, instead of 0-based indexing used in programming
        print(f"{Fore.CYAN}{i}. 🎥 {t} (Polarity: {p:.2f}, {senti(p)})") # p:.2f formats polarity to 2 decimal places

def get_genre():
    print(Fore.GREEN + "Available Genres: ", end="")
    for i, g in enumerate(genres, 1): print(f"{Fore.CYAN}{i}. {g}")
    print()
    while True:
        x = input(Fore.YELLOW + "Enter genre number or name: ").strip()
        if x.isdigit() and 1 <= int(x) <= len(genres): return genres[int(x) - 1]
        x = x.title()
        if x in genres: return x
        print(Fore.RED + "Invalid input. Try again.\n")

def get_rating():
    while True:
        x = input(Fore.YELLOW + "Enter minimum IMDB rating (7.6-9.3) or 'skip': ").strip()
        if x.lower() == "skip": return None
        try:
            r = float(x)
            if 7.6 <= r <= 9.3: return r  # Valid rating range is based on the dataset's IMDB_Rating column, which typically ranges from 7.6 to 9.3 for the top 1000 movies. This ensures that user input is meaningful and corresponds to actual ratings in the dataset.
            print(Fore.RED + "Rating out of range. Try again.\n")
        except ValueError:
            print(Fore.RED + "Invalid input. Try again.\n")

print(Fore.BLUE + "🎥 Welcome to your Personal Movie Recommendation Assistant! 🎥\n")
name = input(Fore.YELLOW + "What's your name? ").strip()
print(f"\n{Fore.GREEN}Great to meet you, {name}!\n")
print(Fore.BLUE + "\n🔍 Let's find the perfect movie for you!\n")

genre = get_genre()

mood = input(Fore.YELLOW + "How do you feel today? (Describe your mood): ").strip() 
print(Fore.BLUE + "\nAnalyzing mood", end="", flush=True); dots()
# Mood polarity
mp = TextBlob(mood).sentiment.polarity
md = "positive 😊" if mp > 0 else "negative 😞" if mp < 0 else "neutral 😐"
print(f"\n{Fore.GREEN}Your mood is {md} (Polarity: {mp:.2f}).\n") # .2f formats the mood polarity to 2 decimal places for cleaner output.

rating = get_rating()
print(f"{Fore.BLUE}\nFinding movies for {name}", end="", flush=True); dots()
recs = recommend(genre=genre, mood=mood, rating=rating, n=5)
print(Fore.RED + recs + "\n") if isinstance(recs, str) else show(recs, name) # If recommend() returns a string (error message), it prints in red. Otherwise, it calls show() to display the list of recommendations.
# isinstance(recs, str) checks if the output from recommend() is a string (indicating an error message) or a list of recommendations. This allows the program to handle both cases gracefully and provide appropriate feedback to the user.
# IMP:: if recs is a string, it means no recommendations were found, and the error message is printed in red. If recs is a list of recommendations, the show() function is called to display them in a formatted manner.

while True:
    a = input(Fore.YELLOW + "\nWould you like more recommendations? (yes/no): ").strip().lower()
    if a == "no":
        print(Fore.GREEN + f"\nEnjoy your movie picks, {name}! 🎬🍿\n"); break
    if a == "yes":
        recs = recommend(genre=genre, mood=mood, rating=rating, n=5)
        print(Fore.RED + recs + "\n") if isinstance(recs, str) else show(recs, name)
    else:
        print(Fore.RED + "Invalid choice. Try again.\n")
