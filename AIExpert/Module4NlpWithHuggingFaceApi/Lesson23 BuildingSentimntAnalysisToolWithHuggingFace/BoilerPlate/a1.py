# ==================================================
# DUPLICATE QUESTION DETECTOR – BOILERPLATE
# ==================================================
# This program checks whether two questions mean the same thing.
#
# HOW IT WORKS
# 1) Takes two questions (Q1, Q2) from the user.
# 2) Uses a Hugging Face sentence-similarity model to get a base score (0–1).
# 3) Improves the score with simple logic:
#    • Boost if important words overlap.
#    • Penalize if numbers differ (e.g., 200 vs 300).
#    • Penalize if negation differs (can vs can’t).
#    • Penalize if opposite actions appear (increase vs decrease).
# 4) Shows:
#    • RESULT first (final score + decision)
#    • FLOW next (how the comparison was made).
# 5) After each round, shows 2 RANDOM demo question pairs.
# 6) Repeats until the user types: exit
#
# --------------------------------------------------
# CONFIG
# --------------------------------------------------
# MODEL      : Sentence similarity model from Hugging Face
# TH (0–1)   : Duplicate threshold
# DEMOS      : Example question pairs for demonstration
#
# --------------------------------------------------
# KEY HELPERS
# --------------------------------------------------
# clean(text)     → lowercase + remove punctuation
# nums(text)      → extract numbers from text
# has_any(text)   → check presence of keywords
# bar(score)      → visual similarity bar
#
# --------------------------------------------------
# SCORING LOGIC
# --------------------------------------------------
# final_score = model_score + boosts − penalties
#
# Boosts:
# • Shared meaningful words
# • Strong word overlap (Jaccard)
#
# Penalties:
# • Number mismatch
# • Negation mismatch
# • Opposite intent words
#
# --------------------------------------------------
# OUTPUT LABELS
# --------------------------------------------------
# ✅ DUPLICATE     : score ≥ TH
# 🤔 CLOSE MATCH  : score just below TH
# ❌ DIFFERENT    : otherwise
#
# --------------------------------------------------
# FLOW DISPLAY
# --------------------------------------------------
# 1) Input sentences
# 2) Tokens (as typed)
# 3) Strongest / Helper / Least words
# 4) Reason for similarity result
#
# --------------------------------------------------
# ENTRY POINT
# --------------------------------------------------
# main() runs the loop until user types "exit"
# ==================================================
