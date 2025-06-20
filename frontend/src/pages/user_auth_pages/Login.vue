<template>
  <form @submit.prevent="submitLogin">
    <input v-model="username" type="text" placeholder="Enter your username" required />
    <input v-model="password" type="password" placeholder="Enter your password" required />
    <div id="recaptcha-container"></div>
    <button :disabled="submitting" type="submit">Login</button>
  </form>
</template>

<script setup>
import { ref } from 'vue'

const username = ref('')
const password = ref('')
const submitting = ref(false)
let recaptchaId = null

const interval = setInterval(() => {
  if (window.grecaptcha?.render) {
    recaptchaId = grecaptcha.render('recaptcha-container', {
      sitekey: '6LdCYGMrAAAAAPWA54wtlKIZfP4WV9pPgOkk8wzb'
    })
    clearInterval(interval)
  }
}, 100)
  
async function submitLogin() {
  submitting.value = true

  const captchaToken = grecaptcha.getResponse(recaptchaId)
  if (!captchaToken) {
    alert('Please complete the CAPTCHA.')
    submitting.value = false
    return
  }

  const res = await fetch('/api/login/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      username_email: username.value,
      password: password.value,
      captcha: captchaToken
    })
  })

  const data = await res.json()

  if (res.ok) {
    localStorage.setItem('access', data.access)
    localStorage.setItem('refresh', data.refresh)
    localStorage.setItem('isAuthenticated', 'true')
    window.location.href = '/'
  } else {
    grecaptcha.reset(recaptchaId)
    alert(data.captcha?.[0] || data.username_email?.[0] || 'Login failed.')
  }

  submitting.value = false
}
</script>
