
const chatMessages = document.getElementById('chatMessages');
const userInput = document.getElementById('userInput');
const sendButton = document.getElementById('sendButton');
const currentTimeEl = document.getElementById('currentTime');

function updateTime() {
    const now = new Date();
    const options = {
        timeZone: 'Asia/Kolkata',
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit'
    };
    currentTimeEl.textContent = now.toLocaleTimeString('en-IN', options);
}

updateTime();
setInterval(updateTime, 1000);

function addMessage(text, isUser = false) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${isUser ? 'user-message' : 'bot-message'}`;

    const contentDiv = document.createElement('div');
    contentDiv.className = 'message-content';

    if (isUser) {
        contentDiv.innerHTML = `<strong>You:</strong> ${text}`;
    } else {
        contentDiv.innerHTML = `<strong>DARKHAT:</strong> ${text}`;
    }

    const timeDiv = document.createElement('div');
    timeDiv.className = 'message-time';
    const now = new Date();
    timeDiv.textContent = now.toLocaleTimeString('en-IN', {
        timeZone: 'Asia/Kolkata',
        hour: '2-digit',
        minute: '2-digit'
    });

    messageDiv.appendChild(contentDiv);
    messageDiv.appendChild(timeDiv);
    chatMessages.appendChild(messageDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

async function searchWikipedia(query) {
    const topic = query.toLowerCase().replace('wiki', '').trim();
    const url = `https://en.wikipedia.org/api/rest_v1/page/summary/${topic.replace(/ /g, '_')}`;

    try {
        const response = await fetch(url);
        if (response.ok) {
            const data = await response.json();
            return `📘 <strong>${data.title}</strong><br><br>${data.extract}<br><br>🔗 <a href="${data.content_urls.desktop.page}" target="_blank">Read more</a>`;
        } else {
            return "⚠️ No Wikipedia article found for that topic.";
        }
    } catch (error) {
        return "❌ Error fetching Wikipedia data.";
    }
}

function getResponse(input) {
    const lowerInput = input.toLowerCase().trim();

    const now = new Date();
    const istOptions = { timeZone: 'Asia/Kolkata' };

    if (lowerInput.match(/^(hi|hello|hey)$/)) {
        return 'Hello, operative. DARKHAT interface ready.';
    }
    if (lowerInput.includes('how are you')) {
        return 'Stable. Monitoring. All systems operational.';
    }
    if (lowerInput.includes('who are you')) {
        return 'I am DARKHAT — your AI interface for intelligence gathering and analysis.';
    }
    if (lowerInput.includes('name')) {
        return 'Callsign: DARKHAT. Advanced Intelligence System.';
    }
    if (lowerInput.includes('time')) {
        return `🕒 Current IST Time: ${now.toLocaleTimeString('en-IN', {...istOptions, hour: '2-digit', minute: '2-digit', second: '2-digit'})}`;
    }
    if (lowerInput.includes('date')) {
        return `📅 Today's Date: ${now.toLocaleDateString('en-IN', {...istOptions, year: 'numeric', month: 'long', day: 'numeric'})}`;
    }
    if (lowerInput.includes('day')) {
        return `📆 Day: ${now.toLocaleDateString('en-IN', {...istOptions, weekday: 'long'})}`;
    }
    if (lowerInput.includes('month')) {
        return `🗓️ Month: ${now.toLocaleDateString('en-IN', {...istOptions, month: 'long'})}`;
    }
    if (lowerInput.includes('year')) {
        return `📅 Year: ${now.toLocaleDateString('en-IN', {...istOptions, year: 'numeric'})}`;
    }
    if (lowerInput.includes('python')) {
        return 'Python is a versatile programming language used for AI, automation, web development, and data analysis. Popular for its simplicity and powerful libraries.';
    }
    if (lowerInput.includes('java')) {
        return 'Java is a robust, object-oriented language used for enterprise applications, Android development, and large-scale systems.';
    }
    if (lowerInput.includes('linux')) {
        return 'Linux is the preferred operating system for developers and security professionals. Open-source, secure, and highly customizable.';
    }
    if (lowerInput.includes('windows')) {
        return 'Windows is a user-friendly OS with wide software support, commonly used in business and personal computing.';
    }
    if (lowerInput.includes('help')) {
        return `📋 <strong>Available Commands:</strong><br>
        • "wiki [topic]" - Search Wikipedia<br>
        • "time/date/day/month/year" - Get current info<br>
        • "python/java/linux" - Learn about tech<br>
        • "who are you" - About DARKHAT<br>
        • "help" - Show this menu`;
    }
    if (lowerInput.includes('what can you do')) {
        return 'I can search Wikipedia, provide date/time info, answer tech questions, and assist with information gathering.';
    }
    if (lowerInput.includes('creator') || lowerInput.includes('created you')) {
        return 'Created by Vishal Kumar, BCA 2nd Year. Student ID: 2247110 | Contact: 9608339846';
    }
    if (lowerInput.includes('2247110')) {
        return 'ID: Vishal Kumar | BCA Semester 3 | 📞 9608339846';
    }
    if (lowerInput.includes('mission')) {
        return 'Assist, search, report — that is my protocol. Intelligence gathering and analysis.';
    }
    if (lowerInput.includes('secure') || lowerInput.includes('security')) {
        return 'Security is a mindset. Always encrypt sensitive data, use strong authentication, and monitor for threats.';
    }
    if (lowerInput.includes('ai')) {
        return 'AI can analyze patterns, predict outcomes, and automate complex tasks. Use it responsibly and ethically.';
    }

    return "❔ Command not recognized. Type 'help' for available commands.";
}

async function handleSend() {
    const message = userInput.value.trim();
    if (!message) return;

    addMessage(message, true);
    userInput.value = '';

    const lowerMessage = message.toLowerCase();

    if (lowerMessage.includes('wiki')) {
        addMessage('Searching Wikipedia...', false);
        const result = await searchWikipedia(message);
        setTimeout(() => {
            const messages = chatMessages.getElementsByClassName('message');
            messages[messages.length - 1].remove();
            addMessage(result, false);
        }, 500);
    } else {
        const response = getResponse(message);
        setTimeout(() => addMessage(response, false), 300);
    }
}

sendButton.addEventListener('click', handleSend);
userInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        handleSend();
    }
});

userInput.focus();
