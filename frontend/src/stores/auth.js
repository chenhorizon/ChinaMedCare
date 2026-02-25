import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { authApi } from '@/api/admin'

export const useAuthStore = defineStore('auth', () => {
  const token = ref(localStorage.getItem('admin_token') || '')
  const isAuthenticated = computed(() => !!token.value)

  function setToken(newToken) {
    token.value = newToken
    if (newToken) {
      localStorage.setItem('admin_token', newToken)
    } else {
      localStorage.removeItem('admin_token')
    }
  }

  async function login(username, password) {
    try {
      const response = await authApi.login({ username, password })
      setToken(response.data.access_token)
      return true
    } catch (error) {
      console.error('Login failed:', error)
      return false
    }
  }

  function logout() {
    setToken('')
  }

  return {
    token,
    isAuthenticated,
    login,
    logout
  }
})
