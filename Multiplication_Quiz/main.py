from question_generator import QuestionGenerator as QG
import data

i=1
limit = int(input("How many questions do you want to answer? "))
quiz = QG(limit)
while i<=limit:
    quiz.generate_question(data.multipliers, data.multiplicants)
    i+=1

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{limit}")