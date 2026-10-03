import argparse
import sys

args = {3: "Fizz", 5: "Buzz", 7: "Fang", 11: "Bang"}

# define fizzbuzz game
def fizzbuzz(i, args={3: "Fizz", 5: "Buzz", 7: "Fang", 11: "Bang"}):
    for num in range(1,i+1):
        phrase = ""
        for factor, word in args.items():
            if num % factor == 0:
                phrase += word
        if phrase:
            print(phrase)
        else:
            print(num)

# parse_args function add-on done with the help of Ana Anaya
# i simply could not make this behave, so it currently does not get called
def parse_args():
    if __name__ == '__main__':
        parser = argparse.ArgumentParser(description="Fizzbuzz!")
        parser.add_argument("-rule", action="append", nargs=2, metavar=("Factor", "Word"))
        args = parser.parse_args()
        userargs = {3: "Fizz", 5: "Buzz", 7: "Fang", 11: "Bang"}
        if args.rule:
            for factor, word in args.rule:
                userargs[int(factor)] = word

# check if user wants custom factors and words
def customise(i):
    flip2 = False
    while flip2 == False:
        yn = input("Use custom parameters (y/n)? ")
        yn = yn.strip().lower()
        if yn == 'y':
            args = {}
            userargs = input("Input your own number and replacement word: ")
            usernum, userword = userargs.split(" ")
            try:
                usernum = int(usernum)
            except ValueError:
                print("Failed to assign number. Please try again.")
                customise(i)
            args.update({usernum: userword})
            fizzbuzz(i, args)
            flip2 = True
        elif yn == 'n':
            fizzbuzz(i)
            flip2 = True
        elif yn != 'y' and yn != 'n':
            print("Invalid input.")
            pass

# take and check user input
i = input("Please enter a maximum number: ")

flip1 = False
while flip1 == False:
    try:
        i = int(i)
        flip1 = True
    except ValueError:
        i = input("Invalid input. Please enter a maximum number: ")
if flip1 == True:
    customise(i)
