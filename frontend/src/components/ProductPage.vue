<template>
  <div v-if="loading" class="p-8 text-lg">Loading product...</div>
  <div v-else-if="product" class="max-w-xl mx-auto p-8 bg-white rounded-lg shadow">
    <h2 class="text-3xl font-bold mb-4">{{ product.name }}</h2>
    <p class="text-xl text-blue-700 mb-2">${{ product.price }}</p>
    <p class="text-slate-700">{{ product.description }}</p>
  </div>
  <div v-else class="p-8 text-red-600">Product not found.</div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'

const route = useRoute()
const product = ref(null)
const loading = ref(true)

onMounted(async () => {
  try {
    const res = await axios.get(`/api/products/${route.params.id}/`)
    product.value = res.data
  } catch {
    product.value = null
  } finally {
    loading.value = false
  }
})
</script>
