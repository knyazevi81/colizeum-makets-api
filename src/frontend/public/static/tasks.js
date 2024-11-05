async function fetchDataAndDisplay() {
    try {
        const response = await fetch('/taskmanager/current_tasks', {
            method: 'POST'
        });
        if (!response.ok) {
            throw new Error('Сеть ответила с ошибкой');
        }
        const data = await response.json();
        const tableBody = document.querySelector('#data-table tbody');
        data.forEach(item => {
            const row = document.createElement('tr');
            
            const taskIdCell = document.createElement('td');
            taskIdCell.textContent = item.task_id;
            row.appendChild(taskIdCell);
            
            const clubIdCell = document.createElement('td');
            clubIdCell.textContent = item.club_id;
            row.appendChild(clubIdCell);

            const nicknameCell = document.createElement('td');
            nicknameCell.textContent = item.nickname;
            row.appendChild(nicknameCell);

            const taskNameCell = document.createElement('td');
            taskNameCell.textContent = item.task_name;
            row.appendChild(taskNameCell);

            const descriptCell = document.createElement('button');
            descriptCell.textContent = "Подробнее";
            descriptCell.addEventListener('click', function () {
                window.location = "/tasks/${task_id}";
            });
            row.appendChild(descriptCell);

            tableBody.appendChild(row);
        });
    } catch (error) {
        console.error('Ошибка при получении данных:', error);
    }
}

// Function to send a POST request for a given action
async function handleAction(id, endpoint) {
    try {
        const response = await fetch(endpoint, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ id })
        });

        if (!response.ok) {
            throw new Error('Ошибка при выполнении действия');
        }

        // Optionally, update the UI or notify the user
        console.log(`Действие для пользователя с id ${id} успешно выполнено`);
    } catch (error) {
        console.error('Ошибка при выполнении действия:', error);
    }
}


fetchDataAndDisplay();
