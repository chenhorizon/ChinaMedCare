<template>
  <header class="header">
    <div class="container">
      <div class="header-content">
        <router-link to="/" class="logo">
          <svg class="logo-icon" viewBox="0 0 32 32" fill="none">
            <rect x="2" y="2" width="28" height="28" rx="8" fill="url(#grad1)"/>
            <path d="M10 10h12v12H10z" fill="white" opacity="0.9"/>
            <path d="M15 10v12M10 16h12" stroke="#2563eb" stroke-width="2" stroke-linecap="round"/>
            <defs>
              <linearGradient id="grad1" x1="2" y1="2" x2="30" y2="30">
                <stop stop-color="#2563eb"/>
                <stop offset="1" stop-color="#1e40af"/>
              </linearGradient>
            </defs>
          </svg>
          <span class="logo-text">ChinaMed<span class="logo-text-accent">Care</span></span>
        </router-link>

        <nav class="nav">
          <router-link v-for="item in navItems" :key="item.key" :to="item.path" class="nav-link" :class="{ active: $route.path === item.path }">
            {{ t(item.key) }}
          </router-link>
        </nav>

        <div class="header-actions">
          <div class="lang-switcher">
            <button v-for="lang in languages" :key="lang.code" class="lang-btn" :class="{ active: currentLocale === lang.code }" @click="changeLocale(lang.code)">
              {{ lang.flag }}
            </button>
          </div>

          <div class="auth-buttons">
            <button class="btn-text">{{ t('nav.login') }}</button>
            <button class="btn btn-primary btn-small">{{ t('nav.signup') }}</button>
          </div>
        </div>
      </div>
    </div>
  </header>
</template>

<script setup>
import { ref } from 'vue'
import { useI18n } from 'vue-i18n'

const { t, locale } = useI18n()
const currentLocale = ref(locale.value)

const navItems = [
  { key: 'nav.home', path: '/' },
  { key: 'nav.hospitals', path: '/hospitals' },
  { key: 'nav.doctors', path: '/doctors' },
  { key: 'nav.services', path: '/services' },
  { key: 'nav.about', path: '/about' }
]

const languages = [
  { code: 'en', flag: '🇺🇸' },
  { code: 'zh', flag: '🇨🇳' },
  { code: 'ru', flag: '🇷🇺' },
  { code: 'ja', flag: '🇯🇵' },
  { code: 'ko', flag: '🇰🇷' }
]

const changeLocale = (val) => {
  currentLocale.value = val
  locale.value = val
}
</script>

<style scoped>
.header {
  background: var(--bg-primary);
  border-bottom: 1px solid var(--border);
  position: sticky;
  top: 0;
  z-index: 1000;
  backdrop-filter: blur(8px);
  background: rgba(255, 255, 255, 0.95);
}

.header-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 72px;
}

.logo {
  display: flex;
  align-items: center;
  gap: 12px;
  text-decoration: none;
  font-size: 20px;
  font-weight: 700;
  color: var(--text-primary);
}

.logo-icon {
  width: 36px;
  height: 36px;
}

.logo-text-accent {
  color: var(--primary);
}

.nav {
  display: flex;
  gap: 8px;
}

.nav-link {
  padding: 10px 16px;
  text-decoration: none;
  color: var(--text-secondary);
  font-size: 14px;
  font-weight: 500;
  border-radius: var(--radius-md);
  transition: all 0.2s ease;
}

.nav-link:hover {
  color: var(--text-primary);
  background: var(--bg-secondary);
}

.nav-link.active {
  color: var(--primary);
  background: var(--primary-light);
}

.header-actions {
  display: flex;
  align-items: center;
  gap: 20px;
}

.lang-switcher {
  display: flex;
  background: var(--bg-secondary);
  padding: 4px;
  border-radius: var(--radius-md);
}

.lang-btn {
  width: 36px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 16px;
  border: none;
  background: transparent;
  border-radius: var(--radius-sm);
  cursor: pointer;
  transition: all 0.2s ease;
}

.lang-btn:hover {
  background: var(--bg-tertiary);
}

.lang-btn.active {
  background: var(--bg-primary);
  box-shadow: var(--shadow-sm);
}

.auth-buttons {
  display: flex;
  align-items: center;
  gap: 12px;
}

.btn-text {
  background: transparent;
  color: var(--text-secondary);
  font-size: 14px;
  font-weight: 500;
  padding: 8px 12px;
  border-radius: var(--radius-md);
  transition: all 0.2s ease;
}

.btn-text:hover {
  color: var(--text-primary);
  background: var(--bg-secondary);
}

.btn-small {
  padding: 8px 16px;
  font-size: 14px;
}
</style>
