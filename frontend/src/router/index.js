import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('@/views/Home.vue')
  },
  {
    path: '/hospitals',
    name: 'Hospitals',
    component: () => import('@/views/HospitalList.vue')
  },
  {
    path: '/hospitals/:id',
    name: 'HospitalDetail',
    component: () => import('@/views/HospitalDetail.vue')
  },
  {
    path: '/doctors',
    name: 'Doctors',
    component: () => import('@/views/DoctorList.vue')
  },
  {
    path: '/services',
    name: 'Services',
    component: () => import('@/views/Services.vue')
  },
  {
    path: '/cost',
    name: 'CostEstimator',
    component: () => import('@/views/CostEstimator.vue')
  },
  {
    path: '/about',
    name: 'About',
    component: () => import('@/views/About.vue')
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    } else {
      return { top: 0 }
    }
  }
})

export default router
