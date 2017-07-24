#Hour 22 exercise
#Testing out git and github
#merging branches.
#

from random import randint

def main():
    print "Welcome to the number guessing game! You get five chances."
    number = randint(1, 10)
    tries = 0
    
    while True:
        guess = raw_input("Guess a number between one and ten: ")
        
        if int(guess) == number:
            print "That's right!"
            break
        else:
            tries = tries + 1
            attempts = 5 - tries
            if tries == 5:
                print "That's not right. Sorry! Game over."
                print "My number was {}.".format(number)
                break
            else:
                print "That's not right. Sorry! You have {} attempts left.".format(attempts)

if __name__ == '__main__':
    main()
