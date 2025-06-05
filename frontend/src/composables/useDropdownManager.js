import { ref } from 'vue'

const activeDropdown = ref(null)

export function useDropdownManager() {
  function openDropdown(id) {
    activeDropdown.value = id
  }
  function closeDropdown() {
    activeDropdown.value = null
  }
  function isActive(id) {
    return activeDropdown.value === id
  }
  return { activeDropdown, openDropdown, closeDropdown, isActive }
}
