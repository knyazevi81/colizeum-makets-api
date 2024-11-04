async function fetchCurrentUser() {
    try {
        const response = await fetch("/users/me", {
            method: "GET",
            headers: { "Accept": "application/json" },
        });

        if (!response.ok) {
            window.location.replace('/auth');
        }

        const userData = await response.json();
        console.log(userData); // Используйте эту информацию по необходимости
    } catch (error) {
        console.error("Error fetching user:", error);
    }
}


// Вызовите асинхронную функцию для получения текущего пользователя
fetchCurrentUser();