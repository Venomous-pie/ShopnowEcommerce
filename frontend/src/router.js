import { createRouter, createWebHistory } from 'vue-router'
import Layout from './components/Layout.vue'
import { Homepage, About } from './pages'

const routes = [
  {
    path: '/',
    component: Layout,
    children: [
      { path: '', component: Homepage },
      { path: 'about', component: About },
    ]
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
