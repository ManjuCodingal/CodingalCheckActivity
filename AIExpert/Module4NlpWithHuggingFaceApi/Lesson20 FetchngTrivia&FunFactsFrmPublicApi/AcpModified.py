# Game style quiz

import requests
import random
import html

def get_questions(difficulty):
    url = f"https://opentdb.com/api.php?amount=5&difficulty={difficulty}&type=boolean"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        if data['response_code'] == 0:
            return data['results']
    except:
        return None


def play_level(level_name, difficulty): # Total 3 level of game, if pass level one level then only move to next level
    print(f"\n🎯 {level_name} ({difficulty.upper()}) LEVEL\n")
    
    questions = get_questions(difficulty)
    if not questions:
        print("Error fetching questions!")
        return 0
    
    score = 0

    for i, q in enumerate(questions, 1):
        question = html.unescape(q['question'])
        correct = html.unescape(q['correct_answer'])
        incorrect = html.unescape(q['incorrect_answers'][0])

        options = [correct, incorrect]
        random.shuffle(options)

        print(f"Q{i}: {question}")
        for idx, opt in enumerate(options, 1):
            print(f"  {idx}. {opt}")

        while True:
            try:
                choice = int(input("Your answer (1-2): "))
                if 1 <= choice <= 2:
                    break
            except:
                pass
            print("Invalid input! Enter 1 or 2.")

        if options[choice - 1] == correct:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer: {correct}\n")

    print(f"Level Score: {score}/5")
    return score


def main():
    print("🎮 Welcome to the Quiz Game!")
    total_score = 0

    # Level 1
    score1 = play_level("LEVEL 1", "easy")
    total_score += score1
    if score1 < 3:
        print("💀 Game Over! You didn't pass Level 1")
        return

    # Level 2
    score2 = play_level("LEVEL 2", "medium")
    total_score += score2
    if score2 < 3:
        print("💀 Game Over! You didn't pass Level 2")
        return

    # Level 3
    score3 = play_level("LEVEL 3", "hard")
    total_score += score3

    print("\n🏆 GAME COMPLETED!")
    print(f"Final Score: {total_score}/15")

    if total_score >= 12:
        print("🌟 Excellent Player!")
    elif total_score >= 8:
        print("👍 Good Job!")
    else:
        print("🙂 Keep Practicing!")


if __name__ == "__main__":
    main()

# 🎯 Features Added

# ✅ Levels (Easy → Medium → Hard),  Total 3 level of game, if pass level one level then only move to next level
# ✅ Score tracking
# ✅ Game Over system 💀
# ✅ Randomized answers
# ✅ Feedback after each question
# ✅ Final ranking

# 🎮 Sample Gameplay
# 🎮 Welcome to the Quiz Game!

# 🎯 LEVEL 1 (EASY LEVEL)

# Q1: The sky is blue.
# 1. True
# 2. False
# Your answer: 1
# ✅ Correct!
# 🧠 Teaching Explanation

# “We divide the quiz into levels, increase difficulty gradually, and allow progression only if the player performs well.”    