import { ref } from 'vue'
import { Menu, X } from 'lucide-vue-next'

export function useMobileNav() {
  const mobileSearchOpen = ref(false)
  const showMobileNav = ref(false)
  const spinning = ref(false)
  const currentIcon = ref(Menu)

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

  return {
    mobileSearchOpen,
    showMobileNav,
    spinning,
    currentIcon,
    toggleMobileSearch,
    handleIconClick
  }
}
