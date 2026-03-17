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
            searchResults.innerHTML = '<p class="search-loading">正在加载响应</p>';

            const url = new URL('https://search.littlebot.blog/');
            // let url = new URL('http://localhost:8787/');
            url.searchParams.append('q', query);
            url.searchParams.append('stream', 'true');
            // switch to @microsoft/fetch-event-source if necessary
            const eventSource = new EventSource(url);
            let answer = "";
            eventSource.onmessage = (event) => {
                // console.log(event);
                answer += JSON.parse(event.data).response;
                // console.log(answer);
                searchResults.innerHTML = DOMPurify.sanitize(marked.parse(answer));
            };
            eventSource.onerror = (err) => {
                console.log(err);
                eventSource.close();
            };
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