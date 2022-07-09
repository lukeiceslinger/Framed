import random
import time
from time import sleep
import sys

# Game invite
print("\nWelcome to the 'framed'! \n"
        "You only get 9 chances to predict the movie, be a real clairvoyant! \n"
        "If not, there is no place for doltish being and you shall be HANGED!")
time.sleep(3)
name = input("What do we call you ? : ")
print("\nHello " + name + ", Hope you don't get hung!\n")
time.sleep(1)
print("Initiating game...\n")

#loading to build up the tention :
for i in range(21):
    sys.stdout.write('\r')
    sys.stdout.write("%-20s %d%%" % ('-'*i, 5*i))
    sys.stdout.flush()
    sleep(0.25)

time.sleep(1)
# main objects needed for the game:
def main():
    global cnt
    global show
    global movie
    global assumed_word
    global size
    global execute
    global search
    # movies to predict.
    movies_data = ["godfather","aliens","argo","goodfellas","seven","maleficent","cars","jumanji","frozen","brave","pinocchio","scream","cinderella","poltergiest",
                       "lincoln","batman","superman","flash","avengers","dracula","thor","spiderman","ironman","jaws","psycho","titanic","inception" ] 
    movie = random.choice(movies_data)
    size = len(movie)
    cnt = 0
    search = movie
    show = '_' * size
    assumed_word = []
    execute = ""
# for the continuation of the round after first round is over:
def play_loop():
    global execute
    execute = input("Wish to continue? y/n \n")
    while execute not in ["y", "n","Y","N"]:
        execute = input("stick with the y or n options. CAN YOU CONTINUE STILL? y = yes, n = no \n")
    if execute == "y":
        main()
    elif execute == "n":
        print("Hope to see you risk it all again!")
        exit()
#conditions in game:
def framed():
    global cnt
    global show
    global movie
    global assumed_word
    global execute
    global search
    lives = 9
    predict = input("\nMovie that might doom you is : " + show + " Enter your predict: \n")
    predict = predict.strip()
    if len(predict.strip()) == 0 or len(predict.strip()) >= 2 or predict <= "9":
        print("Input is Invalid, Try again with a letter.\n")
        framed()

        
    elif predict in movie:
        assumed_word.extend([predict])
        index = movie.find(predict)
        movie = movie[:index] + "_" + movie[index + 1:] 
        show = show[:index] + predict + show[index + 1:]
        print(show + "\n")
    elif predict in assumed_word:
        print("Try different letter.\n")
    else:
        cnt += 1
        if cnt == 1:
            time.sleep(.5)
            print("  |      ")
            time.sleep(.5)
            print("  |      ")
            time.sleep(.5)
            print("__|__\n")
            print("BUZZ!! " + str(lives - cnt) + " lives left\n")
        elif cnt == 2:
            time.sleep(.5)
            print("  |      ")
            time.sleep(.5)
            print("  |      ")
            time.sleep(.5)
            print("  |      ")
            time.sleep(.5)
            print("__|__    ")
            print("BUZZ!! " + str(lives - cnt) + " lives left\n")
        elif cnt == 3:
            time.sleep(.5)
            print("   _ ")
            time.sleep(.5)
            print("  |     ")
            time.sleep(.5)
            print("  |      ")
            time.sleep(.5)
            print("  |      ")
            time.sleep(.5)
            print("  |      ")
            time.sleep(.5)
            print("__|__    ")
            print("BUZZ!! " + str(lives - cnt) + " lives left\n")
        elif cnt == 4:
            time.sleep(.5)
            print("   ___ ")
            time.sleep(.5)
            print("  |     ")
            time.sleep(.5)
            print("  |      ")
            time.sleep(.5)
            print("  |      ")
            time.sleep(.5)
            print("  |      ")
            time.sleep(.5)
            print("__|__    ")
            print("BUZZ!! " + str(lives - cnt) + " lives left\n")
        elif cnt == 5:
            time.sleep(.5)
            print("   _____ ")
            time.sleep(.5)
            print("  |     ")
            time.sleep(.5)
            print("  |      ")
            time.sleep(.5)
            print("  |      ")
            time.sleep(.5)
            print("  |      ")
            time.sleep(.5)
            print("__|__    ")
            print("BUZZ!! " + str(lives - cnt) + " lives left\n")
        elif cnt == 6:
            time.sleep(.5)
            print("   _____ ")
            time.sleep(.5)
            print("  |     |")
            time.sleep(.5)
            print("  |      ")
            time.sleep(.5)
            print("  |      ")
            time.sleep(.5)
            print("  |      ")
            time.sleep(.5)
            print("__|__    ")
            print("BUZZ!! " + str(lives - cnt) + " lives left\n")
        elif cnt == 7:
            time.sleep(.5)
            print("   _____  ")
            time.sleep(.5)
            print("  |     | ")
            time.sleep(.5)
            print("  |     O ")
            time.sleep(.5)
            print("  |       ")
            time.sleep(.5)
            print("  |       ")
            time.sleep(.5)
            print("__|__     ")
            print("BUZZ!! " + str(lives - cnt) + " lives left\n")
        elif cnt == 8:
            time.sleep(.5)
            print("   _____   ")
            time.sleep(.5) 
            print("  |     |  ")
            time.sleep(.5)
            print("  |     O  ")
            print("  |    /|\ ")
            time.sleep(.5)
            print("  |        ")
            time.sleep(.5)
            print("__|__      ")
            print("BUZZ!! " + str(lives - cnt) + " chance is all you got now.\n")
        elif cnt == 9:
            time.sleep(.5)
            print("   _____   ")
            time.sleep(.5) 
            print("  |     |  ")
            time.sleep(.5)
            print("  |     O  ")
            print("  |    /|\ ")
            print("  |    / \ ")
            time.sleep(.5)
            print("__|__      ")
            print("\n\nBUZZ!!!!!\n")
            print("The movie was:",search)
            play_loop()
    if movie == '_' * size:
        print("Congratulations! You got the movie right!")
        play_loop()
    elif cnt != lives:
        framed()
main()
framed()
