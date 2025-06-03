import { createRouter, createWebHistory } from 'vue-router'
import Layout from './components/Layout.vue'
import HomePage from './pages/Homepage.vue'

const routes = [
  {
    path: '/',
    component: Layout,
    children: [
      { path: '', component: HomePage },
      { path: 'about', component: () => import('./pages/About.vue') },
    ]
  }
]

export default createRouter({
  history: createWebHistory(),
  routes,
})
