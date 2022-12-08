import random

def main():
    print("I thought of a number between 1 and 100.")
    r = random.randint(1,100)
    talalt=False
    guesses=0
    while talalt==False:
        n=int(input("your guess> "))
        if n<r:
            print("my number is bigger")
            guesses+=1
        if n>r:
            print("my number is smaller")
            guesses+=1
        if n==r:
            talalt=True
            guesses+=1
            print("Good job! That's it!")
            print("Number of guesses: {0}".format(guesses))
if __name__=="__main__":
    main()