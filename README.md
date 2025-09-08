# DARKHAT 🤖💻 – Hacker-Style Python Chatbot

DARKHAT is a hacker-themed AI chatbot built using Python, NLTK, Google Custom Search API, and Wikipedia API. Designed to mimic a terminal-based assistant, DARKHAT can answer custom questions, search the web, fetch Wikipedia summaries, and display system time/date – all in a stylish terminal interface.

---

## 💡 Features

- 🧠 NLTK-based AI conversation
- 🔍 Google search integration (via API)
- 📘 Wikipedia summary search
- 📅 Indian timezone date & time functions
- 🛡️ Hacker/Dark UI style responses
- 🎯 Expandable custom logic for topics like Python, Linux, Java, etc.

---

## 🔧 Requirements

- Python 3.8+
- Required packages:
  ```bash
  pip install nltk pytz requests
🚀 Setup Instructions
Clone or download this repo to your local system.

Create a virtual environment (optional but recommended):

bash
Copy
Edit
python -m venv venv
venv\Scripts\activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Configure your API keys:

Go to Google Cloud Console → Create API Key

Create a search engine at Programmable Search Engine

Replace values in darkhat_ai.py:

python
Copy
Edit
key = 'YOUR_GOOGLE_API_KEY'
cx = 'YOUR_SEARCH_ENGINE_ID'
🧪 Usage
bash
Copy
Edit
python darkhat_ai.py
Try:

shell
Copy
Edit
> hi
> what is your name
> google python advantages
> wiki hacker
> time
> date
> quit
🔐 Security Note
Do not share your Google API key or client secrets publicly. Consider storing them in a .env file and using python-dotenv.

👨‍💻 Developer
Vishal Kumar
BCA 2nd Year
📞 9608339846

🧠 Credits
Python NLTK

Google Programmable Search

Wikipedia REST API

📸 Screenshot
kotlin
Copy
Edit
⛓️ DARKHAT AI Interface Ready. Type 'quit' to exit.
