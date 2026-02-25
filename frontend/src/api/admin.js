import axios from 'axios'

// Determine API base URL based on environment
const getApiBaseUrl = () => {
  if (import.meta.env.PROD) {
    return import.meta.env.VITE_API_URL || ''
  }
  return ''
}

const adminApi = axios.create({
  baseURL: getApiBaseUrl(),
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json'
  }
})

// Request interceptor - add auth token
adminApi.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('admin_token')
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
    return config
  },
  (error) => {
    return Promise.reject(error)
  }
)

// Response interceptor - handle 401
adminApi.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      localStorage.removeItem('admin_token')
      window.location.href = '/admin/login'
    }
    return Promise.reject(error)
  }
)

// Auth API
export const authApi = {
  login: (credentials) => adminApi.post('/api/admin/login', credentials),
  logout: () => adminApi.post('/api/admin/logout')
}

// Hospital Admin API
export const hospitalAdminApi = {
  getAll: (params = {}) => adminApi.get('/api/admin/hospitals', { params }),
  getById: (id) => adminApi.get(`/api/admin/hospitals/${id}`),
  create: (data) => adminApi.post('/api/admin/hospitals', data),
  update: (id, data) => adminApi.put(`/api/admin/hospitals/${id}`, data),
  delete: (id) => adminApi.delete(`/api/admin/hospitals/${id}`)
}

export default adminApi
