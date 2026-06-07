import time

questions = [
    {
        "question": "Normal BP?",
        "options": ["120/80", "140/90", "100/60", "160/100"],
        "answer": "120/80"
    },
    {
        "question": "RBC lifespan?",
        "options": ["60 days", "90 days", "120 days", "150 days"],
        "answer": "120 days"
    }
]

score = 0

for q in questions:
    print("\n====================")
    print("Question:", q["question"])

    for i, option in enumerate(q["options"]):
        print(f"{i+1}. {option}")

    print("\nYou have 10 seconds to answer...")

    start_time = time.time()
    user_input = input("Choose (1-4): ")
    end_time = time.time()

    time_taken = end_time - start_time

    if time_taken > 10:
        print("Time over ⏰")
        continue

    selected_answer = q["options"][int(user_input) - 1]

    if selected_answer == q["answer"]:
        print("Correct ✅")
        score += 1
    else:
        print("Wrong ❌")

print("\n====================")
print("Final Score:", score, "/", len(questions))
