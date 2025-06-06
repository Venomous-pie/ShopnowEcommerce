import { ref } from 'vue'

export function useSearch(products) {
  const searchQuery = ref("")
  const searchSuggestions = ref([])
  const showSuggestions = ref(false)

  const updateSuggestions = () => {
    if (!searchQuery.value.trim()) {
      searchSuggestions.value = []
      showSuggestions.value = false
      return
    }
    const query = searchQuery.value.toLowerCase()
    searchSuggestions.value = products.value.filter(p =>
      p.name.toLowerCase().includes(query) ||
      (p.short_description && p.short_description.toLowerCase().includes(query))
    ).slice(0, 5) // limit to 5 suggestions
    showSuggestions.value = searchSuggestions.value.length > 0
  }

  const selectSuggestion = (product) => {
    searchQuery.value = product.name
    showSuggestions.value = false
  }

  return {
    searchQuery,
    searchSuggestions,
    showSuggestions,
    updateSuggestions,
    selectSuggestion
  }
}
