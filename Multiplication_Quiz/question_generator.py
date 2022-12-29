import random


class QuestionGenerator:

    def __init__(self,limit):
        self.question_number = 0
        self.score = 0
        self.limit = limit

    def generate_question(self, multipliers, multiplicants):
        rand_multiplier = random.choice(multipliers)
        rand_multiplicant = random.choice(multiplicants)
        user_answer = input(f"{rand_multiplier} * {rand_multiplicant} = ")
        if not user_answer.isdigit():
            user_answer = input(f"Enter a number! {rand_multiplier} * {rand_multiplicant} = ")
            if not user_answer.isdigit():
                print("You didn't enter a number! Your answer is = 0")
                user_answer = 0
        text = f"{rand_multiplier} * {rand_multiplicant}"
        correct_answer = rand_multiplier * rand_multiplicant
        self.check_answer(user_answer,correct_answer)

    def check_answer(self, user_answer,correct_answer):
        if int(user_answer) ==correct_answer:
            self.score +=1
            print("You got it right!")
        else:
            print("That was wrong.")
        print(f"The correct answer was {correct_answer}")
        print(f"Your current score is {self.score}/{self.limit}.")
        print("\n")