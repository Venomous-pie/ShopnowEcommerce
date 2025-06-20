<template>
  <form @submit.prevent="submitRegister">
    <input v-model="username" type="text" placeholder="Enter your username" required />
    <input v-model="email" type="email" placeholder="Enter your email" required />
    <input v-model="password" type="password" placeholder="Enter your password" required />
    <input v-model="confirm_password" type="password" placeholder="Confirm your password" required />
    <div id="recaptcha-container"></div>
    <button :disabled="submitting" type="submit">Register</button>
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
const submitting = ref(false)
let recaptchaId = null

// Mount reCAPTCHA as soon as grecaptcha is ready
const interval = setInterval(() => {
  if (window.grecaptcha?.render) {
    recaptchaId = grecaptcha.render('recaptcha-container', {
      sitekey: '6LdCYGMrAAAAAPWA54wtlKIZfP4WV9pPgOkk8wzb'
    })
    clearInterval(interval)
  }
}, 100)

async function submitRegister() {
  submitting.value = true

  const captchaToken = grecaptcha.getResponse(recaptchaId)
  if (!captchaToken) {
    alert('Please complete the CAPTCHA.')
    submitting.value = false
    return
  }

    const res = await fetch('http://localhost:8000/api/register/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
        username: username.value,
        email: email.value,
        password: password.value,
        confirm_password: confirm_password.value,
        captcha: captchaToken
    })
    })

  let data = null
    try {
    data = await res.json()
    } catch {
    console.error('Non-JSON response (probably HTML error page)')
    }

    if (res.ok) {
    router.push('/login')
    } else {
    grecaptcha.reset(recaptchaId)
    console.error(data)  // Log full response for debug

    alert(
        data?.captcha?.[0] ||
        data?.username?.[0] ||
        data?.email?.[0] ||
        data?.password?.[0] ||
        data?.confirm_password?.[0] ||
        (typeof data === 'string' ? data : 'Registration failed. Check console.')
    )
    }



  submitting.value = false
}
</script>
