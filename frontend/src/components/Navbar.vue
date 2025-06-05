<template>
  <!-- Topbar Navigation -->
  <div class="bg-gray-900 text-white py-1 px-4">
    <div class="container mx-auto text-sm">
      <div class="flex justify-between items-center text-center">
        <div class="flex gap-4 items-center">
          <!-- Desktop Links -->
          <div class="hidden sm:flex gap-4">
            <a href="#" class="hover:text-blue-300">Download App</a>
            <span>|</span>
            <a href="#" class="hover:text-blue-300">Become a Seller</a>
            <span>|</span>
            <a href="#" class="hover:text-blue-300">Customer Support</a>
          </div>
          <!-- Mobile Dropdown -->
          <div class="relative sm:hidden" ref="dropdownRef" v-click-outside="closeMoreDropdownHandler">
            <div @click="toggleMoreDropdown" class="flex items-center cursor-pointer select-none text-xs lg:text-sm">
              <a>More</a>
              <ChevronDown class="ml-1 w-4 h-4 text-white mt-1" />
            </div>
            <!-- Dropdown Menu -->
            <div v-if="moreDropdownOpen"
              class="absolute left-0 mt-2 w-40 bg-white text-gray-900 rounded shadow-lg z-30">
              <a href="#" class="block px-4 py-2 hover:bg-blue-100">Download App</a>
              <a href="#" class="block px-4 py-2 hover:bg-blue-100">Become a Seller</a>
              <a href="#" class="block px-4 py-2 hover:bg-blue-100">Customer Support</a>
              <div class="flex items-center justify-center hover:bg-blue-100 py-2">
                <a href="#" class="block font-bold hover:text-blue-600">Register</a>
                <span class="px-2 text-gray-400">|</span>
                <a href="#" class="block font-bold hover:text-blue-600">Login</a>
              </div>
            </div>
          </div>
        </div>
        <div class="flex items-center gap-4">
          <div class="flex gap-1 items-center text-xs lg:text-sm">
            <Globe class="h-4 w-4" />
            <a class="hover:text-blue-300">EN</a>
          </div>
          <div class="flex items-center justify-center gap-2">
            <a href="#" class="text-sm font-medium hover:text-blue-600">Register</a>
            <span class="text-gray-400">|</span>
            <a href="#" class="text-sm font-medium hover:text-blue-600">Login</a>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Main Navigation -->
  <header class="bg-white shadow px-4 relative">
    <div class="container mx-auto py-3 flex items-center justify-between">
      <!-- Logo -->
      <div class="flex items-center gap-2">
        <img src="/cart.ico" alt="cart icon" class="h-6" />
        <router-link to="/" class="text-blue-600 text-lg font-semibold">ShopNow</router-link>
      </div>

      <!-- Desktop Nav -->
      <nav class="hidden md:flex gap-6 text-gray-700 text-sm">
        <router-link to="/" class="hover:text-blue-600">Home</router-link>
        <router-link to="/products" class="hover:text-blue-600">Products</router-link>
        <router-link to="/contact" class="hover:text-blue-600">Contact</router-link>
      </nav>

      <!-- Right Side Icons -->
      <div class="flex items-center gap-4">
        <!-- Desktop Search -->
        <div class="relative ml-4 hidden sm:block">
          <input type="text" placeholder="Search products..."
            class="w-64 pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent text-sm" />
          <Search class="absolute left-3 top-1/2 transform -translate-y-1/2 h-4 w-4 text-gray-400" />
        </div>

        <!-- Mobile Search Icon -->
        <div @click="toggleMobileSearch" class="md:hidden cursor-pointer p-1 hover:bg-gray-100 rounded">
          <Search class="h-5 w-5 text-gray-600 hover:text-blue-600 transition-colors" />
        </div>

        <!-- User Account Dropdown -->
        <div class="relative" ref="userDropdownRef" v-click-outside="closeUserDropdownHandler">
          <div @click="toggleUserDropdown" class="flex items-center cursor-pointer p-1 hover:bg-gray-100 rounded">
            <UserRound class="h-5 w-5 text-gray-600 pb-1" />
          </div>
          <!-- Dropdown Menu -->
          <div v-if="userDropdownOpen"
            class="absolute transform translate-x-1/2 right-0 mt-2 w-48 bg-white text-gray-900 rounded shadow-lg z-30 border">
            <a href="#" class="block px-4 py-2 hover:bg-blue-100 text-sm">Create Account</a>
            <a href="#" class="block px-4 py-2 hover:bg-blue-100 text-sm">My Orders</a>
            <a href="#" class="block px-4 py-2 hover:bg-blue-100 text-sm">Wishlist</a>
            <hr class="my-1" />
            <div class="px-4 py-2 hover:bg-blue-100">
              <div class="flex items-center justify-center gap-2">
                <a href="#" class="text-sm font-medium hover:text-blue-600">Register</a>
                <span class="text-gray-400">|</span>
                <a href="#" class="text-sm font-medium hover:text-blue-600">Login</a>
              </div>
            </div>
          </div>
        </div>

        <!-- Wishlist Icon -->
        <div class="cursor-pointer p-1 hover:bg-gray-100 rounded">
          <Heart class="h-5 w-5 text-gray-600 hover:text-red-500 transition-colors" />
        </div>

        <!-- Shopping Cart -->
        <div class="cursor-pointer p-1 hover:bg-gray-100 rounded">
          <ShoppingBasket class="h-5 w-5 text-gray-600 hover:text-blue-600 transition-colors" />
        </div>

        <!-- Mobile Burger -->
        <div @click="handleIconClick" class="md:hidden cursor-pointer p-1">
          <component :is="currentIcon" :class="{ 'animate-spin': spinning }"
            class="w-5 h-5 text-gray-600 transition-transform duration-200" />
        </div>
      </div>
    </div>

    <!-- Mobile Search Bar -->
    <transition name="slide">
      <div v-if="mobileSearchOpen" ref="MobileSearchRef"
        class="block absolute top-full left-0 right-0 bg-white px-4 py-4 shadow-lg z-20 border-t sm:hidden">
        <div class="relative box-border">
          <input type="text" placeholder="Search products..."
            class="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent box-border" />
          <Search class="absolute left-3 top-1/2 transform -translate-y-1/2 h-4 w-4 text-gray-400" />
        </div>
      </div>
    </transition>

    <!-- Mobile Menu -->
    <transition name="slide">
      <nav v-if="showMobileNav" ref="MobileNavRef"
        class="absolute top-full left-0 right-0 md:hidden bg-white px-4 pb-4 shadow-lg z-20 border-t">
        <router-link to="/" class="block py-2 text-gray-700 hover:text-blue-600">Home</router-link>
        <router-link to="/products" class="block py-2 text-gray-700 hover:text-blue-600">Products</router-link>
        <router-link to="/contact" class="block py-2 text-gray-700 hover:text-blue-600">Contact</router-link>
      </nav>
    </transition>
  </header>
</template>

<script setup>
import { ref } from 'vue'
import { Globe, ChevronDown, Menu, X, UserRound, ShoppingBasket, Heart, Search } from 'lucide-vue-next'

// Simple dropdown state management
const moreDropdownOpen = ref(false)
const userDropdownOpen = ref(false)
const searchBarOpen = ref(false) // Desktop search
const mobileSearchOpen = ref(false) // Mobile search
const showMobileNav = ref(false)
const spinning = ref(false)
const currentIcon = ref(Menu)

const toggleMoreDropdown = () => {
  moreDropdownOpen.value = !moreDropdownOpen.value
  userDropdownOpen.value = false // Close other dropdown
}

const closeMoreDropdownHandler = () => {
  moreDropdownOpen.value = false
}

const toggleUserDropdown = () => {
  userDropdownOpen.value = !userDropdownOpen.value
  moreDropdownOpen.value = false // Close other dropdown
}

const closeUserDropdownHandler = () => {
  userDropdownOpen.value = false
}

// Desktop search toggle
const toggleSearchbar = () => {
  searchBarOpen.value = !searchBarOpen.value
}

const closeSearchbar = () => {
  searchBarOpen.value = false
}

// Mobile search toggle
const toggleMobileSearch = () => {
  mobileSearchOpen.value = !mobileSearchOpen.value
  // Close mobile nav if open
  if (mobileSearchOpen.value && showMobileNav.value) {
    showMobileNav.value = false
    currentIcon.value = Menu
  }
}

const handleIconClick = () => {
  spinning.value = true
  showMobileNav.value = !showMobileNav.value
  // Close mobile search if open
  if (showMobileNav.value && mobileSearchOpen.value) {
    mobileSearchOpen.value = false
  }
  setTimeout(() => {
    currentIcon.value = showMobileNav.value ? X : Menu
    spinning.value = false
  }, 200)
}
</script>

<style scoped>
.slide-enter-active,
.slide-leave-active {
  transition: all 0.3s ease;
}

.slide-enter-from,
.slide-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}

.animate-spin {
  animation: spin 0.2s linear;
}

@keyframes spin {
  from {
    transform: rotate(0deg);
  }

  to {
    transform: rotate(180deg);
  }
}
</style>
