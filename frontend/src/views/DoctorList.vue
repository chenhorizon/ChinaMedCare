<template>
  <div class="doctor-list">
    <div class="container">
      <h1 class="page-title">{{ t('nav.doctors') }}</h1>
      <p class="page-desc">Coming soon...</p>
    </div>
  </div>
</template>

<script setup>
import { useI18n } from 'vue-i18n'
const { t } = useI18n()
</script>

<style scoped>
.doctor-list {
  padding: 80px 0;
  text-align: center;
}
.page-title {
  font-size: 32px;
  margin-bottom: 16px;
}
.page-desc {
  color: #888;
  font-size: 18px;
}
</style>
