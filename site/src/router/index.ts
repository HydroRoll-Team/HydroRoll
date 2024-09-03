// Composables
import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    component: () => import('@/views/index/index.vue'),
  },
  {
    path: '/:path(.*)',
    name: '404',
    component: () => import('@/views/404.vue'),
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
