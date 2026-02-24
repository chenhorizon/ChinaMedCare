<template>
  <div class="home">
    <!-- Trust Banner -->
    <div class="trust-banner">
      <div class="container">
        <div class="trust-items">
          <div class="trust-item">
            <svg class="trust-icon" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/>
            </svg>
            JCI Accredited Hospitals
          </div>
          <div class="trust-item">
            <svg class="trust-icon" viewBox="0 0 20 20" fill="currentColor">
              <path d="M10 2a.75.75 0 01.671.416l7.25 14.5a.75.75 0 01-.671 1.084H2.75a.75.75 0 01-.671-1.084l7.25-14.5A.75.75 0 0110 2zM10 5.5a.75.75 0 00-.75.75v3.5c0 .414.336.75.75.75h3.5a.75.75 0 000-1.5H10.75V6.25A.75.75 0 0010 5.5z"/>
            </svg>
            24/7 Patient Support
          </div>
          <div class="trust-item">
            <svg class="trust-icon" viewBox="0 0 20 20" fill="currentColor">
              <path d="M4 4a2 2 0 00-2 2v1h16V6a2 2 0 00-2-2H4z"/>
              <path fill-rule="evenodd" d="M18 9H2v5a2 2 0 002 2h12a2 2 0 002-2V9zM4 13a1 1 0 011-1h1a1 1 0 110 2H5a1 1 0 01-1-1zm5-1a1 1 0 100 2h1a1 1 0 100-2H9z" clip-rule="evenodd"/>
            </svg>
            Secure Payment Protection
          </div>
          <div class="trust-item">
            <svg class="trust-icon" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clip-rule="evenodd"/>
            </svg>
            50,000+ Patients Served
          </div>
        </div>
      </div>
    </div>

    <!-- Hero Section with Search -->
    <section class="hero">
      <div class="hero-background">
        <div class="hero-overlay"></div>
      </div>
      <div class="container">
        <div class="hero-content">
          <h1 class="hero-title">
            Find World-Class Medical Care
            <span class="title-accent">in China</span>
          </h1>
          <p class="hero-subtitle">
            Connect with 150+ accredited hospitals, 2,000+ expert doctors, and seamless medical travel services
          </p>

          <!-- Search Box - Booking.com style -->
          <div class="search-box">
            <div class="search-row">
              <div class="search-input-wrapper">
                <svg class="search-icon" viewBox="0 0 20 20" fill="currentColor">
                  <path fill-rule="evenodd" d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z" clip-rule="evenodd"/>
                </svg>
                <input type="text" class="search-input" placeholder="Search by hospital, specialty, or city..." />
              </div>
              <button class="search-btn" @click="$router.push('/hospitals')">
                <svg viewBox="0 0 20 20" fill="currentColor">
                  <path fill-rule="evenodd" d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z" clip-rule="evenodd"/>
                </svg>
                Search
              </button>
            </div>
            <div class="search-quick">
              <span class="quick-label">Popular searches:</span>
              <button class="quick-tag" @click="searchByDept('Cardiology')">Cardiology</button>
              <button class="quick-tag" @click="searchByDept('Orthopedics')">Orthopedics</button>
              <button class="quick-tag" @click="searchByDept('Oncology')">Oncology</button>
              <button class="quick-tag" @click="searchByDept('TCM')">TCM</button>
            </div>
          </div>

          <!-- Hero Stats -->
          <div class="hero-stats">
            <div class="stat">
              <div class="stat-number">150+</div>
              <div class="stat-label">Hospitals</div>
            </div>
            <div class="stat">
              <div class="stat-number">2,000+</div>
              <div class="stat-label">Doctors</div>
            </div>
            <div class="stat">
              <div class="stat-number">98%</div>
              <div class="stat-label">Satisfaction</div>
            </div>
            <div class="stat">
              <div class="stat-number">50k+</div>
              <div class="stat-label">Patients</div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Featured Hospitals -->
    <section class="section">
      <div class="container">
        <div class="section-header">
          <div class="section-header-left">
            <p class="section-subtitle">Top Picks</p>
            <h2 class="section-title">Featured Hospitals</h2>
          </div>
          <button class="btn-link" @click="$router.push('/hospitals')">
            View all hospitals
            <svg viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z" clip-rule="evenodd"/>
            </svg>
          </button>
        </div>
        <div class="hospital-grid">
          <HospitalCard v-for="hospital in hospitals" :key="hospital.id" :hospital="hospital" />
        </div>
      </div>
    </section>

    <!-- Popular Specialties -->
    <section class="section section-alt">
      <div class="container">
        <div class="section-header">
          <div class="section-header-left">
            <p class="section-subtitle">Medical Specialties</p>
            <h2 class="section-title">Popular Treatments</h2>
          </div>
        </div>
        <div class="specialty-grid">
          <div v-for="dept in departments" :key="dept.id" class="specialty-card" @click="selectDepartment(dept)">
            <div class="specialty-icon">{{ dept.icon }}</div>
            <div class="specialty-info">
              <h3>{{ dept.name }}</h3>
              <p>{{ dept.hospitals }} hospitals</p>
            </div>
            <svg class="specialty-arrow" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clip-rule="evenodd"/>
            </svg>
          </div>
        </div>
      </div>
    </section>

    <!-- Why Choose Us -->
    <section class="section">
      <div class="container">
        <div class="section-header centered">
          <p class="section-subtitle">Why ChinaMedCare</p>
          <h2 class="section-title">Your Trusted Medical Partner</h2>
        </div>
        <div class="features-grid">
          <div class="feature-card">
            <div class="feature-icon-wrapper">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/>
              </svg>
            </div>
            <h3>Verified Hospitals</h3>
            <p>All hospitals are JCI accredited and thoroughly vetted for quality and safety</p>
          </div>
          <div class="feature-card">
            <div class="feature-icon-wrapper">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M3 5h12M9 3v2m1.048 9.5A18.022 18.022 0 016.412 9m6.088 9h7M11 21l5-10 5 10M12.751 5C11.783 10.77 8.07 15.61 3 18.129"/>
              </svg>
            </div>
            <h3>Multilingual Support</h3>
            <p>24/7 support in English, Russian, Japanese, Korean, and Chinese</p>
          </div>
          <div class="feature-card">
            <div class="feature-icon-wrapper">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
              </svg>
            </div>
            <h3>Transparent Pricing</h3>
            <p>Clear cost estimates with no hidden fees. Compare and save up to 70%</p>
          </div>
          <div class="feature-card">
            <div class="feature-icon-wrapper">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"/>
              </svg>
            </div>
            <h3>End-to-End Service</h3>
            <p>From booking to recovery, we manage every step of your journey</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Testimonials -->
    <section class="section section-alt">
      <div class="container">
        <div class="section-header centered">
          <p class="section-subtitle">Patient Stories</p>
          <h2 class="section-title">What Our Patients Say</h2>
        </div>
        <div class="testimonial-grid">
          <div class="testimonial-card" v-for="t in testimonials" :key="t.id">
            <div class="testimonial-rating">
              <span v-for="i in 5" :key="i" class="star">{{ i <= t.rating ? '★' : '☆' }}</span>
            </div>
            <p class="testimonial-text">"{{ t.text }}"</p>
            <div class="testimonial-author">
              <div class="author-avatar">{{ t.initials }}</div>
              <div class="author-info">
                <div class="author-name">{{ t.name }}</div>
                <div class="author-country">{{ t.country }}</div>
              </div>
            </div>
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
            <p>Get a free consultation with our patient care team within 24 hours</p>
          </div>
          <div class="cta-actions">
            <button class="btn btn-primary btn-large">Get Free Consultation</button>
            <button class="btn btn-secondary btn-large" @click="$router.push('/hospitals')">Browse Hospitals</button>
          </div>
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
    reviews: 2341,
    image: 'https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?w=600',
    departments: ['Cardiology', 'Neurology', 'Oncology', 'Orthopedics'],
    languages: ['English', 'Chinese', 'Japanese'],
    accreditation: 'JCI'
  },
  {
    id: 2,
    name: 'Shanghai First People\'s Hospital',
    location: 'Shanghai, China',
    rating: 4.8,
    reviews: 1892,
    image: 'https://images.unsplash.com/photo-1586773860418-d37222d8fce3?w=600',
    departments: ['Cardiology', 'Orthopedics', 'TCM', 'Dermatology'],
    languages: ['English', 'Chinese', 'Korean'],
    accreditation: 'JCI'
  },
  {
    id: 3,
    name: 'Guangdong Provincial People\'s Hospital',
    location: 'Guangzhou, China',
    rating: 4.7,
    reviews: 1567,
    image: 'https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=600',
    departments: ['Oncology', 'Cardiology', 'Reproductive', 'Pediatrics'],
    languages: ['English', 'Chinese', 'Russian'],
    accreditation: 'JCI'
  }
])

const departments = ref([
  { id: 1, name: 'Cardiology', icon: '❤️', hospitals: 85 },
  { id: 2, name: 'Orthopedics', icon: '🦴', hospitals: 72 },
  { id: 3, name: 'Neurology', icon: '🧠', hospitals: 68 },
  { id: 4, name: 'Oncology', icon: '🎗️', hospitals: 54 },
  { id: 5, name: 'TCM', icon: '🌿', hospitals: 48 },
  { id: 6, name: 'Dermatology', icon: '🩺', hospitals: 42 },
  { id: 7, name: 'Reproductive', icon: '👶', hospitals: 38 },
  { id: 8, name: 'Ophthalmology', icon: '👁️', hospitals: 35 }
])

const testimonials = ref([
  {
    id: 1,
    name: 'Alexei Petrov',
    country: 'Russia',
    initials: 'AP',
    rating: 5,
    text: 'Exceptional service from start to finish. The medical team at Peking Union was outstanding.'
  },
  {
    id: 2,
    name: 'Yuki Tanaka',
    country: 'Japan',
    initials: 'YT',
    rating: 5,
    text: 'Professional translation service made everything so easy. Highly recommend ChinaMedCare!'
  },
  {
    id: 3,
    name: 'Sarah Johnson',
    country: 'USA',
    initials: 'SJ',
    rating: 4,
    text: 'Saved 60% on my procedure compared to US prices. The quality was just as good, if not better.'
  }
])

const searchByDept = (dept) => {
  router.push({ path: '/hospitals', query: { department: dept } })
}

const selectDepartment = (dept) => {
  router.push({ path: '/hospitals', query: { department: dept.name } })
}
</script>

<style scoped>
/* Trust Banner */
.trust-banner {
  background: #0f172a;
  color: white;
  padding: 12px 0;
  border-bottom: 1px solid #1e293b;
}

.trust-items {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 40px;
}

.trust-item {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 13px;
  color: #cbd5e1;
}

.trust-icon {
  width: 16px;
  height: 16px;
  color: #22c55e;
}

/* Hero */
.hero {
  position: relative;
  padding: 60px 0 80px;
  min-height: 580px;
  display: flex;
  align-items: center;
}

.hero-background {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: url('https://images.unsplash.com/photo-1576091160550-2173dba999ef?w=1600') center/cover;
  z-index: -2;
}

.hero-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(135deg, rgba(15, 23, 42, 0.85) 0%, rgba(30, 64, 175, 0.75) 100%);
  z-index: -1;
}

.hero-content {
  text-align: center;
  max-width: 900px;
  margin: 0 auto;
}

.hero-title {
  font-size: 48px;
  font-weight: 800;
  line-height: 1.1;
  color: white;
  margin-bottom: 16px;
  letter-spacing: -0.02em;
}

.title-accent {
  color: #60a5fa;
}

.hero-subtitle {
  font-size: 18px;
  color: rgba(255, 255, 255, 0.85);
  margin-bottom: 32px;
  line-height: 1.6;
}

/* Search Box */
.search-box {
  background: white;
  border-radius: 16px;
  padding: 8px;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.2);
  margin-bottom: 40px;
}

.search-row {
  display: flex;
  gap: 8px;
}

.search-input-wrapper {
  flex: 1;
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 16px;
  background: #f8fafc;
  border-radius: 12px;
}

.search-icon {
  width: 20px;
  height: 20px;
  color: #64748b;
  flex-shrink: 0;
}

.search-input {
  flex: 1;
  border: none;
  background: transparent;
  font-size: 16px;
  outline: none;
  color: #1e293b;
}

.search-input::placeholder {
  color: #94a3b8;
}

.search-btn {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 12px 28px;
  background: linear-gradient(135deg, #2563eb 0%, #1e40af 100%);
  color: white;
  border: none;
  border-radius: 12px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
}

.search-btn:hover {
  transform: translateY(-1px);
  box-shadow: 0 8px 20px rgba(37, 99, 235, 0.4);
}

.search-btn svg {
  width: 18px;
  height: 18px;
}

.search-quick {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 8px 4px;
  flex-wrap: wrap;
}

.quick-label {
  font-size: 13px;
  color: #64748b;
  font-weight: 500;
}

.quick-tag {
  padding: 6px 12px;
  background: #f1f5f9;
  border: none;
  border-radius: 100px;
  font-size: 13px;
  color: #475569;
  cursor: pointer;
  transition: all 0.2s ease;
}

.quick-tag:hover {
  background: #e2e8f0;
  color: #1e293b;
}

/* Hero Stats */
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
  font-size: 28px;
  font-weight: 800;
  color: white;
  margin-bottom: 2px;
}

.stat-label {
  font-size: 13px;
  color: rgba(255, 255, 255, 0.7);
}

/* Section */
.section-header {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  margin-bottom: 40px;
}

.section-header.centered {
  flex-direction: column;
  align-items: center;
  text-align: center;
}

.section-header-left {
  flex: 1;
}

.section-subtitle {
  font-size: 13px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: #2563eb;
  margin-bottom: 8px;
}

.section-title {
  font-size: 32px;
  font-weight: 800;
  color: #1e293b;
  margin-bottom: 0;
  line-height: 1.2;
}

.btn-link {
  display: flex;
  align-items: center;
  gap: 6px;
  background: transparent;
  border: none;
  color: #2563eb;
  font-size: 15px;
  font-weight: 600;
  cursor: pointer;
  transition: gap 0.2s ease;
}

.btn-link:hover {
  gap: 10px;
}

.btn-link svg {
  width: 18px;
  height: 18px;
}

/* Hospital Grid */
.hospital-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
}

/* Specialty Grid */
.specialty-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
}

.specialty-card {
  background: white;
  padding: 20px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  gap: 16px;
  cursor: pointer;
  transition: all 0.2s ease;
  border: 1px solid #e2e8f0;
}

.specialty-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08);
  border-color: #cbd5e1;
}

.specialty-icon {
  font-size: 32px;
}

.specialty-info {
  flex: 1;
}

.specialty-info h3 {
  font-size: 15px;
  font-weight: 700;
  color: #1e293b;
  margin-bottom: 2px;
}

.specialty-info p {
  font-size: 13px;
  color: #64748b;
  margin: 0;
}

.specialty-arrow {
  width: 20px;
  height: 20px;
  color: #94a3b8;
  transition: all 0.2s ease;
}

.specialty-card:hover .specialty-arrow {
  transform: translateX(4px);
  color: #2563eb;
}

/* Features */
.features-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 24px;
}

.feature-card {
  text-align: center;
  padding: 12px;
}

.feature-icon-wrapper {
  width: 64px;
  height: 64px;
  background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%);
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 20px;
  color: #2563eb;
}

.feature-icon-wrapper svg {
  width: 32px;
  height: 32px;
}

.feature-card h3 {
  font-size: 18px;
  font-weight: 700;
  color: #1e293b;
  margin-bottom: 8px;
}

.feature-card p {
  font-size: 14px;
  color: #64748b;
  line-height: 1.6;
  margin: 0;
}

/* Testimonials */
.testimonial-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
}

.testimonial-card {
  background: white;
  padding: 28px;
  border-radius: 16px;
  border: 1px solid #e2e8f0;
}

.testimonial-rating {
  color: #f59e0b;
  font-size: 16px;
  margin-bottom: 16px;
}

.testimonial-text {
  font-size: 15px;
  line-height: 1.7;
  color: #475569;
  margin-bottom: 24px;
}

.testimonial-author {
  display: flex;
  align-items: center;
  gap: 12px;
}

.author-avatar {
  width: 44px;
  height: 44px;
  background: linear-gradient(135deg, #2563eb 0%, #1e40af 100%);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: 700;
  font-size: 15px;
}

.author-name {
  font-size: 15px;
  font-weight: 700;
  color: #1e293b;
}

.author-country {
  font-size: 13px;
  color: #64748b;
}

/* CTA */
.cta-section {
  padding: 80px 0;
}

.cta-card {
  background: linear-gradient(135deg, #2563eb 0%, #1e40af 100%);
  border-radius: 20px;
  padding: 48px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 40px;
  box-shadow: 0 20px 40px rgba(37, 99, 235, 0.3);
}

.cta-content h2 {
  color: white;
  font-size: 28px;
  font-weight: 800;
  margin-bottom: 8px;
}

.cta-content p {
  color: rgba(255, 255, 255, 0.85);
  font-size: 16px;
  margin: 0;
}

.cta-actions {
  display: flex;
  gap: 12px;
  flex-shrink: 0;
}

.cta-card .btn-primary {
  background: white;
  color: #2563eb;
}

.cta-card .btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
}

.cta-card .btn-secondary {
  background: rgba(255, 255, 255, 0.1);
  color: white;
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.cta-card .btn-secondary:hover {
  background: rgba(255, 255, 255, 0.15);
}

/* Responsive Styles */
@media (max-width: 992px) {
  .trust-items {
    gap: 24px;
    flex-wrap: wrap;
  }

  .hospital-grid {
    grid-template-columns: repeat(2, 1fr);
  }

  .specialty-grid {
    grid-template-columns: repeat(2, 1fr);
  }

  .features-grid {
    grid-template-columns: repeat(2, 1fr);
  }

  .testimonial-grid {
    grid-template-columns: repeat(2, 1fr);
  }

  .cta-card {
    flex-direction: column;
    text-align: center;
    gap: 24px;
  }

  .cta-actions {
    width: 100%;
    justify-content: center;
  }
}

@media (max-width: 768px) {
  .trust-banner {
    padding: 16px 0;
  }

  .trust-items {
    gap: 12px 20px;
  }

  .trust-item {
    font-size: 12px;
  }

  .hero {
    padding: 48px 0 60px;
    min-height: auto;
  }

  .hero-title {
    font-size: 36px;
  }

  .hero-subtitle {
    font-size: 16px;
  }

  .search-row {
    flex-direction: column;
  }

  .search-btn {
    width: 100%;
    justify-content: center;
  }

  .hero-stats {
    gap: 24px;
    flex-wrap: wrap;
  }

  .stat-number {
    font-size: 24px;
  }

  .section-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 16px;
  }

  .section-header.centered {
    align-items: center;
  }

  .hospital-grid {
    grid-template-columns: 1fr;
  }

  .testimonial-grid {
    grid-template-columns: 1fr;
  }

  .cta-section {
    padding: 48px 0;
  }

  .cta-card {
    padding: 32px 24px;
  }

  .cta-content h2 {
    font-size: 24px;
  }

  .cta-actions {
    flex-direction: column;
  }

  .cta-actions .btn {
    width: 100%;
  }
}

@media (max-width: 576px) {
  .trust-items {
    justify-content: space-between;
  }

  .trust-item {
    gap: 6px;
  }

  .trust-icon {
    width: 14px;
    height: 14px;
  }

  .hero-title {
    font-size: 28px;
  }

  .hero-subtitle {
    font-size: 15px;
  }

  .search-box {
    padding: 12px;
  }

  .search-quick {
    gap: 8px;
  }

  .quick-label {
    width: 100%;
  }

  .section-title {
    font-size: 24px;
  }

  .specialty-grid {
    grid-template-columns: 1fr;
  }

  .features-grid {
    grid-template-columns: 1fr;
  }

  .hero-stats {
    gap: 16px 32px;
    justify-content: space-between;
  }
}
</style>
