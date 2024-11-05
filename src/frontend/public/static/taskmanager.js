async function approve() {
    var Kurl = window.location.href;
    const parts = Kurl.split('/');
    const id = parts[parts.length - 1];
    const response = await fetch('/taskmanager/approve', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ id })
    });
    window.location = "/tasks";
}

async function reject() {
    var Kurl = window.location.href;
    const parts = Kurl.split('/');
    const id = parts[parts.length - 1];
    const response = await fetch('/taskmanager/reject', { // исправлено 'rejetc' на 'reject'
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ id })
    });
    window.location = "/tasks";
}

// Исправлено добавление слушателей событий
const rejectButtons = document.getElementsByClassName('tasks-button');
for (let button of rejectButtons) {
    button.addEventListener('click', reject);
}

const approveButtons = document.getElementsByClassName('approve-btn');
for (let button of approveButtons) {
    button.addEventListener('click', approve);
}
