
questions = [
    {
        "question": "1. Which language is used for AI?",
        "options": ["A. HTML", "B. Python", "C. CSS", "D. PHP"],
        "answer": "B"
    },
    {
        "question": "2. Which function is used to display output?",
        "options": ["A. input()", "B. print()", "C. type()", "D. len()"],
        "answer": "B"
    },
    {
        "question": "3. Which data type stores True or False?",
        "options": ["A. int", "B. str", "C. bool", "D. list"],
        "answer": "C"
    },
    {
        "question": "4. Which symbol is used for comments?",
        "options": ["A. //", "B. #", "C. @", "D. $"],
        "answer": "B"
    },
    {
        "question": "5. Which keyword is used to define a function?",
        "options": ["A. function", "B. def", "C. fun", "D. return"],
        "answer": "B"
    },
    {
        "qustion": "6.What is the python developed? ",
        "options": ["A. Dennis Ritchie", "B.James Gosling","C.Guido van Rossum","D.Bjarne Stroustrup"],
        "answer": "C"
    },
    {
        "qustion":"7.Which extension is used for Python files?",
        "options":["A..java","B..py","C..html","D..cpp"],
        "answer": "B"
    },
    {
        "question":"8.Which data type stores decimal values?",
        "options": ["A.int","B.Float","c.Str","D.bool"],
        "answer": "B"
    }
]

score = 0

print("\n**********************************")
print("       PYTHON QUIZ APP")
print("*************************************")

name = input("Enter your name: ")


print("Select the correct option: A, B, C or D\n")

for q in questions:

    print(q["question"])

    for option in q["options"]:
        print(option)

    answer = input("Enter your answer: ").upper()

    if answer == q["answer"]:
        print("Correct Answer!\n")
        score += 1
    else:
        print("Wrong Answer!")
        print("Correct answer:", q["answer"], "\n")

print("**********************************")
print("          QUIZ RESULT")
print("************************************")

print("Student Name:", name)
print("Total Questions:", len(questions))
print("Correct Answers:", score)
print("Wrong Answers:", len(questions) - score)
print("Your Score:", score, "/", len(questions))

percentage = (score / len(questions)) * 100

print("Percentage:", percentage, "%")

if percentage >= 80:
    print("Excellent Performance!")
elif percentage >= 50:
    print("Good Performance!")
else:
    print("Keep Practicing!")

print("\nThank you for playing!")
