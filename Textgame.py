import random

user = input('Rock, Paper or Scissors:'+ ' ')
plays = ['rock' , 'paper' , 'scissors']
computer = random.choice(plays)

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
        print('scissors cuts paper! You Win!!!')
    else:
        print('Rock smashed Scissors! You Lose...')
