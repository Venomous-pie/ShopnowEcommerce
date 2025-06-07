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
        const response = await fetch('http://localhost:5173/api/login/', {
            method: 'POST',
            headers: {'Content-type': 'application/json'},
            body: JSON.stringify({
                username: username.value,
                password: password.value,
            }),
        })

        const data = await response.json()

        if (response.ok) {
            localStorage.setItem('access', data.access)
            localStorage.setItem('refresh', data.refresh)
            localStorage.setItem('isAuthenticated', 'true')

            window.location.href = '/'
        } else {
            console.error(data)
            alert('Invalid Credentials.')
        }
    }
</script>
