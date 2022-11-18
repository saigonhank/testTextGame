# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random


def gameOver():
    print("THE GAME IS OVER")
    print("YOU LOSE")
    print("GOOD DAY SIR!")
    exit()

def wrong_answer(lives, topic):
    lives -= 1
    if lives == 0:
        gameOver()
    else:
        tryagain = input("oops you failed! try again: yes or no? ")
        while tryagain != "yes" and tryagain != "no":
            tryagain = input("i dunno what that means... yes or no? ")
        if tryagain == "yes":
            if topic == 'math':
                mathQuestions(lives)
            if topic == 'ling':
                lingQuestions(lives)
            if topic == "ticTacToe":
                levelTwo(lives)
            if topic == "3e":
                levelThreeEasy(lives)
        if tryagain == "no":
            if topic == 'math':
                print("well let's go for linguistics, son")
                lingQuestions(lives)
            if topic == 'ling':
                print("lolok math time sucka")
                mathQuestions(lives)
            else:
                gameOver()


def lingQuestions(lives):
    print(f"Welcome to the linguistics room! You have {lives} lives. "
          "You must answer 2 questions in a row correctly to move to level 2!")
    ans = input("Question 1. which of the following is not a stop consonant? b p m d k ")
    if ans == 'm':
        print("nice, 1 down,,, 2 to go")
    else:
        wrong_answer(lives, "ling")

    ans = input("Question 2. which of the following words lacks a consonant cluster sound ? "
                "than, bank, joint, paint, press ")
    if ans == 'than':
        print("indeed")
        levelTwo(lives)
    else:
        wrong_answer(lives, "ling")


def mathQuestions(lives):
    print(f"Welcome to the math room! You have {lives} lives. "
          "You must answer 3 questions in a row correctly to move to level 2!")
    ans = input("Question 1. What is 5! ? ")
    while not ans.isdigit():
        ans = input("dude it's gotta be a number-- what is 5! ? ")
    if int(ans) == 120:
        print("good shit dawg")
    else:
        wrong_answer(lives,'math')
    ans = input("Question 2. What is 29 - 4 * 6? ")
    while not ans.isdigit():
        ans = input("dude it's gotta be a number-- What is 29 - 4 * 6? ")
    if int(ans) == 5:
        print("you a smart fella")
    else:
        wrong_answer(lives,'math')
    ans = input("Question 3. What is 1+1? ")
    while not ans.isdigit():
        ans = input("dude it's gotta be a number-- What is 1+1? ")
    if int(ans) == 2:
        print("damn. we goin to level 2 !! ")
        levelTwo(lives)
    else:
        wrong_answer(lives,'math')


#function to insert the answer for tic tac toe (level 2)
def placeAnswer(ans, board, player):
    answers = {"A1": 0, "A2": 1, "A3": 2,
               "B1": 3, "B2": 4, "B3": 5,
               "C1": 6, "C2": 7, "C3": 8}
    #the dumb AI starts from the top left and chooses the first available square
    if player == "o":
        for i in range(0, len(board)):
            if board[i] == 'a':
                print(f"The computer chooses "
                      f"{list(answers.keys())[list(answers.values()).index(i)]}")
                board[i] = 'o'
                return board
    if board[answers[ans]] == 'x' or board[answers[ans]] == 'o':
        print("That square is already taken! "
              "You lose a turn! :(")
    else:
        board[answers[ans]] = player
    return board


#function to check if there is a winner after each move in tictactoe (level2)
def checkBoard(board):
    for i in range(0,3):
        #check if there is a winner via columns
        if board[i] == board[i+3] == board[i+6] and board[i] != 'a':
            if board[i] == 'x': return 1
            if board[i] == 'o': return 2


    for i in range(0,9,3):
        #check if there is a winner via rows
        if board[i] == board[i+1] == board[i+2] and board[i] != 'a':
            if board[i] == 'x': return 1
            if board[i] == 'o': return 2

    #check if AI wins via 1 of 2 diagonals
    if board[0] == board[4] == board[8] == 'o'\
            or board[6] == board[4] == board[2] == 'o':
        return 2
    #check if player wins via 1 of 2 diagonals
    if board[0] == board[4] == board[8] == 'x'\
            or board[6] == board[4] == board[2] == 'x':
        return 1

    #check if the board is full with no winner
    if 'a' not in board:
        print("The FINAL board is")
        print(board[0:3])
        print(board[3:6])
        print(board[6:])
        print("The board is full! No moves remain! It's a draw. :(((")
        return 2
    return 0


def levelTwo(lives):
    board = ['a','a','a','a','a','a','a','a','a']
    game = 0
    print("Welcome to level 2, buddy.")
    print(f"You have {lives} lives.")
    print("You will play tic tac toe against a pretty damn stupid computer.")
    print("You are 'x'. The computer is 'o'. Empty squares have 'a'.")
    print("rows are A B C")
    print("columns are 1 2 3")
    print("please type your selection as <ROW><COLUMN> e.g. A1 ")
    while game == 0:
        print("The current board is")
        print(board[0:3])
        print(board[3:6])
        print(board[6:])
        ans = "pp"
        while ans[0].upper() != "A" and ans[0].upper() != "B" and ans[0].upper() != "C"\
                or ans[1] != "1" and ans[1] != "2" and ans[1] != "3":
            ans = input("what is your selection? ")

        board = placeAnswer(ans.upper(), board, "x")

        game = checkBoard(board) #check if game is over before AI enters a new slot
        if game != 0:
            break

        board = placeAnswer("", board, "o")

        game = checkBoard(board) #check if game is over before prompting user for new slot

    if game == 1:
        print("YOU WIN")
        levelThree(lives)
    else:
        wrong_answer(lives, "ticTacToe")

def levelThreeEasyRoom2(lives, room):
    if room == 7:
        print("nice, you made it to safety...")
        print("The whole game is over")
        print("Ngủ ngon đi bạn ơi")
        return
    print(f"Nice, you made it to room {room}!")
    print("The fire feels very close to you on the left....")
    if room == 2:
        door = input("Do you want to go to the 'left' or 'down'? ")
        while door != 'left' and door != 'down':
            door = input("Sir, you must type 'left' or 'down'. ")
    elif room == 6:
        door = input("Hmmm... this room also has a room to the 'right'!")
        while door != 'left' and door != 'right' and door != 'down' and door != 'up':
            door = input("Sir, you must type 'left', 'right', 'up' or 'down'. ")
    else:
        door = input("Do you want to go to the 'left', 'up', or 'down'? ")
        while door != 'left' and door != 'down' and door != 'up':
            door = input("Sir, you must type 'left', 'up', or 'down'. ")
    if door == 'right':
        print("oh shit, you've been teleported!")
        levelThreeEasyRoom2(lives, random.randint(2,7))
    elif door == 'left':
        print("yep, that's fire")
        wrong_answer(lives, "3e")
    elif door == 'down':
        levelThreeEasyRoom2(lives, room+1)
    else:
        levelThreeEasyRoom2(lives, room-1)


def levelThreeEasy(lives):
    print("The god of this game has dropped you into a pit")
    print("You must find your way out quickly before you succomb to the elements.")
    print("You hear dragons to your right and sense a fire to your left.")
    print("But you're not sure how far these dangers are....")
    print("You'll have to experiment.")
    print(f"Good thing you have {lives} lives!")
    print("There are two doors in this room!")
    door = input("Do you want to go left or right? ")
    while door != "left" and door != "right":
        door = input("I am dumb as shit and can only understand if you type exactly"
                     " 'left' or 'right'. Please. ")
    if door == "right":
        print("Oh shit, there's a dragon in that room!"
              "You better go left next time. :(((")
        wrong_answer(lives, "3e")
    else: levelThreeEasyRoom2(lives, 2)



def levelThree(lives):
    print("Welcome to level 3.")
    print(f"You have {lives} lives.")
    mode = input("Type 'e' for easy, 'h' for hard. ")
    while mode.lower() != 'e' and mode.lower() != 'h':
        mode = input("Please type exactly 'e' or 'h' ")
    if mode.lower() == 'h':
        lives += 1
        print("You selected hard mode! Congrats, you received 1 more life.")
        print(f"Now, you have {lives} lives.")
    if mode.lower() == 'e':
        print("You're a puss. Whatever. Welcome to the easy mode.")
        levelThreeEasy(lives)



def introScene(name):
    topics = {'math', 'linguistics'}
    topic = input("Do you prefer math or linguistics? ")
    while topic not in topics:
        topic = input("Please type exactly 'math',  or 'linguistics'. ")
    if topic == 'math':
        mathQuestions(3)
    if topic == 'linguistics':
        lingQuestions(3)


if __name__ == '__main__':
        name = input("Welcome to the game! What's your name? ")
        print("Good luck, " + name + ".")
        introScene(name)


