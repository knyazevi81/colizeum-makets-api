async function fetchDataAndDisplay() {
    try {
        const response = await fetch('/tgusers');
        if (!response.ok) {
            throw new Error('Сеть ответила с ошибкой');
        }
        const data = await response.json();
        const tableBody = document.querySelector('#data-table tbody');
        data.forEach(item => {
            const row = document.createElement('tr');

            // Create and append cells as before
            const clubIdCell = document.createElement('td');
            clubIdCell.textContent = item.club_id;
            row.appendChild(clubIdCell);

            const tgIdCell = document.createElement('td');
            tgIdCell.textContent = item.tg_id;
            row.appendChild(tgIdCell);

            const nicknameCell = document.createElement('td');
            nicknameCell.textContent = item.nickname;
            row.appendChild(nicknameCell);

            const nameCell = document.createElement('td');
            nameCell.textContent = item.name;
            row.appendChild(nameCell);

            const idCell = document.createElement('td');
            idCell.textContent = item.id;
            row.appendChild(idCell);

            // Add the 'approve' button with a click event listener
            const statusCellApprove = document.createElement('button');
            statusCellApprove.textContent = 'одобрить';
            statusCellApprove.style = "background-color: rgb(44, 193, 96);"
            statusCellApprove.addEventListener('click', function () {
                handleAction(item.tg_id, '/tgusers/approve'); // Call the handleAction function with 'approve' endpoint
                window.location = "/telegram"
            });
            row.appendChild(statusCellApprove);

            // Add the 'reject' button with a click event listener
            const statusCellReject = document.createElement('button');
            statusCellReject.textContent = 'отклонить';
            statusCellReject.style = "background-color: rgb(238, 96, 96);"
            statusCellReject.addEventListener('click', function () {
                handleAction(item.tg_id, '/tgusers/reject'); // Call the handleAction function with 'reject' endpoint
                window.location = "/telegram"
            });
            row.appendChild(statusCellReject);

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
