import random
import time
print("WELCOME TO HANGMAN GAME")
print("------------------------------------------------------")
name=input("enter your name\n")
print("WELCOME",name)
time.sleep(1)
print("------------------------------------------------------")
time.sleep(2)
print("LET'S PLAY! :)")
time.sleep(2)
fruits=['apple','banana','mango','guava','orange','llgll']
nature=['plant','tree','mountain','river','ocean','sun','moon']
sports=['cricket','badminton','golf','basketball','volleyball']
choice=input("choose your interested topic to continue\n Fruits\n Nature\n Sports\n Exit\n")
pts=0
life=7
hang=[
'''
        +-----+
        O     |
              |
              |
            === ''',
'''
        +-----+
        O     |
        |     |
              |
            === ''',
'''
        +-----+
        O     |
       /|     |
              |
            === ''',
'''
        +-----+
        O     |
       /|\    |
              |
            === ''',
'''
        +-----+
        O     |
       /|\    |
        |     |
            ===
''',
'''
        +-----+
        O     |
       /|\    |
        |     |
       /    ===
''',
'''
        +-----+
        O     |
       /|\    |
        |     |
       / \  ===
'''
]

match (choice):
    case 'fruits':
        chosen_word=random.choice(fruits)
        # display_word=print(chosen_word.title())

        display=[]
        for i in range(len(chosen_word)):
            display += "_"
        print(display)

        for letter in range(20):
            if life==0:
                break;
            if '_'not in display:
                break;
            else:
                guess=input("guess a letter\n").lower()
                for j in range(len(chosen_word)):
                    word= chosen_word[j]
                    if guess==word:
                        display[j]=word
                        pts+=10
                        # print(display)
                    elif guess not in chosen_word:
                        life=life-1
                        print(life)
                        if life == 6:
                            print(hang[0])
                        if life == 5:
                            print(hang[1])
                        if life == 4:
                            print(hang[2])
                        if life == 3:
                            print(hang[3])
                        if life == 2:
                            print(hang[4])
                        if life == 1:
                            print(hang[5])
                        if life == 0:
                            print(hang[6])
                        break;
                print(display)
        # print("POINTS WON=", pts)


    case 'nature':
        chosen_word = random.choice(nature)
        # display_word = print(chosen_word.title())
        display = []
        for i in range(len(chosen_word)):
            display += "_"
        print(display)

        for letter in range(20):
            if life==0:
                break;
            if '_' not in display:
                break;
            else:
                guess = input("guess a letter\n").lower()
                for j in range(len(chosen_word)):
                    word = chosen_word[j]
                    if word == guess:
                        display[j] = word
                        pts+=10
                    elif guess not in chosen_word:
                        life = life - 1
                        print(life)
                        if life == 6:
                            print(hang[0])
                        if life == 5:
                            print(hang[1])
                        if life == 4:
                            print(hang[2])
                        if life == 3:
                            print(hang[3])
                        if life == 2:
                            print(hang[4])
                        if life == 1:
                            print(hang[5])
                        if life == 0:
                            print(hang[6])
                        break;
                print(display)

    case 'sports':
        chosen_word = random.choice(sports)
        # display_word = print(chosen_word.title())
        display = []
        for i in range(len(chosen_word)):
            display += "_"
        print(display)

        for letter in range(20):
            if life==0:
                break;
            if '_' not in display:
                break;
            else:
                guess = input("guess a letter\n").lower()
                for j in range(len(chosen_word)):
                    word = chosen_word[j]
                    if guess == word:
                        display[j] = word
                        pts+=10
                    elif guess not in chosen_word:
                        life = life - 1
                        print(life)
                        if life == 6:
                            print(hang[0])
                        if life == 5:
                            print(hang[1])
                        if life == 4:
                            print(hang[2])
                        if life == 3:
                            print(hang[3])
                        if life == 2:
                            print(hang[4])
                        if life == 1:
                            print(hang[5])
                        if life == 0:
                            print(hang[6])
                        break;
                print(display)

    case exit:
        print("BYE,COME AGAIN")



print("POINTS WON=", pts)
if pts ==0:
    print("Oops! Better luck next time")
else:
    print("Hey",name,"You have won",pts,"points")