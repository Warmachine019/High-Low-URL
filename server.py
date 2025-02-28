import random
from flask import Flask

random_no = random.randint(0, 100)
print(random_no)
#Remove the print statement if you dont want the user to get a hint to what the number is.

app = Flask(__name__)

def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"

    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"

    return wrapper

@app.route("/")
@make_bold
def home():
    return ('<h1>Guess any number from 0-100</h1>'
            '<h2>And then type it in the URL bar with a "/"</h2>'
            '<img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExcXN3OXR0MDNuMmdxamxka3FpMDJxY3ExZGdpbDQyN2pmOXlnaHdrYiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/y65VoOlimZaus/giphy.gif">')

@app.route("/<int:guess>")
def guess_number(guess):
    if guess > random_no:
        return ("<h1 style='color: red'>Go lower.</h1>"
                "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNWdoaDNoYXV5a2ttY2FxaW0zZnhsazYxMGs1MzEyeTJ3NTJ5OHNrNSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/nzsWN8iSDwSlhCDokc/giphy.gif'/>")

    elif guess < random_no:
        return ("<h1 style='color: blue'>Go higher</h1>"
                "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExanRoOWNvdjlvOTh5b2JiejN2enV0aTlrOHV6bm02dGY0ZmVpYnE1biZlcD12MV9naWZzX3NlYXJjaCZjdD1n/IwAZ6dvvvaTtdI8SD5/giphy.gif'/>")
    else:
        return ("<h1 style='color: green'>Correctly Guessed!</h1>"
                "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExanRoOWNvdjlvOTh5b2JiejN2enV0aTlrOHV6bm02dGY0ZmVpYnE1biZlcD12MV9naWZzX3NlYXJjaCZjdD1n/cXblnKXr2BQOaYnTni/giphy.gif'/>")

if __name__ == "__main__":
    app.run(debug=False)
    #Change "debug" value to true in case you want to restart the server with changes everytime you save the file
