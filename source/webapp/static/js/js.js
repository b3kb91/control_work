async function makeRequest(url, method = "GET") {
    let response = await fetch(url, { method: method });
    if (response.ok) {
        return await response.json();
    } else {
        let error = new Error(await response.text());
        console.log(error);
        throw error;
    }
}

async function toggleFavorite(button, action) {
    let url = button.getAttribute('data-url');
    let method = action === 'add' ? 'GET' : 'GET';

    try {
        let data = await makeRequest(url, method);
        if (data.favorite) {
            button.textContent = 'Удалить из избранного';
            button.setAttribute('data-action', 'remove');
        } else {
            button.textContent = 'Добавить в избранное';
            button.setAttribute('data-action', 'add');
        }
    } catch (error) {
        console.error('Toggle favorite failed', error);
    }
}

async function onClick(event) {
    event.preventDefault();
    let button = event.target;
    let action = button.getAttribute('data-action');
    await toggleFavorite(button, action);
}

function onLoad() {
    let favoriteButtons = document.querySelectorAll('[data-js="favorite-button"]');
    favoriteButtons.forEach(button => {
        let isFavorite = button.getAttribute('data-favorite') === 'true';
        button.textContent = isFavorite ? 'Удалить из избранного' : 'Добавить в избранное';
        button.setAttribute('data-action', isFavorite ? 'remove' : 'add');
        button.addEventListener('click', onClick);
    });
}

window.addEventListener('load', onLoad);
