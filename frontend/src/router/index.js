import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

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
  },
  // Admin Routes
  {
    path: '/admin/login',
    name: 'AdminLogin',
    component: () => import('@/views/admin/Login.vue')
  },
  {
    path: '/admin',
    component: () => import('@/views/admin/Layout.vue'),
    meta: { requiresAuth: true },
    children: [
      {
        path: '',
        redirect: '/admin/hospitals'
      },
      {
        path: 'hospitals',
        name: 'AdminHospitals',
        component: () => import('@/views/admin/HospitalList.vue')
      }
    ]
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

// Auth guard
router.beforeEach((to, from, next) => {
  const authStore = useAuthStore()

  if (to.meta.requiresAuth && !authStore.isAuthenticated) {
    next('/admin/login')
  } else if (to.path === '/admin/login' && authStore.isAuthenticated) {
    next('/admin/hospitals')
  } else {
    next()
  }
})

export default router
