import axios from 'axios'

// Determine API base URL based on environment
const getApiBaseUrl = () => {
  // In production, use Vercel env var or fallback to relative path
  if (import.meta.env.PROD) {
    let apiUrl = import.meta.env.VITE_API_URL || ''
    // Ensure URL has https:// prefix
    if (apiUrl && !apiUrl.startsWith('http')) {
      apiUrl = 'https://' + apiUrl
    }
    // Remove trailing slash
    if (apiUrl.endsWith('/')) {
      apiUrl = apiUrl.slice(0, -1)
    }
    console.log('API Base URL:', apiUrl)
    return apiUrl
  }
  // In development, use the proxy
  return ''
}

const api = axios.create({
  baseURL: getApiBaseUrl(),
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json'
  }
})

// Hospital API
export const hospitalApi = {
  getAll: (params = {}) => api.get('/api/hospitals/', { params }),
  getById: (id) => api.get(`/api/hospitals/${id}`)
}

// Doctor API
export const doctorApi = {
  getAll: (params = {}) => api.get('/api/doctors/', { params }),
  getById: (id) => api.get(`/api/doctors/${id}`)
}

// Booking API
export const bookingApi = {
  create: (data) => api.post('/api/bookings/', data),
  getById: (id) => api.get(`/api/bookings/${id}`)
}

export default api
