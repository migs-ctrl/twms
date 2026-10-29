import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { BootstrapVue, BootstrapVueIcons } from 'bootstrap-vue'
import { createWebHistory, createRouter } from 'vue-router'

import App from './App.vue'
import ViewClients from './components/ViewClients.vue'
import Home from './components/Home.vue'
import SignIn from './components/SignIn.vue'
import './assets/main.css'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'


const routes = [
  { path: '/', component: Home },
  { path: '/clients', component: ViewClients },
  { path: '/signin', component: SignIn}
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

const pinia = createPinia()

var app = createApp(App)
app.use(BootstrapVue)
app.use(BootstrapVueIcons)
app.use(router)
app.use(pinia)
app.mount('#app')
