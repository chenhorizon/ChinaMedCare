<template>
  <div class="about">
    <div class="container">
      <h1 class="page-title">{{ t('nav.about') }}</h1>
      <div class="about-content">
        <h2>Our Mission</h2>
        <p>ChinaMedCare is dedicated to connecting international patients with world-class medical facilities in China.</p>
        <h2>Why Choose Us</h2>
        <ul>
          <li>Access to top-tier hospitals and specialists</li>
          <li>Multilingual support throughout your journey</li>
          <li>Seamless end-to-end service coordination</li>
          <li>Transparent pricing and cost estimates</li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useI18n } from 'vue-i18n'
const { t } = useI18n()
</script>

<style scoped>
.about {
  padding: 60px 0;
}
.container {
  max-width: 800px;
  margin: 0 auto;
  padding: 0 20px;
}
.page-title {
  font-size: 36px;
  text-align: center;
  margin-bottom: 48px;
}
.about-content h2 {
  margin-bottom: 16px;
  color: #333;
}
.about-content p,
.about-content li {
  color: #666;
  line-height: 1.8;
  margin-bottom: 16px;
}

/* Responsive Styles */
@media (max-width: 768px) {
  .about {
    padding: 40px 0;
  }

  .page-title {
    font-size: 28px;
    margin-bottom: 32px;
  }

  .about-content h2 {
    font-size: 20px;
  }
}

@media (max-width: 576px) {
  .page-title {
    font-size: 24px;
  }
}
</style>
