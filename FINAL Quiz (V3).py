# Endgame
# Letting user know that the quiz is over
# Determining score at the end of the game by defining score in print equation
# Defining score as 0 to set it at nothing


score = 0
def endgame():
    print("You have come to the end of Hanna's general knowledge quiz. Thank you for playing!")
    print("Your score is", score)


# Question Fifteen

def question15():
    global score
    print("This is the fifteenth, and final, question!")
    while True:
        australia = input("What is the capital of Australia?")
        if australia == "canberra":
            print("Correct! You have named the capital of Australia and earned one point.")
            score = score + 1
            endgame()
            break
        else:
            print("Wrong! You did not correctly name the capital of Australia (Canberra). You have not earned a point.")
            endgame()
            break

# Question Fourteen
# Five correct answers, so defined by separating with "or" e.g. "osaka" or "mexico city" or
# Using break function to ensure that no functions loop


def question14():
    global score
    print("This is the fourteenth question!")
    while True:
        cities = input("Name one of the five most populated cities in the world.")
        if cities == "osaka" or "mexico city" or "sao paulo" or "mumbai" or "beijing":
            print("Correct! You have listed one of the most populated cities.")
            score = score + 1
            question15()
            break
        else:
            print("Wrong! You did not name Osaka, Mexico City, Sao Paulo, or Beijing. You have not earned a point.")
            question15()
            break

# Question Thirteen


def question13():
    global score
    print("This is the thirteenth question!")
    while True:
        rainbow = input("Name a color of the rainbow.")
        if rainbow == "red" or "orange" or "yellow" or "green" or "blue" or "purple":
            print("Correct! You listed a color of the rainbow.")
            question14()
            score = score + 1
            break
        else:
            print("Wrong! You did not name a color of the rainbow. You have not earned one point.")
            question14()
            break

# Question Twelve
# Free response style questions, defining terms that apply to the question e.g. if colorado == "denver"
# Only one correct answer defined for this type of question, if user gets it, grant point
# Directing user to question 13, by indicating "question13()" and then defining question 13 above
# Setting personalized variables for every question, e.g. defining colorado


def question12():
    global score
    print("Welcome to the free response question of the quiz. This is the twelfth question!")
    while True:
        colorado = input("What is the capital of Colorado?")
        if colorado == "denver":
            print("Correct! Denver is the capital of Colorado. You have earned one point.")
            question13()
            score = score + 1
            break
        else:
            print("Wrong! The capital of Colorado is Denver. You have not earned a point.")
            question13()
            break

# Question Eleven


def question11():
    global score
    print("This is the eleventh question and the last multiple choice question!")
    print("The ozone layer restricts:")
    answer11 = input("""
a.	Visible light
b.	Infrared radiation
c.	X-rays and gamma rays
d.	Ultraviolet radiation
""")
    if answer11 == "d":
        print("Correct! You have earned one point.")
        score = score + 1
        question12()
    else:
        print("Incorrect! The ozone layer restricts ultraviolet radiation. You have not earned a point.")
        question12()

# Question Ten


def question10():
    global score
    print("This is the tenth question!")
    print("Federation Cup, World Cup, Allywyn International Trophy and Challenge Cup are awarded to winners of:")
    answer10 = input("""
a.	Tennis
b.	Basketball
c.	Volleyball
d.	Cricket""")
    if answer10 == "c":
        print("Correct! You have earned one point.")
        score = score + 1
        question11()
    else:
        print("Incorrect! They are awarded to volleyball You have not earned one point.")
        question11()

# Question Nine


def question9():
    global score
    print("This is the ninth question!")
    print("For the Olympics and World Tournaments, the dimensions of basketball court are:")
    answer9 = input("""
a.  26 m x 14 m
b.	28 m x 15 m
c.	27 m x 16 m
d.	28 m x 16 m""")
    if answer9 == "b":
        print("Correct! You have earned one point.")
        score = score + 1
        question10()
    else:
        print("Incorrect! The dimensions are 28 m X 15 m. You have not earned one point.")
        question10()

# Question Eight


def question8():
    global score
    print("This is the eighth question!")
    print("For which of the following disciplines is Nobel Prize awarded?")
    answer8 = input("""
a.  Physics and Chemistry
b.	Physiology or Medicine
c.	Literature, Peace and Economics
d.	All of the above""")
    if answer8 == "d":
        print("Correct! You have earned one point.")
        score = score + 1
        question9()
    else:
        print("Incorrect! The Nobel Prize is awarded to all disciplines. You have not earned one point.")
        question9()


# Question Seven


def question7():
    global score
    print("This is the seventh question!")
    print("Entomology is the science that studies:")
    answer7 = input("""
a.  Behavior of human beings
b.	Insects
c.	The origin and history of technical and scientific terms
d.	The formation of rocks""")
    if answer7 == "b":
        print("Correct! You have earned one point.")
        score = score + 1
        question8()
    else:
        print("Incorrect! Entomology is the science that students insects. You have not earned one point.")
        question8()


# Question Six
# Multiple choice introduced: providing users with options a, b, c, and d
# If user selects the correct answer, earn a point
# Use global score function to account for the total score
# Offer explanations for incorrect answers (providing the correct answer)


def question6():
    global score
    print("Welcome to the multiple choice section of the quiz. This is the sixth question!")
    print("Which track and field star overcame childhood polio to become one of the greatest athletes of her time?")
    answer6 = input("""
a. Wilma Rudolph
b. Gail Devers
c. Florence Griffith Joyner
d. Jackie Robinson""")
    if answer6 == "a":
        print("Correct! You have earned one point.")
        score = score + 1
        question7()
    else:
        print("Incorrect! Wilma Rudolph overcame child polio. You have not earned one point.")
        question7()


# Question Five


def question5():
    global score
    print("This is the fifth question!")
    while True:
        bromine = input("Bromine is a non-metal that remains liquid at room temperature, true or false?")
        if bromine == "false":
            print("Wrong! Bromine remains liquid at room temperature. You have not earned a point.")
            question6()
            break
        elif bromine == "true":
            print("Correct! Bromine remains liquid at room temperature. You have earned a point.")
            score = score + 1
            question6()
            break
        else:
            print("Please enter a valid response!")

# Question Four


def question4():
    global score
    print("This is the fourth question!")
    while True:
        fathometer = input("The fathometer is used to measure sound intensity, true or false?")
        if fathometer == "false":
            print("Correct! The fathometer is used to measure ocean depth. You have earned a point.")
            score = score + 1
            question5()
            break
        elif fathometer == "true":
            print("Wrong! The fathometer is used to measure ocean depth. You have not earned a point.")
            question5()
            break
        else:
            print("Please enter a valid response!")

# Question Three


def question3():
    global score
    print("This is the third question!")
    while True:
        horse = input("Epsom, England is associated with horse racing, true or false?")
        if horse == "false":
            print("Wrong! Epsom is associated with horse racing. You have not earned a point.")
            question4()
            break
        elif horse == "true":
            print("Correct! Epsom is associated with horse racing. You have earned a point.")
            score = score + 1
            question4()
            break
        else:
            print("Please enter a valid response!")

# Question Two


def question2():
    global score
    print("This is the second question!")
    while True:
        egypt = input("The capital of Egypt is Cairo, true or false?")
        if egypt == "false":
            print("Wrong! The capital of Egypt is Cairo. You have not earned a point.")
            question3()
            break
        elif egypt == "true":
            print("Correct! The capital of Egypt is Cairo. You have earned a point.")
            score = score + 1
            question3()
            break
        else:
            print("Please enter a valid response.")

# Question One
# Using functions to define true or false questions
# If right, award point and if not, do not award point
# Score calculating equation introduced


def question1():
    score = 0
    print("Welcome to the true or false section of the quiz. This is the first question!")
    while True:
        continents = input("There are eight continents, true or false?")
        if continents == "false":
            print("Correct! There are seven continents. You have earned one point.")
            score = score + 1
            question2()
            break
        elif continents == "true":
            print("Wrong! There are seven continents. You have not earned a point.")
            question2()
            break
        else:
            print("Please enter a valid response.")

# Introduction
# Defining my quiz, giving user option 1 to play and option 2 to not play
# Using if, elif, and else to guide user to next segment of quiz


def gkquiz():
    print("Welcome to hanna's general knowledge quiz! You will be tested for your level of general understanding through a series of sixteen multiple choice, true/false, and short answer questions.")
    while True:
        startquiz = int(input("Do you want to take the quiz? Enter 1 for Yes, and 2 for No."))
        if startquiz == 1:
            print("Welcome to the GK Quiz! Good luck!")
            question1()
            break
        elif startquiz == 2:
            print("You have chosen to not participate in the quiz.")
            break
        else:
            print("Please enter 1 or 2")

name = input("What is your name?")

print("Welcome", name, "to your quiz!")

while True:
    welcome = input("Are you ready to play now? Y or N")
    if welcome == "Y":
        print("The quiz will start now.")
        gkquiz()
        break
    elif welcome == "N":
        print("The game quiz not start now.")
        break
    else:
        print("Not a valid response, please say Y or N")
