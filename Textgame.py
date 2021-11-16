import random
def mainmenu():
    user = str(input('Welcome to the Main Menu. There are many rooms with games and their respective masters. There are 4 rooms, choose a room to challenge an opponent or input 5 to quit:'+' ')).lower()
    if user == '1':
        rps()
    elif user == '2':
        highlow()
    elif user == '5':
        quit()

def highlow():
    user = str(input('Is the number higher, lower or equal to 50:'+ ' ')).lower()
    computer = random.randint(1,100)

    if user == 'higher' and (computer > 50):
        print('The Number is Higher. You Win!!!')
        mainmenu()
    elif user == 'higher' and (computer < 50):
        print('The Number is Lower. You Lose...')
        mainmenu()
    elif user == 'equal' and (computer > 50):
        print('The Number is Higher. You Lose...')
        mainmenu()
    elif user == 'lower' and (computer < 50):
        print('The Number is Lower. You Win!!!')
        mainmenu()
    elif user == 'lower' and (computer > 50):
        print('The Number is Higher. You Lose...')
        mainmenu()
    elif user == 'equal' and (computer < 50):
        print('The Number is Lower. You Lose...')
        mainmenu()
    elif user == 'higher' and (computer == 50):
        print('The Number is equal to 50. You Lose...')
        mainmenu()
    elif user == 'lower' and (computer == 50):
        print('The Number is equal to 50. You Lose...')
        mainmenu()
    elif user == 'equal' and (computer == 50):
        print('The Number is equal to 50. You Win!!!')
        mainmenu()
    else:
        print('No option selected, try again.')
        highlow()
#This a rock paper scissors game. It takes a play(Rock, paper or scissors) from the user and put it against the computer. The computer randomly picks a play and goes against the user. I use if statements to compare the plays against each other and print out a string that says who wins.
def rps():
    user = str(input('Rock, Paper or Scissors:'+ ' ')).lower()
#this takes a play from the user and puts it against a randomized computer play
    plays = ['rock' , 'paper' , 'scissors']
    computer = random.choice(plays)
#This is to have the computer opponent pick randomly from the plays list.
    if user == computer:
        print("Both have selected the same play")
        rps()
    elif user == 'rock':
        if computer == 'scissors':
            print('Rock smashed Scissors! You Win!!!!')
            mainmenu()
        else:
            print('Paper covered Rock! You Lose...')
            mainmenu()
    elif user == 'paper':
        if computer == 'rock':
            print('Paper covered Rock! You Win!!!')
            mainmenu()
        else:
            print('Scissors cuts Paper! You Lose...')
            mainmenu()
    elif user == 'scissors':
        if computer == 'paper':
            print('Scissors cuts Paper! You Win!!!')
            mainmenu()
        else:
            print('Rock smashed Scissors! You Lose...')
            mainmenu()
    else:
        print('No option selected, try again.')
        rps()
        # raise TypeError("That is not an option.")
#these are all the results for the outcomes of a rock paper scissors game. It then prints to the terminal what the player and computer chose and who won.
mainmenu()

def hang():
    words = ['dog', 'cat', 'monster']
    word = random.choice(words)
    user = str(input('Guess a letter:'+ ' ')).lower()
    
