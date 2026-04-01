# Explaoring NLP and Getting introduced to HuggingFace platform
# Can learn how computers understand human lang and discover zero-shot classig=fication, where AI can categorize text without prior training.Eg. News Topic classifier that sorts headlines into relevant categories.

import requests
from config import HF_API_KEY

MODEL_ID = "facebook/bart-large-mnli"
API_URL = f"https://router.huggingface.co/hf-inference/models/{MODEL_ID}"
HEADERS = {"Authorization": f"Bearer {HF_API_KEY}"} # contains api key in the format hugging face expects
TOPICS = ["Sports", "Technology", "Business", "Politics", "Health"]

def ask_hf(headline: str):
    payload = {"inputs": headline, "parameters": {"candidate_labels": TOPICS}}
    r = requests.post(API_URL, headers=HEADERS, json=payload, timeout=30) # Timeout: wait upto 30 seconds for a response (first req can be slow)
    if not r.ok: # checks if something went wrong with the request
        raise RuntimeError(f"HF error {r.status_code}: {r.text}")
    return r.json()  # returns a LIST of {"label": ..., "score": ...}. Converts response from Json format to py list/dictionary

# Helper functions
def best_topic(preds: list): # finds prediction with highest score from all topics
    best = max(preds, key=lambda x: x["score"]) #  max() with key=lambda is a py trick to find max by a specific field
    return best["label"], best["score"]

def bar(score: float) -> str: # creates a visual progress bar using block characters "█"  for filled,  "░" for empty
    pct = score * 100 # integer division to get how many blocks to fill (eg.75%=7 blocks) (Percentage)
    blocks = int(pct // 10)
    return "█" * blocks + "░" * (10 - blocks)

def show(headline: str, preds: list): # creates a beautiful formatted display of results
    top_label, top_score = best_topic(preds)
    print("\n" + "=" * 60) # "=" * 60 creates a line of 60 equal signs for visual separation
    print("????️ News Topic Classifier")
    print("=" * 60)
    print("Headline:", headline)
    print(f"Best topic: {top_label}")
    print(f"Confidence: {round(top_score*100,1)}% [{bar(top_score)}]") # top_score*100:: Assumes top_score is a number between 0 and 1 (like 0.873).. Multiplying by 100 converts it into a percentage. round(..., 1) rounds it to 1 decimal place for cleaner display.
# bar(top_score) :: This is a function call.
# It likely generates a visual bar representation (like a progress bar) based on top_score.
# Example output might look like: ████████░░ (for ~80%)
# [...]:: The square brackets are just formatting to visually wrap the bar.

    print("\nTop 3 guesses:")
    top3 = sorted(preds, key=lambda x: x["score"], reverse=True)[:3] # sorted(..., reverse=True)[:3] sorts by score (highest first) and takes top 3
    for i, p in enumerate(top3, start=1): # enumerate(..., start=1) Numbers items starting frfom 1 instead of 0
        print(f"{i}. {p['label']:<11} {round(p['score']*100,1)}% [{bar(p['score'])}]") # {p['label']:<11}: left aligns the label in 11 characters for neat columns
    print("=" * 60)
 
def main():
    print("Welcome! Type a news headline and I'll guess the topic.")
    print("Topics:", ", ".join(TOPICS))
    print("Type 'exit' to stop.\n")

    while True: # infinite loop so users can classify multiple headlines
        headline = input("Headline: ").strip()
        if headline.lower() == "exit":
            print("Bye! Keep coding ????")
            break

        if not headline:
            print("Please type a headline (not empty).\n")
            continue

        try:
            preds = ask_hf(headline)
            if isinstance(preds, list) and preds and "label" in preds[0]:
                show(headline, preds)
            else:
                print("Oops! Unexpected reply:", preds)

        except Exception as e:
            print("\n⚠️ Oops! Something went wrong.")
            print("Reason:", e)
            print("Tip: Check HF_API_KEY + internet.\n")

if __name__ == "__main__":
    main()