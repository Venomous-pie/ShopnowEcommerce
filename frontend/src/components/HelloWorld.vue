<template>
  <div>
    <h2>Message from Django:</h2>
    <p v-if="loading">Loading…</p>
    <p v-else>{{ message }}</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const message = ref('')
const loading = ref(true)

onMounted(async () => {
  try {
    // Because of Vite proxy, "/api/hello/" → "http://localhost:8000/api/hello/"
    const res = await axios.get('/api/hello/')
    message.value = res.data.message
  } catch (err) {
    message.value = 'Error fetching from Django'
    console.error(err)
  } finally {
    loading.value = false
  }
})
</script>
