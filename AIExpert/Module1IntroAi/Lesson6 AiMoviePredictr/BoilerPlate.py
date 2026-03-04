import time, pandas as pd
from textblob import TextBlob
from colorama import init, Fore

# Init colors
init(autoreset=True)

# Load CSV (same error output)
try: df = pd.read_csv("imdb_top_1000.csv")
except FileNotFoundError:
    print(Fore.RED + "Error: The file 'imdb_top_1000.csv' was not found."); raise SystemExit

# Unique genres
genres = sorted({g.strip() for xs in df["Genre"].dropna().str.split(", ") for g in xs})

def dots():
    """Prints ... with delay (AI thinking effect)."""
    for _ in range(3): print(Fore.YELLOW + ".", end="", flush=True); time.sleep(0.5)

def senti(p):
    """Polarity -> label."""
    return "Positive 😊" if p > 0 else "Negative 😞" if p < 0 else "Neutral 😐"

def recommend(genre=None, mood=None, rating=None, n=5):
    """Filter by genre/rating, shuffle, analyze Overview polarity, return n (title, polarity) or message."""
    # 1) Start: d = df
    # 2) If genre: filter Genre contains (case-insensitive)
    # 3) If rating not None: filter IMDB_Rating >= rating
    # 4) If empty: return "No suitable movie recommendations found."
    # 5) Shuffle: sample(frac=1).reset_index(drop=True)
    # 6) need_nonneg = bool(mood)
    # 7) Loop rows:
    #    - skip missing Overview
    #    - pol = TextBlob(overview).sentiment.polarity
    #    - if not need_nonneg or pol >= 0: append (Series_Title, pol)
    #    - stop at n
    # 8) Return list else same message
    pass

def show(recs, name):
    """Print in same format: header + numbered 🎥 lines with polarity + senti()."""
    # Print: "\n🍿 AI-Analyzed Movie Recommendations for {name}:"
    # Loop enumerate(recs, 1) and print:
    # "{i}. 🎥 {title} (Polarity: {p:.2f}, {senti(p)})"
    pass

def get_genre():
    """Print genres, then ask: Enter genre number or name: (repeat until valid)."""
    # Print "Available Genres: " then each: "{i}. {genre}"
    # Input prompt must match exactly
    # Accept valid number OR exact title-cased genre name
    # On invalid: print "Invalid input. Try again.\n"
    pass

def get_rating():
    """Ask rating or 'skip' (repeat until valid)."""
    # Prompt must match exactly
    # If skip -> None
    # Else float in 7.6..9.3
    # Out of range -> "Rating out of range. Try again.\n"
    # Bad float -> "Invalid input. Try again.\n"
    pass

# MAIN (students write)
# 1) Print welcome + ask name + greet
# 2) Print 🔍 line
# 3) genre = get_genre(); mood input
# 4) Print "Analyzing mood" + dots(); compute mood polarity + print mood line
# 5) rating = get_rating()
# 6) Print "Finding movies for {name}" + dots()
# 7) recs = recommend(...); if str print red else show()
# 8) Loop ask "Would you like more recommendations? (yes/no):"
#    - no -> print enjoy line + break
#    - yes -> recommend again + show
#    - else -> invalid choice line
