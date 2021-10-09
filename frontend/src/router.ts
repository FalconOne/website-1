import { createRouter, createWebHistory, routerKey } from "vue-router";
import Home from './pages/Home.vue'
import Contact from './pages/Contact.vue'

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/',
            component: Home
        },
        {
            path: '/contact',
            component: Contact
        }
    ]
})

export default router