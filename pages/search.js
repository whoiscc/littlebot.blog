const searchInput = document.querySelector('#search-input');

searchInput.addEventListener('keypress', async (event) => {
    const query = searchInput.value.trim();
    if (event.key === 'Enter') {
        event.preventDefault();
        if (query) {
            searchInput.value = '';
            searchInput.classList.remove('is-typing');
            searchInput.blur();

            document.querySelector('#search-title').innerHTML = `<h2>${query}</h2>`;
            const searchResults = document.querySelector('#search-results');
            searchResults.innerHTML = '<p class="search-loading">烧烤中</p>';

            const url = new URL('https://84b379a3-48bb-49d5-83e5-f96851f774a8.search.ai.cloudflare.com/chat/completions');
            const response = await fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    "messages": [
                        {
                            "role": "user",
                            "content": query
                        }
                    ],
                    "stream": true,
                }),
            });

            let answer = '';
            let buffer = '';
            const decoder = new TextDecoder();

            for await (const chunk of response.body) {
                buffer += decoder.decode(chunk, { stream: true });
                const events = buffer.split('\n\n');
                buffer = events.pop() || '';

                for (const eventBlock of events) {
                    const lines = eventBlock.split('\n');
                    const dataLines = lines
                        .filter((line) => line.startsWith('data:'))
                        .map((line) => line.slice(5).trim());

                    for (const data of dataLines) {
                        if (data === '[DONE]') {
                            continue;
                        }

                        try {
                            const payload = JSON.parse(data);
                            const delta = payload?.choices?.[0]?.delta?.content || '';
                            if (delta) {
                                answer += delta;
                                searchResults.innerHTML = DOMPurify.sanitize(marked.parse(answer));
                            }
                        } catch (err) {
                            console.log('Failed to parse SSE data', err);
                        }
                    }
                }
            }

            // Flush any final buffered text after stream completion.
            buffer += decoder.decode();
        }
    }
});

searchInput.addEventListener('input', (event) => {
    const query = searchInput.value.trim();
    if (query) {
        searchInput.classList.add('is-typing');
    } else {
        searchInput.classList.remove('is-typing');
    }
});