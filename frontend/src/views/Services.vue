<template>
  <div class="services">
    <div class="container">
      <h1 class="page-title">{{ t('services.title') }}</h1>

      <div class="service-cards">
        <div v-for="service in services" :key="service.id" class="service-card-large">
          <div class="service-icon">{{ service.icon }}</div>
          <h2>{{ service.title }}</h2>
          <p>{{ service.desc }}</p>
          <el-button type="primary" size="large">{{ service.cta }}</el-button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useI18n } from 'vue-i18n'

const { t } = useI18n()

const services = [
  {
    id: 1,
    icon: '📅',
    title: t('services.appointmentBooking'),
    desc: t('services.appointmentBookingDesc'),
    cta: 'Book Appointment'
  },
  {
    id: 2,
    icon: '📄',
    title: t('services.medicalTranslation'),
    desc: t('services.medicalTranslationDesc'),
    cta: 'Upload Documents'
  },
  {
    id: 3,
    icon: '🧑‍⚕️',
    title: t('services.escortService'),
    desc: t('services.escortServiceDesc'),
    cta: 'Find Escort'
  },
  {
    id: 4,
    icon: '✈️',
    title: t('services.visaAssistance'),
    desc: t('services.visaAssistanceDesc'),
    cta: 'Learn More'
  }
]
</script>

<style scoped>
.services {
  padding: 60px 0;
}
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}
.page-title {
  font-size: 36px;
  text-align: center;
  margin-bottom: 60px;
  color: #333;
}
.service-cards {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 32px;
}
.service-card-large {
  background: #fff;
  padding: 48px;
  border-radius: 16px;
  box-shadow: 0 4px 16px rgba(0,0,0,0.08);
  text-align: center;
}
.service-icon {
  font-size: 64px;
  margin-bottom: 24px;
}
.service-card-large h2 {
  font-size: 24px;
  margin-bottom: 16px;
  color: #333;
}
.service-card-large p {
  color: #666;
  margin-bottom: 32px;
  font-size: 16px;
}
</style>
