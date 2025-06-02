<template>
  <div class="max-w-md mx-auto mt-12 p-6 bg-softblue-50 rounded-lg shadow-lg">
    <h2 class="text-2xl font-semibold text-softblue-700 mb-4 hover:text-black">
      Message from Django:
    </h2>

    <p
      v-if="loading"
      class="flex items-center text-lg text-softblue-500"
    >
      <span class="w-4 h-4 mr-2 border-2 border-softblue-500 border-t-transparent rounded-full animate-spin"></span>
      Loading…
    </p>

    <p
      v-else
      class="text-xl text-softblue-900 mt-2"
    >
      {{ message }}
    </p>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const message = ref('')
const loading = ref(true)

onMounted(async () => {
  try {
    // With Vite proxy, "/api/hello/" → "http://localhost:8000/api/hello/"
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

<style scoped>
/* No extra CSS needed—everything is Uno utilities */
</style>
