<template>
    <form @submit.prevent="submitLogin">
        <input v-model="username" type="text" placeholder="Enter your username" required>
        <input v-model="password" type="password" placeholder="Enter your password" required>
        <button type="submit">Login</button>
    </form>
</template>

<script setup>

    import { ref } from 'vue'
    import { useRouter } from 'vue-router'
    
    const router = useRouter()
    const username = ref('')
    const password = ref('')

    async function submitLogin() {
        try {
            const response = await fetch('http://localhost:5173/api/login/', {
                method: 'POST',
                headers: { 'Content-type': 'application/json' },
                body: JSON.stringify({
                    username_email: username.value,
                    password: password.value,
                }),
            });

            let data;
            try {
                data = await response.json();
            } catch (err) {
                console.error('Error parsing JSON:', err);
                alert('Unexpected server response. Please try again later.');
                return;
            }

            if (response.ok) {
                localStorage.setItem('access', data.access);
                localStorage.setItem('refresh', data.refresh);
                localStorage.setItem('isAuthenticated', 'true');
                window.location.href = '/';
            } else {
                if (response.status === 403) {
                    alert('You’ve made too many login attempts. Please wait a few minutes before trying again.');
                } else if (response.status === 401) {
                    alert(data?.error || 'Invalid credentials.');
                } else {
                    alert(data?.error || data?.detail || 'Login failed. Please try again.');
                }
            }

        } catch (err) {
            console.error('Network or server error:', err);
            alert('Cannot connect to the server. Please check your internet or try again later.');
        }
    }

</script>
