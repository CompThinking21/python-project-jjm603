import random
#This function creates a mainmenu, where the user can choose which game they would like to play. Once every game is finished, the player is returned back to the main menu and can pick again
def mainmenu():
    user = str(input('Welcome to the Main Menu. There are many rooms with games and their respective masters. There are 3 rooms, choose a room to challenge an opponent or input 5 to quit:'+' ')).lower()
    if user == '1':
        rps()
    elif user == '2':
        highlow()
    elif user == '3':
        hang()
    elif user == '5':
        quit()
#This is a game called higher or lower. The player is prompted to guess if the random number chosen is above, below or equal to 50.
def highlow():
    user = str(input('Is the number higher, lower or equal to 50:'+ ' ')).lower()
#this line of code takes the user input and puts it in lowercase characters.
    computer = random.randint(1,100)
#I use if statements to tell whether or not the player was correct and send them back to the main menu afterwards.
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

#these are all the results for the outcomes of a rock paper scissors game. It then prints to the terminal what the player and computer chose and who won.

#This is a hangman game. The player has to guess the letters or guess the word in order to win the game.
def hang():
#a list of animals that are going to be the words that the player has to guess.
    words = [ "Aardvark",
    "Albatross",
    "Alligator",
    "Alpaca",
    "Ant",
    "Anteater",
    "Antelope",
    "Ape",
    "Armadillo",
    "Donkey",
    "Baboon",
    "Badger",
    "Barracuda",
    "Bat",
    "Bear",
    "Beaver",
    "Bee",
    "Bison",
    "Boar",
    "Buffalo",
    "Butterfly",
    "Camel",
    "Capybara",
    "Caribou",
    "Cassowary",
    "Cat",
    "Caterpillar",
    "Cattle",
    "Chamois",
    "Cheetah",
    "Chicken",
    "Chimpanzee",
    "Chinchilla",
    "Chough",
    "Clam",
    "Cobra",
    "Cockroach",
    "Cod",
    "Cormorant",
    "Coyote",
    "Crab",
    "Crane",
    "Crocodile",
    "Crow",
    "Curlew",
    "Deer",
    "Dinosaur",
    "Dog",
    "Dogfish",
    "Dolphin",
    "Dotterel",
    "Dove",
    "Dragonfly",
    "Duck",
    "Dugong",
    "Dunlin",
    "Eagle",
    "Echidna",
    "Eel",
    "Eland",
    "Elephant",
    "Elk",
    "Emu",
    "Falcon",
    "Ferret",
    "Finch",
    "Fish",
    "Flamingo",
    "Fly",
    "Fox",
    "Frog",
    "Gaur",
    "Gazelle",
    "Gerbil",
    "Giraffe",
    "Gnat",
    "Gnu",
    "Goat",
    "Goldfinch",
    "Goldfish",
    "Goose",
    "Gorilla",
    "Goshawk",
    "Grasshopper",
    "Grouse",
    "Guanaco",
    "Gull",
    "Hamster",
    "Hare",
    "Hawk",
    "Hedgehog",
    "Heron",
    "Herring",
    "Hippopotamus",
    "Hornet",
    "Horse",
    "Human",
    "Hummingbird",
    "Hyena",
    "Ibex",
    "Ibis",
    "Jackal",
    "Jaguar",
    "Jay",
    "Jellyfish",
    "Kangaroo",
    "Kingfisher",
    "Koala",
    "Kookabura",
    "Kouprey",
    "Kudu",
    "Lapwing",
    "Lark",
    "Lemur",
    "Leopard",
    "Lion",
    "Llama",
    "Lobster",
    "Locust",
    "Loris",
    "Louse",
    "Lyrebird",
    "Magpie",
    "Mallard",
    "Manatee",
    "Mandrill",
    "Mantis",
    "Marten",
    "Meerkat",
    "Mink",
    "Mole",
    "Mongoose",
    "Monkey",
    "Moose",
    "Mosquito",
    "Mouse",
    "Mule",
    "Narwhal",
    "Newt",
    "Nightingale",
    "Octopus",
    "Okapi",
    "Opossum",
    "Oryx",
    "Ostrich",
    "Otter",
    "Owl",
    "Oyster",
    "Panda"
    "Panther",
    "Parrot",
    "Partridge",
    "Peafowl",
    "Pelican",
    "Penguin",
    "Pheasant",
    "Pig",
    "Pigeon",
    "Pony",
    "Porcupine",
    "Porpoise",
    "Quail",
    "Quelea",
    "Quetzal",
    "Rabbit",
    "Raccoon",
    "Rail",
    "Ram",
    "Rat",
    "Raven",
    "Reindeer",
    "Rhinoceros",
    "Rook",
    "Salamander",
    "Salmon",
    "Sandpiper",
    "Sardine",
    "Scorpion",
    "Seahorse",
    "Seal",
    "Shark",
    "Sheep",
    "Shrew",
    "Skunk",
    "Snail",
    "Snake",
    "Sparrow",
    "Spider",
    "Spoonbill",
    "Squid",
    "Squirrel",
    "Starling",
    "Stingray",
    "Stinkbug",
    "Stork",
    "Swallow",
    "Swan",
    "Tapir",
    "Tarsier",
    "Termite",
    "Tiger",
    "Toad",
    "Trout",
    "Turkey",
    "Turtle",
    "Viper",
    "Vulture",
    "Wallaby",
    "walrus",
    "wasp",
    "weasel",
    "whale",
    "wildcat",
    "wolf",
    "wolverine",
    "wombat",
    "woodcock",
    "woodpecker",
    "worm",
    "wren",
    "yak",
    "zebra"]
    word = random.choice(words).lower()
    abc = ('abcdefghijklmnopqrstuvwxyz')
#list to make sure the player is only using letters when guessing.
    letters_guessed = []
#a list to put all the letters in that have already been guessed. This is so the player doesn't use the same letters again.
    turns = 7
    guessed = False
    print()
    print('The word contains', len(word), 'letters.')
    print(len(word)*'_')
    while guessed == False and turns > 0:
        print('You have ' + str(turns) + ' turns')
        user = input('Guess a letter in the word or enter the full word: ').lower()
    #These if statements are the responses to the guesses from the user. Some of it is to tell the user when their answer isn't a letter or if they already guessed the letter before.
        if len(user) == 1:
            if user not in abc:
                print('Not a letter')
            elif user in letters_guessed:
                print('This was guessed before')
            elif user not in word:
                print('That letter is not part of the word')
                letters_guessed.append(user)
                turns-=1
            elif user in word:
                print('That letter exist')
                letters_guessed.append(user)
            else:
                print('Invalid answer')
        elif len(user) == len(word):
            if user == word:
                print('You guessed the word correctly. You Win!!!')
                guessed = True
                mainmenu()
            else:
                print('That is the wrong word')
                turns -=1
        else:
            print('Your guess is not the same length as the word.')
            turns-=1
#This is to print the blank spaces when the letters haven't been guessed yet. Goes throght each letter and sees if it is in the list of guessed letters. It also sees when the player guesses the full word.
        status = ''
        if guessed == False:
            for letter in word:
                if letter in letters_guessed:
                    status += letter
                else:
                    status += '_'
            print(status)
        if status == word:
            print('You guessed the word correctly. You Win!!!')
            guessed = True
            mainmenu()
        elif turns == 0:
            print('The word was ' +str(word)+ '. You Lose...')
            mainmenu()
mainmenu()
