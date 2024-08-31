function getCSRFToken() {
    const token = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
    return token;
}

async function makeRequest(url, method = "POST") {
    const csrfToken = getCSRFToken();

    try {
        let response = await fetch(url, {
            method: method,
            headers: {
                'X-CSRFToken': csrfToken,
                'Content-Type': 'application/json'
            },
            credentials: 'include'
        });
        if (!response.ok) {
            let errorText = await response.text();
            throw new Error(errorText);
        }
        return await response.json();
    } catch (error) {
        console.log('Ошибка:', error);
        throw error;
    }
}

function handleFavoriteClick(event) {
    event.preventDefault();
    let button = event.target;
    let url = button.getAttribute('data-url');

    makeRequest(url).then(data => {
        if (data.success) {
            button.textContent = data.is_favorite ? 'Удалить из избранного' : 'Добавить в избранное';
        } else {
            console.log('Не удалось обновить состояние избранного:', data.error);
        }
    }).catch(error => console.log('Ошибка при обработке запроса:', error));
}

function onLoad() {
    let favoriteButtons = document.querySelectorAll('.favorite-button');
    for (let button of favoriteButtons) {
        button.addEventListener('click', handleFavoriteClick);
    }
}

window.addEventListener('load', onLoad);
