<template>
    <!-- Topbar Navigation -->
    <div class="bg-gray-900 text-white py-2">
        <div class="container mx-auto px-4 text-sm">
            <div class="flex justify-between text-center">
                <div class="flex gap-4">
                    <a href="#" class="hover:text-blue-300">Download App</a>
                    <a href="#" class="hover:text-blue-300">Become a Seller</a>
                    <a href="#" class="hover:text-blue-300">Customer Support</a>
                </div>
                <div class="flex gap-4">
                    <div class="flex gap-1">
                        <Globe class="h-5 w-5"/>
                        <span>EN</span>
                    </div>
                    <a href="#" class="text-sm hover:text-blue-300">Register | Login</a>
                </div>
            </div>
        </div>
    </div>

    <!-- Main Navigation -->
     <header class="bg-white">
        <div class="container mx-auto px-4 mx-4">
            <div class="flex items-center gap-2 items-center">
                <img src="/cart.ico" alt="" srcset="">
                <h2 class="text-blue-600">ShopNow</h2>
            </div>
        </div>
     </header>
</template>

<script setup>
    import { Globe } from 'lucide-vue-next'
</script>
