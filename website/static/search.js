const searchInput = document.querySelector('#search-input');

searchInput.addEventListener('keypress', (event) => {
    const query = searchInput.value.trim();
    if (event.key === 'Enter') {
        event.preventDefault();
        if (query) {
            searchInput.value = '';
            searchInput.classList.remove('is-typing');
            searchInput.blur();

            document.querySelector('#search-title').innerHTML = `<h2>${query}</h2>`;
            const searchResults = document.querySelector('#search-results');
            searchResults.innerHTML = '<p style="color: --text-muted">正在加载响应</p>';
            fetch(`https://search.littlebot.blog/?q=${encodeURIComponent(query)}`)
                .then(response => response.json())
                .then(data => {
                    const html = DOMPurify.sanitize(marked.parse(data.response));
                    searchResults.innerHTML = html;
                });
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