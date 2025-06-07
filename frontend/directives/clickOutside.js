// directives/clickOutside.js
export default {
  beforeMount(el, binding) {
    el.clickOutsideEvent = (event) => {
      if (!el.contains(event.target) && !event.target.closest('[role="menu"]')) {
        binding.value()
      }
    }
    document.addEventListener('click', el.clickOutsideEvent)
  },
  unmounted(el) {
    document.removeEventListener('click', el.clickOutsideEvent)
  }
}
