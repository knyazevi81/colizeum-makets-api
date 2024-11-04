async function fetchAdminUser() {
    try {
        const response = await fetch("/users/me");
        if (!response.ok) throw new Error('Сеть ответила с ошибкой');
        const data = await response.json();
        console.log(data.status)
        if (data.status == "admin") {
            const tableBody = document.querySelector('.right');
            const statusCellApprove = document.createElement('button');
            statusCellApprove.textContent = 'employes';
            statusCellApprove.id = "employes-button"
            
            // Uncomment and define handleAction to make this work
            // statusCellApprove.addEventListener('click', function () {
            //     handleAction(item.id, '/tgusers/approve'); 
            // });

            tableBody.appendChild(statusCellApprove);
        }
    } catch (error) {
        console.error('Ошибка:', error);
    }
}

// Make sure to call the function somewhere in your code
fetchAdminUser();