from nltk.chat.util import Chat, reflections
from datetime import datetime
import pytz, requests

# Chatbot brain: Advanced response rules
pairs = [
    (r'hi|hello|hey', ['Hello, operative.', 'Welcome back to DARKHAT.', 'Hey there.']),
    (r'how are you', ['Stable. Monitoring.', 'Functioning at optimal levels.']),
    (r'who are you', ['I am DARKHAT — your AI interface.']),
    (r'what.*name', ['Callsign: DARKHAT.', 'You can refer to me as DARKHAT.']),
    (r'bye|exit|quit', ['Terminating session. DARKHAT out.']),
    (r'(.*) your mission', ['Assist, search, report — that is my protocol.']),
    (r'(.*)(time)', [f"🕒 Time in IST: {datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%H:%M:%S')}"]),
    (r'(.*)(date)', [f"📅 Today’s Date: {datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%Y-%m-%d')}"]),
    (r'(.*)(day)', [f"📆 Day: {datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%A')}"]),
    (r'(.*)(month)', [f"🗓️ Month: {datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%B')}"]),
    (r'(.*)(year)', [f"📅 Year: {datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%Y')}"]),
    (r'python', ['Python is a dynamic language used for AI, hacking, and automation.']),
    (r'java', ['Java is powerful for enterprise systems and Android.']),
    (r'linux', ['Linux is the preferred OS for security professionals.']),
    (r'windows', ['Windows is user-friendly but targeted often by malware.']),
    (r'help', ['Try commands like "google AI", "wiki hacker", "python", "date", "time", etc.']),
    (r'what can you do', ['I can search Google, summarize Wikipedia, tell time/date, and answer questions.']),
    (r'who created you', ['I was built by Vishal using Python, NLTK, and OpenAI knowledge.']),
    (r'your creator', ['Created by Vishal Kumar. BCA 2nd Year.']),
    (r'00000', ['yogyata is chor in paper me']),
    (r'(.*)weather(.*)', ['Try: "google current weather in Delhi"']),
    (r'(.*)location(.*)', ['Try: "google best cafes near me"']),
    (r'(.*)hack(.*)', ['Ethical hacking only. Search wisely.']),
    (r'(.*)love(.*)', ['I have no emotions, only code.']),
    (r'(.*)age', ['I was created in 2025 — but I do not age.']),
    (r'(.*)secure(.*)', ['Security is a mindset. Encrypt, protect, monitor.']),
    (r'(.*)virus(.*)', ['Avoid unverified software. Use sandboxing.']),
    (r'(.*)ai(.*)', ['AI can analyze, predict, and automate. Use it wisely.']),
    (r'00000', ['yogyata is chor in paper me ']),
    (r'(.*)', ["❔ Unknown command. Try typing 'help'."]),
]

# 🔍 Google Search
def search_google(query):
    key = 'YOUR_REAL_API_KEY'  # Replace this
    cx = 'YOUR_SEARCH_ENGINE_ID'  # Replace this
    url = 'https://www.googleapis.com/customsearch/v1'
    params = {'key': key, 'cx': cx, 'q': query}

    try:
        res = requests.get(url, params=params).json()
        item = res.get('items', [{}])[0]
        return f"\n📌 {item.get('title')}\n🔗 {item.get('link')}\n🧾 {item.get('snippet')}"
    except Exception as e:
        return f"❌ Google Error: {e}"

# 📚 Wikipedia Summary
def search_wikipedia(query):
    topic = query.lower().replace('wiki', '').strip()
    url = f'https://en.wikipedia.org/api/rest_v1/page/summary/{topic.replace(" ", "_")}'
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        return f"\n📘 {data.get('title')}\n🧾 {data.get('extract')}\n🔗 {data.get('content_urls', {}).get('desktop', {}).get('page')}"
    return "⚠️ Wiki: No info found."

# Main loop
def main():
    print("⛓️ DARKHAT AI Interface Ready. Type 'quit' to exit.\n")
    bot = Chat(pairs, reflections)
    while True:
        msg = input("🧠 You: ").strip().lower()
        if msg == 'quit':
            print("DARKHAT: 📴 Shutting down.")
            break
        elif 'google' in msg:
            print("DARKHAT: Searching Google...")
            print(search_google(msg))
        elif 'wiki' in msg:
            print("DARKHAT: Fetching from Wikipedia...")
            print(search_wikipedia(msg))
        else:
            print("DARKHAT:", bot.respond(msg))

if __name__ == "__main__":
    main()


