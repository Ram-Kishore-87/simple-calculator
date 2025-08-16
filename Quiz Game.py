def quiz_game():
    score = 0
    questions = [
        {
            "question": "1. What is the capital of India?",
            "options": ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"],
            "answer": "B"
        },
        {
            "question": "2. Which planet is known as the Red Planet?",
            "options": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
            "answer": "B"
        },
        {
            "question": "3. Who is known as the Father of Computers?",
            "options": ["A. Charles Babbage", "B. Alan Turing", "C. Bill Gates", "D. Steve Jobs"],
            "answer": "A"
        },
        {
            "question": "4. Which gas do humans exhale during respiration?",
            "options": ["A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Hydrogen"],
            "answer": "C"
        },
        {
            "question": "5. Which is the largest ocean in the world?",
            "options": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"],
            "answer": "D"
        },
        {
            "question": "6. Who wrote the Indian National Anthem?",
            "options": ["A. Rabindranath Tagore", "B. Bankim Chandra Chatterjee", "C. Subramania Bharati",
                        "D. Sarojini Naidu"],
            "answer": "A"
        },
        {
            "question": "7. What is the chemical symbol of Gold?",
            "options": ["A. Ag", "B. Au", "C. Go", "D. Gd"],
            "answer": "B"
        },
        {
            "question": "8. Which is the smallest prime number?",
            "options": ["A. 0", "B. 1", "C. 2", "D. 3"],
            "answer": "C"
        },
        {
            "question": "9. Name of this laptop?",
            "options": ["A. HP", "B. Lenovo", "C. Dell", "D. Apple"],
            "answer": "A"
        },
        {
            "question": "10. No of bones in human body:",
            "options": ["A. 209", "B. 208", "C. 206", "D. 205"],
            "answer": "C"  # Corrected key & answer
        }
    ]

    print("---------------------------------------------------")
    print("Welcome to the Quiz Game")
    print("---------------------------------------------------")

    for q in questions:
        print(q["question"])
        for option in q["options"]:
            print(option)

        user_answer = input("Enter your option (A/B/C/D): ").upper()

        if user_answer == q["answer"]:
            print("✅ Correct!\n")
            score += 1
        else:
            print("❌ Incorrect!")
            print(f"The correct answer is {q['answer']}\n")

    score_average = score / len(questions) * 100
    print("---------------------------------------------------")
    print(f"🎯 You got {score}/{len(questions)} correct")
    print(f"📊 Your score percentage is: {score_average:.2f}%")
    print("---------------------------------------------------")


quiz_game()
