import { createRouter, createWebHistory } from 'vue-router'
import Layout from './components/Layout.vue'
import { Homepage, About } from './pages'
import Login from './pages/user_auth_pages/Login.vue'
import Register from './pages/user_auth_pages/Register.vue'
import { compile } from 'vue'


const routes = [
  {
    path: '/',
    component: Layout,
    children: [
      { path: '', component: Homepage },
      { path: 'about', component: About },
      { path: 'login', component: Login},
      { path: 'register', component: Register},
    ]
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
