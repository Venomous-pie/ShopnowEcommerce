<template>
    <form @submit.prevent="submitRegister">
        <input v-model="username" type="text" placeholder="Enter your username" required>
        <input v-model="email" type="email" placeholder="Enter your email" required>
        <input v-model="password" type="password" placeholder="Enter your password" required>
        <input v-model="confirm_password" type="password" placeholder="Confirm your password" required>
        <button type="submit">Register</button>
    </form>
</template>

<script setup>

    import { ref } from 'vue'
    import { useRouter } from 'vue-router'

    const router = useRouter()
    const username = ref('')
    const email = ref('')
    const password = ref('')
    const confirm_password = ref('')

    async function submitRegister() {
        const response = await fetch('http://localhost:5173/api/register/', {
            method: 'POST',
            headers: {'Content-type': 'application/json'},
            body: JSON.stringify({
                username: username.value,
                email: email.value,
                password: password.value,
                confirm_password: confirm_password.value,
            }),
        })

        const data = await response.json()

        if (response.ok) {
            router.push('/login')
        } else {
            console.error(data)
            // alert('')
        }
    }
</script>