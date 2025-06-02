import { createRouter, createWebHistory } from 'vue-router'
import Layout from './components/Layout.vue'
import HomePage from './components/homepage.vue'
import ProductPage from './components/ProductPage.vue'

const routes = [
  {
    path: '/',
    component: Layout,
    children: [
      { path: '', component: HomePage },
      { path: 'product/:id', component: ProductPage, props: true }
    ]
  }
]

export default createRouter({
  history: createWebHistory(),
  routes,
})
