// Получение CSRF-токена из мета-тега
function getCSRFToken() {
    const token = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
    return token;
}

async function makeRequest(url, method = "GET") {
    const csrfToken = getCSRFToken(); // Получение CSRF-токена

    try {
        let response = await fetch(url, {
            method: method,
            headers: {
                'X-CSRFToken': csrfToken,
                'Content-Type': 'application/json'
            }
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
    let action = button.getAttribute('data-action');

    let method = (action === 'add') ? 'POST' : 'DELETE';

    makeRequest(url, method)
        .then(data => {
            if (data.success) {
                if (action === 'add') {
                    button.textContent = 'Удалить из избранного';
                    button.setAttribute('data-action', 'remove');
                } else {
                    button.textContent = 'Добавить в избранное';
                    button.setAttribute('data-action', 'add');
                }
            } else {
                console.log('Не удалось обновить состояние избранного:', data.error);
            }
        })
        .catch(error => console.log('Ошибка при обработке запроса:', error));
}

function onLoad() {
    let favoriteButtons = document.querySelectorAll('.favorite-button');
    for (let button of favoriteButtons) {
        button.addEventListener('click', handleFavoriteClick);
    }
}

window.addEventListener('load', onLoad);
