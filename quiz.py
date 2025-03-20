# Python Quiz Program
# Time and Random Module used for this project.

import time
import random

print("Welcome to this quick 10 question quiz! \n")
time.sleep(2)

# Questions
Q1 = input("What is the speed of sound: A 260mph, B 560mph, C 760mph?: ").upper()
time.sleep(1)

Q2 = input("\nWhich is the correct spelling: A mistake, B misstake, C missteak?: ").upper()
time.sleep(1)

Q3 = input("\nHow many letters in the Greek alphabet: A 16, B 24, C 28?: ").upper()
time.sleep(1)

Q4 = input("\nThe Model T car was made by which company: A Ford, B Mercedes, C BMW?: ").upper()
time.sleep(1)

Q5 = input("\nThe Golden Oriole is a: A bird, B fish, C flower?: ").upper()
time.sleep(1)

Q6 = input("\nWhich of these was a US President: A George Washington, B George York, C George Houston?: ").upper()
time.sleep(1)

Q7 = input("\nPer person, which country eats the most chocolate: A USA, B Switzerland, C Belgium?: ").upper()
time.sleep(1)

Q8 = input("\nThe X-Box games console is made by which company: A Sony, B Nintendo, C Microsoft?: ").upper()
time.sleep(1)

Q9 = input("\nRoughly how many hairs are on a human head: A 100,000, B 10,000, C 30,000?: ").upper()
time.sleep(1)

Q10 = input("\nA cinquain poem has how many lines: A 5, B 15, C 10?: ").upper()
time.sleep(1)

def correct_answers():
    score = 0
    if Q1 == "C":
        score += 1
    else:
        score -= 1
    if Q2 == "A":
        score += 1
    else:
        score -= 1
    if Q3 == "B":
        score += 1
    else:
        score -= 1
    if Q4 == "A":
        score += 1
    else:
        score -= 1
    if Q5 == "A":
        score += 1
    else:
        score -= 1
    if Q6 == "A":
        score += 1
    else:
        score -= 1
    if Q7 == "B":
        score += 1
    else:
        score -= 1
    if Q8 == "C":
        score += 1
    else:
        score -= 1
    if Q9 == "A":
        score += 1
    else:
        score -= 1
    if Q10 == "A":
        score += 1
    else:
        score -= 1

    print(f'\nYour score is {score}/10!\n')

    if score < 6:
        print("You failed! Try Again!")
    elif score > 6 and score < 9:
        print("Nice job, you did fine!")
    elif score > 9:
        print("EXCELLENT JOB!")
    else:
        print("Error, something went wrong")


#Loop to put everything together and even prompts the user if they'd like to go again.
while True:
    QUESTIONS = [Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10]
    random.choice(QUESTIONS)
    correct_answers()

    retry = input("Would you like to try the quiz again? (Y/N): ").upper()
    if retry == "Y":
        QUESTIONS = [Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10]
        random.choice(QUESTIONS)
        correct_answers()
    elif retry == "N":
        print("Thanks for playing! ")
        time.sleep(1)
        break
    else:
        print("Sorry, not Y or N :/")
        time.sleep(1)
        break
