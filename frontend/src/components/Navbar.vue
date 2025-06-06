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
          <div class="relative sm:hidden" ref="dropdownRef" v-click-outside="closeDropdown">
            <div @click.stop="() => toggleDropdown('more')"
              class="flex items-center cursor-pointer select-none text-xs lg:text-sm px-2 py-1 rounded-md hover:bg-white/10 transition-colors duration-200"
              :class="{ 'bg-white/10': isActive('more') }" aria-haspopup="true" :aria-expanded="isActive('more')">
              <span class="text-white">More</span>
              <ChevronDown class="ml-1 w-4 h-4 text-white transition-transform duration-200"
                :class="{ 'rotate-180': isActive('more') }" />
            </div>

            <!-- Dropdown Menu -->
            <Transition enter-active-class="transition duration-200 ease-out"
              enter-from-class="transform scale-95 opacity-0" enter-to-class="transform scale-100 opacity-100"
              leave-active-class="transition duration-150 ease-in" leave-from-class="transform scale-100 opacity-100"
              leave-to-class="transform scale-95 opacity-0">
              <div v-if="isActive('more')"
                class="absolute left-0 mt-2 w-48 bg-white text-gray-700 rounded-lg shadow-lg z-50 border border-gray-200 overflow-hidden"
                role="menu">
                <div class="py-1">
                  <a href="#"
                    class="flex items-center px-4 py-2.5 hover:bg-gray-50 text-sm transition-colors duration-150 hover:text-blue-700"
                    role="menuitem">
                    <Smartphone class="h-4 w-4 mr-2 text-gray-500" />
                    <span>Download App</span>
                  </a>
                  <a href="#"
                    class="flex items-center px-4 py-2.5 hover:bg-gray-50 text-sm transition-colors duration-150 hover:text-blue-700"
                    role="menuitem">
                    <Store class="h-4 w-4 mr-2 text-gray-500" />
                    <span>Become a Seller</span>
                  </a>
                  <a href="#"
                    class="flex items-center px-4 py-2.5 hover:bg-gray-50 text-sm transition-colors duration-150 hover:text-blue-700"
                    role="menuitem">
                    <HelpCircle class="h-4 w-4 mr-2 text-gray-500" />
                    <span>Customer Support</span>
                  </a>
                </div>

                <hr class="border-gray-200" />

                <div class="px-4 py-2">
                  <div class="flex items-center justify-center gap-3">
                    <a href="#"
                      class="flex-1 text-center text-sm font-medium py-1.5 px-2 rounded-md bg-gray-100 hover:bg-gray-200 transition-colors duration-150">
                      Register
                    </a>
                    <a href="#"
                      class="flex-1 text-center text-sm font-medium py-1.5 px-2 rounded-md bg-blue-50 text-blue-600 hover:bg-blue-100 transition-colors duration-150">
                      Login
                    </a>
                  </div>
                </div>
              </div>
            </Transition>
          </div>
        </div>
        <div class="flex items-center gap-4">
          <div class="flex gap-1 items-center text-xs lg:text-sm">
            <Globe class="h-4 w-4" />
            <a class="hover:text-blue-300">EN</a>
          </div>
          <div class="hidden sm:flex items-center justify-center gap-2">
            <a href="#" class="text-sm font-medium hover:text-blue-600">Register</a>
            <span class="text-gray-400">|</span>
            <a href="#" class="text-sm font-medium hover:text-blue-600">Login</a>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Main Navigation -->
  <header class="bg-white shadow px-4 relative sticky top-0 z-40">
    <div class="container mx-auto py-3 flex items-center justify-between">
      <!-- Logo -->
      <div class="flex items-center gap-2">
        <img src="/cart.ico" alt="cart icon" class="h-6" />
        <router-link to="/" class="text-blue-600 text-lg font-semibold">ShopNow</router-link>
      </div>

      <!-- Desktop Nav -->
      <nav class="hidden md:flex gap-6 text-gray-700 text-sm">
        <router-link to="/" class="hover:text-blue-600">Home</router-link>
        <div class="relative" @mouseenter="toggleDropdown('categories')" @mouseleave="closeDropdown('categories')">
          <div class="hover:text-blue-600 flex items-center cursor-pointer"
            @click.stop="() => toggleDropdown('categories')">
            Categories
            <ChevronDown class="ml-1 w-4 h-4 transition-transform" :class="{ 'rotate-180': isActive('categories') }" />
          </div>
          <div v-if="isActive('categories')"
            class="absolute transform translate-x-3/7 right-0 top-full w-[36rem] bg-white text-gray-900 rounded-lg shadow-lg z-30 border border-gray-200 overflow-hidden">
            <!-- Simple Header -->
            <div class="px-4 py-1 bg-gray-50 border-b border-gray-100">
              <h3 class="text-sm font-medium text-gray-700">Shop by Category</h3>
            </div>

            <!-- Categories -->
            <div class="p-3">
              <div class="grid gap-1 grid-cols-[repeat(auto-fill,minmax(10rem,1fr))] max-h-[30rem] overflow-y-auto pr-1">

                <router-link v-for="cat in categories" :key="cat" :to="`/category/${encodeURIComponent(cat)}`"
                  class="flex items-center px-3 py-4 hover:bg-gray-50 text-sm text-gray-700 hover:text-blue-600 transition-colors duration-150 rounded-md group/item">
                  <!-- Category Icon -->
                  <div class="w-5 h-5 flex items-center justify-center mr-2">
                    <component :is="getCategoryIcon(cat)" class="w-4 h-4 text-gray-400" />
                  </div>
                  <span>{{ cat.length > 20 ? cat.slice(0, 15) + '...' : cat }}</span>
                </router-link>
              </div>
            </div>
          </div>
        </div>
        <router-link to="/" class="hover:text-blue-600">Products</router-link>
      </nav>

      <!-- Right Side Icons -->
      <div class="flex items-center gap-4">
        <!-- Desktop Search -->
        <div class="relative ml-4 hidden sm:block" v-click-outside="() => showSuggestions = false">
          <input v-model="searchQuery" @input="updateSuggestions" @focus="updateSuggestions" type="text"
            placeholder="Search products..."
            class="w-64 pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent text-sm" />
          <Search class="absolute left-3 top-1/2 transform -translate-y-1/2 h-4 w-4 text-gray-400" />
          <div v-if="showSuggestions"
            class="absolute left-0 mt-1 w-full bg-white border border-gray-200 rounded shadow-lg z-40">
            <div v-for="suggestion in searchSuggestions" :key="suggestion.sku"
              @mousedown.prevent="selectSuggestion(suggestion)"
              class="px-4 py-2 cursor-pointer hover:bg-blue-50 text-sm text-gray-700 flex items-center gap-2">
              <img :src="suggestion.image" alt="" class="w-8 h-8 object-cover rounded mr-2" />
              <span>{{ suggestion.name }}</span>
            </div>
            <div v-if="searchSuggestions.length === 0" class="px-4 py-2 text-gray-400 text-sm">No results found</div>
          </div>
        </div>

        <!-- Mobile Search Icon -->
        <div @click="toggleMobileSearch" class="md:hidden cursor-pointer p-1 hover:bg-gray-100 rounded">
          <Search class="h-5 w-5 text-gray-600 hover:text-blue-600 transition-colors" />
        </div>

        <!-- User Account Dropdown -->
        <div class="relative" ref="userDropdownRef" v-click-outside="closeUserDropdown">
          <div @click.stop="() => toggleDropdown('user')"
            class="flex items-center justify-center cursor-pointer p-2 hover:bg-gray-100 rounded-full transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-gray-200"
            :class="{ 'bg-gray-100': isActive('user') }" aria-haspopup="true" :aria-expanded="isActive('user')">
            <UserRound class="h-5 w-5 text-gray-600 mb-1" />
          </div>

          <!-- Dropdown Menu -->
          <Transition enter-active-class="transition duration-200 ease-out"
            enter-from-class="transform scale-95 opacity-0" enter-to-class="transform scale-100 opacity-100"
            leave-active-class="transition duration-150 ease-in" leave-from-class="transform scale-100 opacity-100"
            leave-to-class="transform scale-95 opacity-0">
            <div v-if="isActive('user')"
              class="absolute transform translate-x-3/7 mt-2 bg-white text-gray-700 rounded-lg shadow-lg z-30 border border-gray-200 overflow-hidden right-0 w-48 sm:w-56"
              role="menu">
              <div class="py-1">
                <a href="#"
                  class="flex items-center px-4 py-2.5 hover:bg-gray-50 text-sm transition-colors duration-150 hover:text-blue-700"
                  role="menuitem">
                  <UserPlus class="h-4 w-4 mr-2 text-gray-500" />
                  <span>Create Account</span>
                </a>
                <a href="#"
                  class="flex items-center px-4 py-2.5 hover:bg-gray-50 text-sm transition-colors duration-150 hover:text-blue-700"
                  role="menuitem">
                  <Package class="h-4 w-4 mr-2 text-gray-500" />
                  <span>My Orders</span>
                </a>
                <a href="#"
                  class="flex items-center px-4 py-2.5 hover:bg-gray-50 text-sm transition-colors duration-150 hover:text-blue-700"
                  role="menuitem">
                  <Heart class="h-4 w-4 mr-2 text-gray-500" />
                  <span>Wishlist</span>
                </a>
              </div>

              <hr class="border-gray-200" />

              <div class="px-4 py-2">
                <div class="flex items-center justify-center gap-3 sm:gap-4">
                  <a href="#"
                    class="flex-1 text-center text-sm font-medium py-1.5 px-2 rounded-md bg-gray-100 hover:bg-gray-200 transition-colors duration-150">
                    Register
                  </a>
                  <a href="#"
                    class="flex-1 text-center text-sm font-medium py-1.5 px-2 rounded-md bg-blue-50 text-blue-600 hover:bg-blue-100 transition-colors duration-150">
                    Login
                  </a>
                </div>
              </div>
            </div>
          </Transition>
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
          <input v-model="searchQuery" @input="updateSuggestions" @focus="updateSuggestions" type="text"
            placeholder="Search products..."
            class="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent box-border" />
          <Search class="absolute left-3 top-1/2 transform -translate-y-1/2 h-4 w-4 text-gray-400" />
          <div v-if="showSuggestions"
            class="absolute left-0 mt-1 w-full bg-white border border-gray-200 rounded shadow-lg z-40">
            <div v-for="suggestion in searchSuggestions" :key="suggestion.sku"
              @mousedown.prevent="selectSuggestion(suggestion)"
              class="px-4 py-2 cursor-pointer hover:bg-blue-50 text-sm text-gray-700 flex items-center gap-2">
              <img :src="suggestion.image" alt="" class="w-8 h-8 object-cover rounded mr-2" />
              <span>{{ suggestion.name }}</span>
            </div>
            <div v-if="searchSuggestions.length === 0" class="px-4 py-2 text-gray-400 text-sm">No results found</div>
          </div>
        </div>
      </div>
    </transition>

    <!-- Mobile Menu -->
    <transition name="slide">
      <nav v-if="showMobileNav" ref="MobileNavRef"
        class="absolute top-full left-0 right-0 md:hidden bg-white px-4 pb-4 shadow-lg z-20 border-t">
        <router-link to="/" class="block py-2 text-gray-700 hover:text-blue-600">Home</router-link>

        <!-- Mobile Categories Dropdown -->
        <div>
          <div @click.stop="() => toggleDropdown('categories')"
            class="flex items-center justify-between py-2 text-gray-700 hover:text-blue-600 cursor-pointer">
            <span>Categories</span>
            <ChevronDown :class="{ 'transform rotate-180': isActive('categories') }"
              class="w-4 h-4 transition-transform duration-200" />
          </div>

          <transition name="expand">
            <div v-if="isActive('categories')" class="pl-4 border-l-2 border-gray-100 ml-2 mt-1 mb-2">
              <router-link v-for="cat in categories" :key="cat" :to="`/category/${encodeURIComponent(cat)}`"
                class="block py-2 text-sm text-gray-600 hover:text-blue-600 border-b border-gray-50 last:border-b-0">
                {{ cat }}
              </router-link>
            </div>
          </transition>
        </div>

        <router-link to="/" class="block py-2 text-gray-700 hover:text-blue-600">Products</router-link>
      </nav>
    </transition>
  </header>
</template>

<script setup>
import { onMounted } from 'vue'
import {
  Globe,
  ChevronDown,
  UserRound,
  ShoppingBasket,
  Heart,
  Search,
  UserPlus,
  Package,
  Smartphone,
  Store,
  HelpCircle,
} from 'lucide-vue-next'
import { useDropdownManager } from '../composables/useDropdownManager'
import { useSearch } from '../composables/useSearch'
import { useMobileNav } from '../composables/useMobileNav'
import { useCategories } from '../composables/useCategories'

// Initialize composables
const { activeDropdown, openDropdown, closeDropdown, isActive } = useDropdownManager()
const { categories, products, getCategoryIcon, loadCategories } = useCategories()
const { searchQuery, searchSuggestions, showSuggestions, updateSuggestions, selectSuggestion } = useSearch(products)
const { mobileSearchOpen, showMobileNav, spinning, currentIcon, toggleMobileSearch, handleIconClick } = useMobileNav()

// Dropdown toggle function
const toggleDropdown = (id) => {
  if (isActive(id)) {
    closeDropdown()
  } else {
    openDropdown(id)
  }
}

const closeUserDropdown = () => {
  if (isActive('user')) {
    closeDropdown()
  }
}

// Load categories on mount
onMounted(loadCategories)
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

.expand-enter-active,
.expand-leave-active {
  transition: all 0.3s ease;
  max-height: 500px;
  overflow: hidden;
}

.expand-enter-from,
.expand-leave-to {
  max-height: 0;
  opacity: 0;
}
</style>
