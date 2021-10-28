import random
#This a rock paper scissors game. It takes a play(Rock, paper or scissors) from the user and put it against the computer. The computer randomly picks a play and goes against the user. I use if statements to compare the plays against each other and print out a string that says who wins.
user = input('Rock, Paper or Scissors:'+ ' ')
#this takes a play from the user and puts it against a randomized computer play
plays = ['rock' , 'paper' , 'scissors']
computer = random.choice(plays)
#This is to have the computer opponent pick randomly from the plays list.
if user == computer:
    print("Both have selected the same play")
elif user == 'rock':
    if computer == 'scissors':
        print('Rock smashed Scissors! You Win!!!!')
    else:
        print('Paper covered Rock! You Lose...')
elif user == 'paper':
    if computer == 'rock':
        print('Paper covered Rock! You Win!!!')
    else:
        print('Scissors cuts Paper! You Lose...')
elif user == 'scissors':
    if computer == 'paper':
        print('Scissors cuts paper! You Win!!!')
    else:
        print('Rock smashed Scissors! You Lose...')
#these are all the results for the outcomes of a rock paper scissors game. It then prints to the terminal what the player and computer chose and who won.
