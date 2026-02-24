<template>
  <div class="home">
    <!-- Hero Section -->
    <section class="hero">
      <div class="hero-background"></div>
      <div class="container">
        <div class="hero-content">
          <div class="hero-badge">
            <span class="badge-icon">✓</span>
            Trusted by 50,000+ international patients
          </div>
          <h1 class="hero-title">
            World-Class Medical Care
            <span class="title-accent">in China</span>
          </h1>
          <p class="hero-subtitle">
            Connect with top hospitals, expert doctors, and seamless medical services. Your journey to health starts here.
          </p>
          <div class="hero-actions">
            <button class="btn btn-primary btn-large" @click="$router.push('/hospitals')">
              <svg class="btn-icon" viewBox="0 0 20 20" fill="currentColor">
                <path d="M10 12a2 2 0 100-4 2 2 0 000 4z"/>
                <path fill-rule="evenodd" d="M.458 10C1.732 5.943 5.522 3 10 3s8.268 2.943 9.542 7c-1.274 4.057-5.064 7-9.542 7S1.732 14.057.458 10zM14 10a4 4 0 11-8 0 4 4 0 018 0z" clip-rule="evenodd"/>
              </svg>
              Find Hospitals
            </button>
            <button class="btn btn-secondary btn-large" @click="$router.push('/doctors')">
              Meet Doctors
            </button>
          </div>
          <div class="hero-stats">
            <div class="stat">
              <div class="stat-number">150+</div>
              <div class="stat-label">Partner Hospitals</div>
            </div>
            <div class="stat-divider"></div>
            <div class="stat">
              <div class="stat-number">2,000+</div>
              <div class="stat-label">Expert Doctors</div>
            </div>
            <div class="stat-divider"></div>
            <div class="stat">
              <div class="stat-number">98%</div>
              <div class="stat-label">Satisfaction Rate</div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Featured Hospitals -->
    <section class="section">
      <div class="container">
        <div class="section-header">
          <p class="section-subtitle">Top Medical Facilities</p>
          <h2 class="section-title">Featured Hospitals</h2>
          <p class="section-description">Hand-picked hospitals with international accreditations and multilingual staff</p>
        </div>
        <div class="hospital-grid">
          <HospitalCard v-for="hospital in hospitals" :key="hospital.id" :hospital="hospital" />
        </div>
        <div class="section-footer">
          <button class="btn btn-secondary" @click="$router.push('/hospitals')">
            View All Hospitals
            <svg class="btn-icon-arrow" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z" clip-rule="evenodd"/>
            </svg>
          </button>
        </div>
      </div>
    </section>

    <!-- Popular Departments -->
    <section class="section section-alt">
      <div class="container">
        <div class="section-header">
          <p class="section-subtitle">Specialties</p>
          <h2 class="section-title">Popular Departments</h2>
          <p class="section-description">Explore our most sought-after medical specialties</p>
        </div>
        <div class="department-grid">
          <div v-for="dept in departments" :key="dept.id" class="department-card" @click="selectDepartment(dept)">
            <div class="dept-icon-wrapper">
              <span class="dept-icon">{{ dept.icon }}</span>
            </div>
            <span class="dept-name">{{ dept.name }}</span>
            <span class="dept-arrow">→</span>
          </div>
        </div>
      </div>
    </section>

    <!-- How It Works -->
    <section class="section">
      <div class="container">
        <div class="section-header">
          <p class="section-subtitle">Simple Process</p>
          <h2 class="section-title">How It Works</h2>
          <p class="section-description">Get started in just 3 easy steps</p>
        </div>
        <div class="steps">
          <div class="step">
            <div class="step-number">01</div>
            <div class="step-content">
              <h3>Search & Choose</h3>
              <p>Browse hospitals and doctors, compare specialties and ratings</p>
            </div>
          </div>
          <div class="step-connector"></div>
          <div class="step">
            <div class="step-number">02</div>
            <div class="step-content">
              <h3>Book Appointment</h3>
              <p>Schedule your visit and share medical records securely</p>
            </div>
          </div>
          <div class="step-connector"></div>
          <div class="step">
            <div class="step-number">03</div>
            <div class="step-content">
              <h3>Receive Care</h3>
              <p>Get treated with our full support throughout your journey</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Services Preview -->
    <section class="section section-alt">
      <div class="container">
        <div class="section-header">
          <p class="section-subtitle">Comprehensive Support</p>
          <h2 class="section-title">Our Services</h2>
          <p class="section-description">We handle everything so you can focus on what matters</p>
        </div>
        <div class="service-grid">
          <div v-for="service in services" :key="service.id" class="service-card">
            <div class="service-icon">{{ service.icon }}</div>
            <h3>{{ service.title }}</h3>
            <p>{{ service.desc }}</p>
            <a href="/services" class="service-link">Learn more →</a>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA Section -->
    <section class="cta-section">
      <div class="container">
        <div class="cta-card">
          <div class="cta-content">
            <h2>Ready to Start Your Medical Journey?</h2>
            <p>Get a free consultation with our patient care team today</p>
          </div>
          <button class="btn btn-primary btn-large">Get Started</button>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import HospitalCard from '@/components/HospitalCard.vue'

const router = useRouter()

const hospitals = ref([
  {
    id: 1,
    name: 'Peking Union Medical College Hospital',
    location: 'Beijing, China',
    rating: 4.9,
    image: 'https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?w=600',
    departments: ['Cardiology', 'Neurology', 'Oncology', 'Orthopedics'],
    languages: ['English', 'Chinese', 'Japanese']
  },
  {
    id: 2,
    name: 'Shanghai First People\'s Hospital',
    location: 'Shanghai, China',
    rating: 4.8,
    image: 'https://images.unsplash.com/photo-1586773860418-d37222d8fce3?w=600',
    departments: ['Cardiology', 'Orthopedics', 'TCM', 'Dermatology'],
    languages: ['English', 'Chinese', 'Korean']
  },
  {
    id: 3,
    name: 'Guangdong Provincial People\'s Hospital',
    location: 'Guangzhou, China',
    rating: 4.7,
    image: 'https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=600',
    departments: ['Oncology', 'Cardiology', 'Reproductive', 'Pediatrics'],
    languages: ['English', 'Chinese', 'Russian']
  }
])

const departments = ref([
  { id: 1, name: 'Cardiology', icon: '❤️' },
  { id: 2, name: 'Orthopedics', icon: '🦴' },
  { id: 3, name: 'Neurology', icon: '🧠' },
  { id: 4, name: 'Oncology', icon: '🎗️' },
  { id: 5, name: 'TCM', icon: '🌿' },
  { id: 6, name: 'Dermatology', icon: '🩺' },
  { id: 7, name: 'Reproductive', icon: '👶' },
  { id: 8, name: 'Ophthalmology', icon: '👁️' }
])

const services = ref([
  { id: 1, icon: '📅', title: 'Appointment Booking', desc: 'Book appointments with top doctors online in minutes' },
  { id: 2, icon: '📄', title: 'Medical Translation', desc: 'Professional translation of medical records by experts' },
  { id: 3, icon: '🧑‍⚕️', title: 'Medical Escort', desc: 'Personal interpreter and guide for hospital visits' },
  { id: 4, icon: '✈️', title: 'Visa Assistance', desc: 'Support with medical visa application process' }
])

const selectDepartment = (dept) => {
  router.push({ path: '/hospitals', query: { department: dept.name } })
}
</script>

<style scoped>
.hero {
  position: relative;
  padding: 120px 0 100px;
  overflow: hidden;
}

.hero-background {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 50%, #f0fdf4 100%);
  z-index: -1;
}

.hero-background::before {
  content: '';
  position: absolute;
  top: -50%;
  right: -20%;
  width: 800px;
  height: 800px;
  background: radial-gradient(circle, rgba(37, 99, 235, 0.1) 0%, transparent 70%);
  border-radius: 50%;
}

.hero-content {
  text-align: center;
  max-width: 800px;
  margin: 0 auto;
}

.hero-badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: white;
  padding: 8px 16px;
  border-radius: 100px;
  font-size: 14px;
  font-weight: 500;
  color: var(--text-secondary);
  box-shadow: var(--shadow-md);
  margin-bottom: 24px;
}

.badge-icon {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 20px;
  height: 20px;
  background: var(--success);
  color: white;
  border-radius: 50%;
  font-size: 12px;
}

.hero-title {
  font-size: 56px;
  font-weight: 800;
  line-height: 1.1;
  color: var(--text-primary);
  margin-bottom: 20px;
  letter-spacing: -0.02em;
}

.title-accent {
  background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.hero-subtitle {
  font-size: 20px;
  color: var(--text-secondary);
  margin-bottom: 40px;
  line-height: 1.6;
}

.hero-actions {
  display: flex;
  gap: 16px;
  justify-content: center;
  margin-bottom: 56px;
}

.btn-large {
  padding: 14px 28px;
  font-size: 16px;
}

.btn-icon {
  width: 20px;
  height: 20px;
}

.btn-icon-arrow {
  width: 16px;
  height: 16px;
}

.hero-stats {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 48px;
}

.stat {
  text-align: center;
}

.stat-number {
  font-size: 32px;
  font-weight: 800;
  color: var(--primary);
  margin-bottom: 4px;
}

.stat-label {
  font-size: 14px;
  color: var(--text-secondary);
}

.stat-divider {
  width: 1px;
  height: 48px;
  background: var(--border);
}

.hospital-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
  margin-bottom: 40px;
}

.section-footer {
  text-align: center;
}

.department-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 20px;
}

.department-card {
  background: white;
  padding: 24px;
  border-radius: var(--radius-lg);
  display: flex;
  align-items: center;
  gap: 16px;
  cursor: pointer;
  transition: all 0.2s ease;
  border: 1px solid var(--border);
}

.department-card:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-lg);
  border-color: var(--primary-light);
}

.dept-icon-wrapper {
  width: 56px;
  height: 56px;
  background: linear-gradient(135deg, var(--primary-light) 0%, #f0f9ff 100%);
  border-radius: var(--radius-md);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.dept-icon {
  font-size: 28px;
}

.dept-name {
  flex: 1;
  font-weight: 600;
  color: var(--text-primary);
}

.dept-arrow {
  color: var(--text-muted);
  font-size: 20px;
  transition: transform 0.2s ease;
}

.department-card:hover .dept-arrow {
  transform: translateX(4px);
  color: var(--primary);
}

.steps {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  max-width: 1000px;
  margin: 0 auto;
  position: relative;
}

.step {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  flex: 1;
  position: relative;
  z-index: 1;
}

.step-number {
  width: 64px;
  height: 64px;
  background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
  color: white;
  border-radius: var(--radius-lg);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 24px;
  font-weight: 800;
  margin-bottom: 24px;
  box-shadow: var(--shadow-md);
}

.step-content h3 {
  font-size: 20px;
  font-weight: 700;
  margin-bottom: 8px;
  color: var(--text-primary);
}

.step-content p {
  color: var(--text-secondary);
  font-size: 15px;
  line-height: 1.6;
}

.step-connector {
  flex: 0.5;
  height: 2px;
  background: linear-gradient(90deg, var(--primary) 0%, var(--border) 100%);
  margin-top: 32px;
  opacity: 0.3;
}

.service-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 24px;
}

.service-card {
  background: white;
  padding: 32px 24px;
  border-radius: var(--radius-lg);
  border: 1px solid var(--border);
  transition: all 0.2s ease;
}

.service-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-lg);
  border-color: var(--primary-light);
}

.service-icon {
  font-size: 40px;
  margin-bottom: 20px;
  display: block;
}

.service-card h3 {
  font-size: 18px;
  font-weight: 700;
  margin-bottom: 12px;
  color: var(--text-primary);
}

.service-card p {
  color: var(--text-secondary);
  font-size: 14px;
  line-height: 1.6;
  margin-bottom: 20px;
}

.service-link {
  color: var(--primary);
  font-weight: 600;
  font-size: 14px;
  text-decoration: none;
  transition: color 0.2s ease;
}

.service-link:hover {
  color: var(--primary-dark);
}

.cta-section {
  padding: 80px 0;
}

.cta-card {
  background: linear-gradient(135deg, var(--primary) 0%, var(--primary-dark) 100%);
  border-radius: var(--radius-xl);
  padding: 56px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 40px;
  box-shadow: var(--shadow-xl);
}

.cta-content h2 {
  color: white;
  font-size: 32px;
  font-weight: 700;
  margin-bottom: 8px;
}

.cta-content p {
  color: rgba(255, 255, 255, 0.8);
  font-size: 18px;
}

.cta-card .btn-primary {
  background: white;
  color: var(--primary);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  white-space: nowrap;
}

.cta-card .btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.2);
}
</style>
