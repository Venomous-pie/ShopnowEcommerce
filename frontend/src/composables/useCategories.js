import { ref } from 'vue'
import {
  Tag,
  Monitor,
  Home,
  Shirt,
  HeartHandshake,
  Dumbbell,
  ShoppingCart,
  Leaf,
  LampDesk,
  ToyBrick,
  Flame,
  Star,
  Gift,
  BadgePercent,
  Sparkles,
  Footprints,
  Backpack,
  Cable,
  BookOpen,
} from 'lucide-vue-next'

export function useCategories() {
  const categories = ref([])
  const products = ref([])

  const categoryIcons = {
    'electronics': Monitor,
    'home & kitchen': Home,
    'sportswear': Dumbbell,
    'health & wellness': HeartHandshake,
    'toys & games': ToyBrick,
    'office supplies': LampDesk,
    'fashion': Shirt,
    'beauty': Sparkles,
    'sale': BadgePercent,
    'new arrivals': Star,
    'bestsellers': Flame,
    'gifts': Gift,
    'grocery': ShoppingCart,
    'home & living': Home,
    'footwear': Footprints,
    'home decor': LampDesk,
    'bags & luggage': Backpack,
    'computers & accessories': Cable,
    'garden & outdoor': Leaf,
    'books': BookOpen,
    default: Tag
  }

  const getCategoryIcon = (cat) => {
    if (!cat) return categoryIcons.default
    const key = cat.trim().toLowerCase()
    return categoryIcons[key] || categoryIcons.default
  }

  const loadCategories = async () => {
    try {
      const response = await fetch('/products.json')
      const data = await response.json()
      products.value = data
      const counts = {}
      data.forEach(p => {
        counts[p.category] = (counts[p.category] || 0) + 1
      })
      const sorted = Object.entries(counts).sort((a, b) => b[1] - a[1])
      categories.value = sorted.map(([cat]) => cat)
    } catch (error) {
      console.error('Error loading products:', error)
    }
  }

  return {
    categories,
    products,
    getCategoryIcon,
    loadCategories
  }
}
