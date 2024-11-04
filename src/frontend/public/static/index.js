export async function send(event) {
    event.preventDefault(); // Отменяем стандартное поведение формы

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    const response = await fetch("/users/login",{
        method: "POST",
        headers: { "Accept": "application/json", "Content-Type": "application/json" },
        body: JSON.stringify({ 
            login: username,
            password: password
        })
    });

    if (response.ok) {
        window.location.replace('/dashboard');
    }
}

window.send = send;