import requests, re, random # requests: Http library for making api calls for hugging face, re=> regular expressn module for pattern matching and text cleaning; random=> for randomly selecting demo questions pair
from config import HF_API_KEY # personal authentication key 

#change below model to this if required --> "sentence-transformers/all-mpnet-base-v2"
MODEL="sentence-transformers/all-MiniLM-L6-v2" # sentence transformer model- understand semantic meaning
API=f"https://router.huggingface.co/hf-inference/models/{MODEL}"
HEAD={"Authorization":f"Bearer {HF_API_KEY}"} # auth header with bearer token
TH=0.72 # threshold 72% or higher means duplicate 
DEMOS=[("how to delete my account","how do i remove my account"), # demo questns pair. List of tuples contains 2 questions with same meaning but diff wording.
       ("start the game","begin the game"),
       ("nearest hospital to me","closest clinic near me"),
       ("mobile games are getting bigger in size","game size on phones is increasing"),
       ("is it going to rain today","today is rainy"),
       ("reset my password","change my password")]

TOK=lambda s:" | ".join(s.split()) # tokeniser: splits text into words and joins with'|' separator for display
bar=lambda s:"█"*int(s*10)+"░"*(10-int(s*10)) # bar creates visual progress bar- converts .75 to '███████░░░' (7 filled, 3 empty)
clean=lambda t:[w for w in (re.sub(r"[^a-z0-9']+","",x.lower()) for x in t.split()) if w] # clean removes punctuation, converts to lowercase, keeps only letters, numbers and apostophes
nums=lambda t:set(re.findall(r"\d+(?:\.\d+)?", t)) # num extracts all numbers from text (including decimals like 3.14)
has_any=lambda t,arr:any(a in set(clean(t)) for a in arr) # has_any checks if any word from array exists in text (used for negation/opposite detection). lambda function:: one-line anonymous functions foe cleaner, compact code

def hf(q1,q2):
    r=requests.post(API,headers=HEAD,json={"inputs":{"source_sentence":q1,"sentences":[q2]}},timeout=30) # requests.post: Sends HTTP POST request to Hugging Face API. json payload: Sends q1 as source sentence and q2 as comparison target. timeout=30: Prevents hanging - raises error if no response in 30 seconds

# Error handling 1: Checks HTTP status (.ok) - fails if 404, 500, etc.
# Error handling 2: Checks if API returned error dictionary instead of score
    if not r.ok: raise RuntimeError(r.text)
    data=r.json()
    if isinstance(data,dict): raise RuntimeError(data.get("error",str(data)))
    return float(data[0]) # Return value: Similarity score as float between 0.0 (different) and 1.0 (identical)

def smart_score(base,q1,q2,strong):
    w1={w for w in clean(q1) if len(w)>=4}; w2={w for w in clean(q2) if len(w)>=4} # w1, w2: Filter for meaningful words (4+ chars) - ignores 'the', 'is', 'a', 'to'
    jac=len(w1&w2)/max(1,len(w1|w2)) # jac (Jaccard): Measures word overlap = (shared words) ÷ (total unique words)
    boost=(0.04 if len(strong)>=2 else 0)+(0.03 if jac>=0.20 else 0)+(0.05 if jac>=0.35 else 0)
# +0.04: If 2+ strong word matches (e.g., 'account', 'password')
# +0.03: If 20%+ word overlap (moderate similarity)
# +0.05: If 35%+ word overlap (high similarity)
# Maximum boost: +0.12 (4% + 3% + 5%) can increase score significantly
    negA=["not","no","never","without","can't","cant","cannot","don't","dont","won't","wont","n't"]
    oppA=[("increase","decrease"),("bigger","smaller"),("more","less"),("add","remove"),("open","close"),("enable","disable")]
    num_pen=0.10 if (nums(q1) and nums(q2) and nums(q1)!=nums(q2)) else 0
    neg_pen=0.12 if has_any(q1,negA)!=has_any(q2,negA) else 0
    opp_pen=0.12 if any((has_any(q1,[a]) and has_any(q2,[b])) or (has_any(q1,[b]) and has_any(q2,[a])) for a,b in oppA) else 0
    return max(0.0, min(1.0, base+boost-num_pen-neg_pen-opp_pen))

def label(s): return "✅ DUPLICATE" if s>=TH else ("🤔 CLOSE MATCH" if s>=TH-0.05 else "❌ DIFFERENT") 
# label() function: Three-tier classification system
# ≥72%: ✅ DUPLICATE (same meaning)
# 67-71.9%: 🤔 CLOSE MATCH (similar but not quite)
# <67%: ❌ DIFFERENT (unrelated)
def show_result(s): # show_result(): Displays percentage, visual bar, emoji label, and threshold rule
    print(f"\n🎯 Result of Similarity: {round(s*100,1)}% [{bar(s)}]  →  {label(s)}") # round(s*100,1): Converts 0.8549 → 85.5% (one decimal place)
    print(f"Rule: score ≥ {TH} means DUPLICATE")

# Word categorization system:
# Strongest: Words 4+ chars that appear in BOTH sentences (core meaning)
# Helper: Words 2-3 chars (minor context like 'my', 'to', 'is')
# Least: Connectors and tiny words (1-2 chars or common connectors)

# Educational transparency: Shows exactly how the algorithm breaks down sentences
# TOK(q1): Displays tokenized version with ' | ' separators

def show_flow(q1,q2):
    a,b=clean(q1),clean(q2); raw=set(a+b)
    w1={w for w in a if len(w)>=4}; w2={w for w in b if len(w)>=4}
    shared=sorted(w1&w2)
    helpers=sorted({w for w in raw if 2<=len(w)<=3})
    conn={"a","an","the","to","of","in","on","is","am","are","do","did","does","my","me","it"}
    least=sorted({w for w in raw if len(w)<=2 or w in conn})
    print("\n🔁 FLOW (sentence → strongest/helper/least → similarity %)")
    print("\n1) Input sentences"); print(f"   Q1: {q1}\n   Q2: {q2}")
    print("\n2) Split into words/tokens (same as you typed)")
    print("   Q1 →",TOK(q1)); print("   Q2 →",TOK(q2))
    print("\n3) Pick the “meaning-carrying” parts (from YOUR sentences)")
    print("   Strongest:",", ".join(shared) if shared else "No obvious shared/synonym matches")
    print("   Helper:",", ".join(helpers) if helpers else "None")
    print("   Least:",", ".join(least) if least else "None")
    print("\n4) Why similarity is high/low for THIS pair")
    print("   - Direct matches:",", ".join(shared)) if shared else print("   - The model used overall meaning patterns, not exact word matches.")

# Step 1 - Title: Prints section header ('YOUR QUESTIONS' or 'RANDOM DEMO 1')
# • Step 2 - API Call: Gets base similarity from Hugging Face model
# • Step 3 - Strong Words: Finds intersection of meaningful words (4+ chars) from both sentences
# • Step 4 - Scoring: Applies smart_score with boost and penalty system
# • Step 5 - Display: Shows result and educational flow breakdown

def run(q1,q2,title):
    print(f"\n--- {title} ---")
    base=hf(q1,q2)
    strong=sorted({w for w in clean(q1) if len(w)>=4} & {w for w in clean(q2) if len(w)>=4})
    s=smart_score(base,q1,q2,strong)
    show_result(s); show_flow(q1,q2)

def main():
    print("Type Question 1 → Question 2. Then you’ll see 2 RANDOM demo pairs.")
    print("Type 'exit' anytime to quit.\n") # exit checks : can exit after either qu1 or Qu2
    while True:
        q1=input("Question 1: ").strip()
        if q1.lower()=="exit": break
        q2=input("Question 2: ").strip()
        if q2.lower()=="exit": break
        if not q1 or not q2: continue
        try:
            run(q1,q2,"YOUR QUESTIONS")
            for i,(d1,d2) in enumerate(random.sample(DEMOS,2),1): run(d1,d2,f"RANDOM DEMO {i}") # (random.sample(DEMOS,2) picks 2 different random pairs from the 6 demos. enumerate(...,1): counts from 1 (not 0) for user friendly display
            print("\n(Next round → Question 1 or 'exit')\n")
        except Exception as e:
            print("\n⚠️ Oops!",e,"\n")

if __name__=="__main__": main()
