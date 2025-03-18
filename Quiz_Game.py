print("Welcome to this Animals Fun Facts Quiz Game :) ")
answer = input("Are you ready to play the Quiz? (yes/no) :")
score = 0
total_questions = 5

if answer.lower() == "yes":
    answer = input("Question 1: What is the animal that has a blue tongue? ")
    if answer.lower() == "giraffe":
        score += 1
        print("Correct")
    else:
        print("Wrong Answer :( ")


    answer = input("Question 2: How big is the heart of a blue whale? ")
    if answer.lower() == "golf cart":
        score += 1
        print("Correct")
    else:
        print("Wrong Answer :( ")


    answer = input("Question 3: The sound of which animal was used for the T-Rex sound in Jurassic Park? ")
    if answer.lower() == "koala":
        score += 1
        print("Correct")
    else:
        print("Wrong Answer :( ")

    answer = input("Question 4: Do pink dolphins exist? ")
    if answer.lower() == "yes":
        score += 1
        print("Correct")
    else:
        print("Wrong Answer :( ")

    answer = input("Question 5: When we look at a world map, what shape is it? ")
    if answer.lower() == "cat playing with australia":
        score += 1
        print("Correct")
    else:
        print("Wrong Answer :( ")

print("Thank you for playing. You attempted", score, "questions correctly!!")
mark = (score/total_questions)*100
print("Marks obtained:", mark)
print("BYE!!")
