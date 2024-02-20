from nltk.chat.util import Chat, reflections
from datetime import datetime
import pytz
import requests


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


google_api_key = 'YOUR_GOOGLE_API_KEY'
google_api_url = 'https://www.googleapis.com/customsearch/v1'  


wikipedia_api_key = 'YOUR_WIKIPEDIA_API_KEY'
wikipedia_api_url = 'https://en.wikipedia.org/w/api.php' 

# Create the DARKHAT
DARKHAT = Chat(pairs, reflections)

def search_google(query):
    params = {'key': google_api_key, 'q': query}
    response = requests.get(google_api_url, params=params)
    data = response.json()
    # Process the data as needed
    return data
# Interaction loop
while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        print("DARKHAT: Goodbye!")
        break

    if 'wikipedia' in user_input.lower():
        # Wikipedia API search
        wikipedia_results = search_wikipedia(user_input)
        print("Wikipedia Results:", wikipedia_results)
    else:
        response = DARKHAT.respond(user_input)
        print("DARKHAT:", response)
