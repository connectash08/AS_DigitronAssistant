import wolframalpha
import webbrowser
import wikipedia as wiki #Use this line to import wikipedia package as wiki keyword
import random
import time
from tkinter import *
from tkinter.ttk import *
from time import strftime
from PyDictionary import PyDictionary
from nltk.corpus import wordnet
client = wolframalpha.Client('3LLJ9Y-4XK54W5UPL')
end = False
print('Digitron Version 5 System Activated')

def wikipedia():
    print("What is your question: ")
    wikiquestion = input()
    wikiquestion.lower()
    result = wiki.summary(wikiquestion) #This gives the summary of the keyword that the user entered
    print(result)

def wolframalpha():
    print("What is your question: ")
    question = input()
    userquestion = client.query(question)
    results = next(userquestion.results).text
    print(results)
    
def internet():
    print("What would you like to search (ex: google, youtube): ")
    website = input()
    website.lower()
    webbrowser.open("https://www."+website+".com")
    
def game():
    list1 = ["Rock","Paper","Scissors"]
    userscore = 0
    computerscore = 0
    print("Welcome to Rock, Paper, Scissors!")
    time.sleep(0.5)
    print("The objective of this game is to choose an option that will beat the opponent's option (ex: Rock beats Scissors)")
    time.sleep(0.5)
    print("You will have 3 rounds to score against the computer!")
    time.sleep(0.5)
    print("Good Luck!")
    time.sleep(0.5)
    for a in range(1,4,1):
        print("Round",a)
        print("Choose Rock, Paper, or Scissors!")
        print("Enter your option here: ")
        userinput = input()
        choice = userinput.lower()
        computerchoice = random.choice(list1)
        if choice == "rock" and computerchoice == "Scissors":
            print("Player won!")
            print("Computer selected",computerchoice)
            userscore = userscore + 1
        if choice == "rock" and computerchoice == "Paper":
            print("Computer Won!")
            print("Computer selected",computerchoice)
            computerscore = computerscore + 1
        if choice == "rock" and computerchoice == "Rock":
            print("It's a tie!")
            print("Computer also selected",computerchoice)
            print("No points are given")
        if choice == "paper" and computerchoice == "Rock":
            print("Player Won!")
            print("Computer selected",computerchoice)
            userscore = userscore + 1
        if choice == "paper" and computerchoice == "Scissors":
            print("Computer Won!")
            print("Computer selected",computerchoice)
            computerscore = computerscore + 1
        if choice == "paper" and computerchoice == "Paper":
            print("It's a tie!")
            print("Computer also selected",computerchoice)
            print("No points are given!")
        if choice == "scissors" and computerchoice == "Rock":
            print("Computer Won!")
            print("Computer selected",computerchoice)
            computerscore = computerscore + 1
        if choice == "scissors" and computerchoice == "Paper":
            print("Player won!")
            print("Computer selected",computerchoice)
            userscore = userscore + 1
        if choice == "scissors" and computerchoice == "Scissors":
            print("It's a tie!")
            print("Computer also selected",computerchoice)
            print("No points are given")
    print("It's now time to see who won")
    print("Tallying up the points...")
    if userscore > computerscore:
        print("The Player Won! Great Job!")
        print("Player Score: ",userscore)
        print("Computer score: ",computerscore)
    if computerscore > userscore:
        print("The Computer Won! Better luck next time")
        print("Player Score: ",userscore)
        print("Computer score: ",computerscore)
    if userscore == computerscore:
        print("It's a draw!")
        print("Player Score: ",userscore)
        print("Computer score: ",computerscore)
        
def timeclock():
    main = Tk()
    main.title("Digital Clock")
    def clock():
        tick = strftime("%H: %M: %S %p")
        clock_label.config(text = tick)
        clock_label.after(1000,clock)
    clock_label = Label(main, font =("times", 80), background = "white", foreground = "black")
    clock_label.pack(anchor = "center")
    clock()
    mainloop()
    
def dictionary():
    dictionary = PyDictionary()
    print("Enter a word to define: ")
    define_word = input() #Input gathered to find word to define
    print("Gathering definition...")
    definition = dictionary.meaning(define_word) #Searches the definition for the word stated
    print(definition) #Prints the definition of the word in Python Shell

while end != True:
    print("Avaliable services are: Shutdown, Wikipedia, Wolframalpha, Internet, Game, Clock, Dictionary")
    print("Please enter your command: ")
    service = input().lower()
    if service == "wikipedia":
        wikipedia()
    elif service == "wolframalpha":
        wolframalpha()
    elif service == "internet":
        internet()
    elif service == "shutdown":
        print("Shutting down")
        end = True
    elif service == "game":
        game()
    elif service == "clock":
        timeclock()
    elif service == "dictionary":
        dictionary()
            
    
        
