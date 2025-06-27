<template>
  <form @submit.prevent="submitLogin">
    <input v-model="username" type="text" placeholder="Username" required />
    <input v-model="password" type="password" placeholder="Password" required />

    <div v-if="showCaptcha">
      <div class="g-recaptcha" ref="captchaContainer"></div>
    </div>

    <button :disabled="submitting" type="submit">Login</button>
  </form>
</template>

<script setup>
  import { ref, onMounted, nextTick } from 'vue'

  const username = ref('')
  const password = ref('')
  const captchaToken = ref('')
  const showCaptcha = ref(false)
  const submitting = ref(false)
  const captchaContainer = ref(null)

  // Global callback from Google script
  window.onCaptchaVerified = (token) => {
    captchaToken.value = token
  }

  onMounted(() => {
    if (localStorage.getItem('require_captcha') === 'true') {
      showCaptcha.value = true

      const waitForGrecaptcha = () => {
        if (window.grecaptcha && window.grecaptcha.render) {
          window.onRecaptchaLoadCallback()
        } else {
          setTimeout(waitForGrecaptcha, 200)
        }
      }

      waitForGrecaptcha()
    }
  })

  async function submitLogin() {
    let payload = {
      username_email: username.value,
      password: password.value,
    }

    if (showCaptcha.value) {
      if (!captchaToken.value) {
        alert('Please complete the CAPTCHA.')
        return
      }
      payload['captcha'] = captchaToken.value
    }

    submitting.value = true

    const res = await fetch('/api/login/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCookie('csrftoken')
      },
      body: JSON.stringify(payload)
    })

    const data = await res.json()
    submitting.value = false

    if (res.ok) {
      alert('Welcome!!!')
      localStorage.setItem('access', data.access)
      localStorage.setItem('refresh', data.refresh)
      localStorage.setItem('isAuthenticated', true)
      localStorage.removeItem('require_captcha')

      // This redirect user to homepage
      window.location.href = '/'
    } else {
      if (data.require_captcha === true) {

        localStorage.setItem('require_captcha', 'true')
        showCaptcha.value = true
        renderCaptcha();

      } else if (data.captcha_error) {
        alert(data.captcha_error[0])
      } else if (data.username_email) {
        alert(data.username_email[0])
      } else {
        alert('Login failed.')
      }
    }

    if (showCaptcha.value && window.grecaptcha) {
      window.grecaptcha.reset()
    }
  }

  function renderCaptcha() {
    nextTick(() => {
      if (window.grecaptcha && captchaContainer.value) {
        window.grecaptcha.render(captchaContainer.value, {
          sitekey: '6LdCYGMrAAAAAPWA54wtlKIZfP4WV9pPgOkk8wzb',
          callback: onCaptchaVerified
        })
      }
    })
    alert('To many failed login attempt please verify your not a bot.')
  }

  function getCookie(name) {
    const value = `; ${document.cookie}`
    const parts = value.split(`; ${name}=`)
    if (parts.length === 2) return parts.pop().split(';').shift()
  }

</script>
