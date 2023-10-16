
from nltk.chat.util import Chat, reflections
from datetime import datetime
import pytz
# Define pairs - patterns and responses
#This code creates a basic chatbot using NLTK in Python.
#It defines patterns and responses for various user inputs.
#The chatbot responds to user input based on matching patterns.
#It can provide information about time, date, Python, and has some custom responses.
#The code runs in an infinite loop, continuously taking user input and responding until the user types "quit."
pairs = [
    (r'hello|hi|hey', ['Hi there!', 'Hello!', 'Hey!']),
    (r'how are you', ['I\'m good, thanks. How can I help you today?',
     'I\'m just a bot, but I\'m here to assist.']),
    (r'what is your name', ['I am a DARKHAT.', 'You can call me ChatGPT.']),
    (r'bye|goodbye', ['Goodbye!', 'See you later!', 'Farewell!']),
    (r'who are you', ['I am an AI DARKHAT created by OpenAI.',
     'I\'m your friendly virtual assistant.']),
    (r'help', ['Sure, I can help you with various tasks. Just ask me anything!']),
    (r'(.*) (age|old) (are you|are you?|are you old)',
     ['I don\'t have an age because I\'m just a computer program.']),
    (r'what can you do', [
     'I can answer questions, provide information, and assist with various tasks.']),
    (r'(.*) (love|like) you',
     ['I\'m just a machine, but I appreciate the sentiment!']),
    (r'(.*) (time|current time)', ['The current time in India is {}.'.format(
        datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%H:%M %p'))]),
    (r'(.*) (date|today\'s date)', ['Today\'s date in India is {}.'.format(
        datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%Y-%m-%d'))]),
    (r'(.*) (day|today)', ['Today in India is {}.'.format(
        datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%A'))]),
    (r'(.*) (month|current month)', ['The current month in India is {}.'.format(
        datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%B'))]),
    (r'(.*) (year|current year)', ['The current year in India is {}.'.format(
        datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%Y'))]),
    (r'kaisan baru', ['thik bani prince or bata kay hal ha.']),
    (r'or bhi', ['ma thik hu tu baat']),
    (r'2247110',['vishal kumar Bca 3 sem 2 year 9608339846']),
    (r'time',['check your mobile on watch']),
    (r'python|what is python',['Python is a popular programming language. It was created by Guido van Rossum, and released in 1991.']),
    (r'note|python notes',['https://www.python.org/']),
    (r'buy',['chal ja ']),
    


]
# Create the DARKHAT
DARKHAT = Chat(pairs, reflections)

# Interaction loop
while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        print("DARKHAT: Goodbye!")
        break
    response = DARKHAT.respond(user_input)
    print("DARKHAT:", response)
