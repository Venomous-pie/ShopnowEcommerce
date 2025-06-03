<script setup>
  import Navbar from './Navbar.vue';
  import Footer from './Footer.vue';
</script>

<template>
  <div>
    <Navbar />
    <main>
      <router-view />
    </main>
    <Footer />
  </div>
</template>
