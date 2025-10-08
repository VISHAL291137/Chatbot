export async function searchWithAI(query) {
    try {
        const response = await fetch(`https://api.duckduckgo.com/?q=${encodeURIComponent(query)}&format=json&no_redirect=1`);
        const data = await response.json();

        if (data.Abstract) {
            return {
                success: true,
                title: data.Heading,
                snippet: data.Abstract,
                url: data.AbstractURL
            };
        }

        return await searchPerplexity(query);
    } catch (error) {
        return await searchPerplexity(query);
    }
}

async function searchPerplexity(query) {
    try {
        const response = await fetch('https://www.perplexity.ai/search', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ query })
        });

        if (response.ok) {
            const data = await response.json();
            return {
                success: true,
                answer: data.answer || 'Search completed'
            };
        }
    } catch (error) {
        console.log('Perplexity search unavailable');
    }

    return fallbackSearch(query);
}

async function fallbackSearch(query) {
    const searchUrl = `https://html.duckduckgo.com/html/?q=${encodeURIComponent(query)}`;

    return {
        success: true,
        answer: `🔍 I found results for "${query}". Here are some helpful resources:`,
        searchUrl: searchUrl,
        googleUrl: `https://www.google.com/search?q=${encodeURIComponent(query)}`,
        message: 'Click the links below to see search results'
    };
}

export async function getAIResponse(query) {
    const lowerQuery = query.toLowerCase();

    if (lowerQuery.includes('what is') ||
        lowerQuery.includes('tell me about') ||
        lowerQuery.includes('explain') ||
        lowerQuery.includes('how to') ||
        lowerQuery.includes('why')) {

        const result = await searchWithAI(query);

        if (result.success && result.snippet) {
            return `📌 <strong>${result.title}</strong><br><br>${result.snippet}<br><br>🔗 <a href="${result.url}" target="_blank">Learn more</a>`;
        }

        if (result.answer) {
            return result.answer;
        }

        if (result.searchUrl) {
            return `${result.answer}<br><br>
                🔍 <a href="${result.searchUrl}" target="_blank">DuckDuckGo Search</a><br>
                🔍 <a href="${result.googleUrl}" target="_blank">Google Search</a>`;
        }
    }

    return null;
}
