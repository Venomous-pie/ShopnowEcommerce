import { ref } from 'vue'

const activeDropdown = ref(null)
let lastToggleTimestamp = 0
const DEBOUNCE_DELAY = 50 // 50ms debounce

export function useDropdownManager() {
  function openDropdown(id) {
    const now = Date.now()
    if (now - lastToggleTimestamp < DEBOUNCE_DELAY) {
      return
    }
    lastToggleTimestamp = now
    console.log(`[Dropdown Debug] Opening dropdown with id: ${id}`)
    activeDropdown.value = id
  }

  function closeDropdown() {
    const now = Date.now()
    if (now - lastToggleTimestamp < DEBOUNCE_DELAY) {
      return
    }
    if (!activeDropdown.value) {
      console.log('[Dropdown Debug] No active dropdown to close')
      return
    }
    lastToggleTimestamp = now
    console.log(`[Dropdown Debug] Closing dropdown: ${activeDropdown.value}`)
    activeDropdown.value = null
  }

  function isActive(id) {
    return activeDropdown.value === id
  }

  return { activeDropdown, openDropdown, closeDropdown, isActive }
}
