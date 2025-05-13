# Quiz game in python

questions = (("1. Who is the father of Devadratha. "),
             ("2. Lord King pandu had, how many son's? "),
             ("3. what is the name of dhushal's biggest borther's Name?"),
             ("4. who was the chariotor of arjun"), 
             ("5. Who was lord krishna's favourite preson"))


options = (("A. king veechitra veera", "B. king shanthan", "C. king salva", "D. king dhruthrashta"),
           ("A. 6", "B. 4", "C. 5", "D. 2"),
           ("A. Dhrayodhna", "B. dhshyasana", "C. vi krana", "D. sindhu"),
           ("A. krishna", "B. Yudhistra", "C. Hunuman", "D. Balarama"),
           ("A. Bheeshma", "B. Dhrona", "C. Vidhura", "D. Shakuni"))


answers = ("B", "C", "A", "A", "C")

guessess = []
score = 0
question_num = 0

for question in questions:
    print("---------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter the choice: ").upper()
    guessess.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT")
    else:
        print("INCORRECT")
        print(f"{answers[question_num]} is the CORRECT Answer")
    question_num += 1

print("---------------------------")
print("         RESULT            ")
print("---------------------------")

print("Answers : ", end = "")
for answer in answers:
    print(answer, end = " ")
print()

print("Guess : ", end = "")
for guess in guessess:
    print(guess, end = " ")
print()

score = int(score / len(questions) * 100)

print(f"Your score is: {score}%")
