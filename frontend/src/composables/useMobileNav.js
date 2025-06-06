import { ref } from 'vue'
import { Menu, X } from 'lucide-vue-next'

export function useMobileNav() {
  const mobileSearchOpen = ref(false)
  const showMobileNav = ref(false)
  const spinning = ref(false)
  const currentIcon = ref(Menu)

  const setShowMobileNav = (value) => {
    showMobileNav.value = value
    currentIcon.value = value ? X : Menu
  }

  const toggleMobileSearch = () => {
    mobileSearchOpen.value = !mobileSearchOpen.value
    // Close mobile nav if open
    if (mobileSearchOpen.value && showMobileNav.value) {
      setShowMobileNav(false)
    }
  }

  const handleIconClick = () => {
    spinning.value = true
    setShowMobileNav(!showMobileNav.value)
    // Close mobile search if open
    if (showMobileNav.value && mobileSearchOpen.value) {
      mobileSearchOpen.value = false
    }
    setTimeout(() => {
      spinning.value = false
    }, 200)
  }

  return {
    mobileSearchOpen,
    showMobileNav,
    spinning,
    currentIcon,
    toggleMobileSearch,
    handleIconClick,
    setShowMobileNav
  }
}
