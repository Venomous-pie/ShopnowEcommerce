import { createApp } from 'vue'
import { createPinia } from 'pinia'
import Toast from 'vue-toastification'
import 'vue-toastification/dist/index.css'
import App from './App.vue'
import router from './router'
import 'virtual:uno.css'
import './style.css'
import clickOutside from '../directives/clickOutside'

const app = createApp(App)
const pinia = createPinia()

// Configure toast
const toastOptions = {
    position: "top-right",
    timeout: 3000,
    closeOnClick: true,
    pauseOnFocusLoss: true,
    pauseOnHover: true,
    draggable: true,
    draggablePercent: 0.6,
    showCloseButtonOnHover: false,
    hideProgressBar: false,
    closeButton: "button",
    icon: true,
    rtl: false
}

app.directive('click-outside', clickOutside)
app.use(pinia)
app.use(router)
app.use(Toast, toastOptions)

app.mount('#app')
