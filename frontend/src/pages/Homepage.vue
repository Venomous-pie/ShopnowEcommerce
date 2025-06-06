<script setup>
import { ref, onMounted } from 'vue'

const products = ref([])

onMounted(async () => {
  const response = await fetch('/products.json')
  products.value = await response.json()
})
</script>

<template>
  <div class="max-w-7xl mx-auto px-4 sm:px-8 lg:px-16">
    <h2>Product List</h2>
    <div v-for="product in products" :key="product.sku" class="product-card">
      <img :src="product.image" :alt="product.name" width="200" />
      <h3>{{ product.name }}</h3>
      <p>{{ product.short_description }}</p>
      <p>₱{{ product.price }}</p>
      <p>Stock: {{ product.stock_status }}</p>
      <p>Category: {{ product.category }}</p>
      <!-- Add more fields as needed -->
    </div>
  </div>
</template>
