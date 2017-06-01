from level import Level


#Quiz prompts#
quiz_text = {'Easy':"""*Basic Python*

A common first thing to do in a language is display, 'Hello __1__!'

In __2__ this is particularly easy; all you have to do is type in:
__3__ 'Hello __1__!'

Of course, that isn't a very useful thing to do. However, it is an
example of how to output to the user using the __3__ command, and
produces a program which does something, so it is useful in that capacity.

It may seem a bit odd to do something in a Turing complete language that
can be done even more easily with an __4__ file in a browser, but it's
a step in learning __2__ syntax, and that's really its purpose.
""",

'Medium':"""*Methods*
A __1__ is created with the def keyword.  You specify the inputs a
__1__ takes by adding __2__ separated by commas between the parentheses.
__1__s by default returns __3__ if you don't specify the value to Return.
__2__ can be standard data types such as string, integer, dictionary, tuple,
and __4__ or can be more complicated such as objects and lambda functions.
""",

'Hard':"""*Documentation*
Python has a unique commenting style using __1__.
A doc string is a string that is the first statement in a __2__, module,
class or function. These strings can be extracted automatically through
the __3__ member of the object and are used by __4__.

"""}
#------#

#Quiz Answers
answers = {'Easy':['World','python','print','html'],
'Medium':['function','arguments','None','list'],
'Hard':['doc strings','package','__doc__','pydoc']}

#choices = []
#-------#

#Prompting the user
questions = ["""What should be substituted in for __1__?""", """What should be substituted in for __2__?""", """What should be substituted in for __3__?""","""What should be substituted in for __4__?"""]

holders = ['__1__','__2__','__3__','__4__']
#------#

def quiz(Level):
    """
    Displays question prompts and fills in with responses.
    """
    print (Level.name, Level.questions)
    index = 0
    while index < 4:
        print(questions[index] + " ")
        answer = input()
        if answer == Level.answers[index]:
            print ("Correct!")
            index += 1
            Level.questions = (Level.questions.replace("__"+str(index)+"__", answer))
            print (Level.questions)
        else:
            print("Try again!")
    print ("You win! Game over")


Easy = Level("Easy",quiz_text["Easy"],answers["Easy"])
Medium = Level("Medium",quiz_text["Medium"],answers["Medium"])
Hard = Level("Hard",quiz_text["Hard"],answers["Hard"])
#levels = [Easy, Medium, Hard]

def choose_level():
    print ("Here is a quiz to test your knowledge of python. First, choose your level.\n Easy, Medium, or hard?")
    answer = input("Level:")
    if answer in ["Easy", "easy"]:
        answer = Easy
    if answer in ["Medium", "medium"]:
        answer = Medium
    if answer in ["Hard", "hard"]:
        answer = Hard
    Level = answer
    quiz(Level)

choose_level()
