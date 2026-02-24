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

        <nav class="nav d-none-md">
          <router-link v-for="item in navItems" :key="item.key" :to="item.path" class="nav-link" :class="{ active: $route.path === item.path }">
            {{ t(item.key) }}
          </router-link>
        </nav>

        <div class="header-actions d-none-md">
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

        <button class="hamburger-btn d-block-md" @click="toggleMenu" aria-label="Toggle menu">
          <svg v-if="!menuOpen" class="hamburger-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path stroke-linecap="round" stroke-linejoin="round" d="M4 6h16M4 12h16M4 18h16"/>
          </svg>
          <svg v-else class="hamburger-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12"/>
          </svg>
        </button>
      </div>
    </div>

    <div class="mobile-menu-overlay" :class="{ active: menuOpen }" @click="closeMenu"></div>

    <div class="mobile-menu" :class="{ active: menuOpen }">
      <div class="mobile-menu-header">
        <div class="logo">
          <svg class="logo-icon" viewBox="0 0 32 32" fill="none">
            <rect x="2" y="2" width="28" height="28" rx="8" fill="url(#grad2)"/>
            <path d="M10 10h12v12H10z" fill="white" opacity="0.9"/>
            <path d="M15 10v12M10 16h12" stroke="#2563eb" stroke-width="2" stroke-linecap="round"/>
            <defs>
              <linearGradient id="grad2" x1="2" y1="2" x2="30" y2="30">
                <stop stop-color="#2563eb"/>
                <stop offset="1" stop-color="#1e40af"/>
              </linearGradient>
            </defs>
          </svg>
        </div>
        <button class="close-menu-btn" @click="closeMenu" aria-label="Close menu">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12"/>
          </svg>
        </button>
      </div>

      <nav class="mobile-nav">
        <router-link v-for="item in navItems" :key="item.key" :to="item.path" class="mobile-nav-link" :class="{ active: $route.path === item.path }" @click="closeMenu">
          {{ t(item.key) }}
        </router-link>
      </nav>

      <div class="mobile-lang-switcher">
        <span class="lang-label">Language / 语言</span>
        <div class="lang-buttons">
          <button v-for="lang in languages" :key="lang.code" class="mobile-lang-btn" :class="{ active: currentLocale === lang.code }" @click="changeLocale(lang.code)">
            {{ lang.flag }} {{ lang.name }}
          </button>
        </div>
      </div>

      <div class="mobile-auth-buttons">
        <button class="btn btn-secondary btn-full">{{ t('nav.login') }}</button>
        <button class="btn btn-primary btn-full">{{ t('nav.signup') }}</button>
      </div>
    </div>
  </header>
</template>

<script setup>
import { ref } from 'vue'
import { useI18n } from 'vue-i18n'

const { t, locale } = useI18n()
const currentLocale = ref(locale.value)
const menuOpen = ref(false)

const navItems = [
  { key: 'nav.home', path: '/' },
  { key: 'nav.hospitals', path: '/hospitals' },
  { key: 'nav.doctors', path: '/doctors' },
  { key: 'nav.services', path: '/services' },
  { key: 'nav.about', path: '/about' }
]

const languages = [
  { code: 'en', flag: '🇺🇸', name: 'English' },
  { code: 'zh', flag: '🇨🇳', name: '中文' },
  { code: 'ru', flag: '🇷🇺', name: 'Русский' },
  { code: 'ja', flag: '🇯🇵', name: '日本語' },
  { code: 'ko', flag: '🇰🇷', name: '한국어' }
]

const changeLocale = (val) => {
  currentLocale.value = val
  locale.value = val
}

const toggleMenu = () => {
  menuOpen.value = !menuOpen.value
  if (menuOpen.value) {
    document.body.style.overflow = 'hidden'
  } else {
    document.body.style.overflow = ''
  }
}

const closeMenu = () => {
  menuOpen.value = false
  document.body.style.overflow = ''
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

/* Hamburger Button */
.hamburger-btn {
  display: none;
  width: 40px;
  height: 40px;
  border-radius: 10px;
  border: none;
  background: var(--bg-secondary);
  cursor: pointer;
  align-items: center;
  justify-content: center;
  color: var(--text-primary);
  transition: all 0.2s ease;
}

.hamburger-btn:hover {
  background: var(--bg-tertiary);
}

.hamburger-icon {
  width: 24px;
  height: 24px;
}

/* Mobile Menu Overlay */
.mobile-menu-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  opacity: 0;
  visibility: hidden;
  transition: all 0.3s ease;
  z-index: 1001;
}

.mobile-menu-overlay.active {
  opacity: 1;
  visibility: visible;
}

/* Mobile Menu Sidebar */
.mobile-menu {
  position: fixed;
  top: 0;
  right: 0;
  width: 300px;
  max-width: 85vw;
  height: 100vh;
  background: white;
  transform: translateX(100%);
  transition: transform 0.3s ease;
  z-index: 1002;
  display: flex;
  flex-direction: column;
  overflow-y: auto;
}

.mobile-menu.active {
  transform: translateX(0);
}

.mobile-menu-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 16px 20px;
  border-bottom: 1px solid var(--border);
}

.mobile-menu-header .logo-icon {
  width: 32px;
  height: 32px;
}

.close-menu-btn {
  width: 36px;
  height: 36px;
  border-radius: 8px;
  border: none;
  background: var(--bg-secondary);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--text-primary);
  transition: all 0.2s ease;
}

.close-menu-btn:hover {
  background: var(--bg-tertiary);
}

.close-menu-btn svg {
  width: 20px;
  height: 20px;
}

.mobile-nav {
  flex: 1;
  padding: 16px 0;
}

.mobile-nav-link {
  display: block;
  padding: 14px 20px;
  text-decoration: none;
  color: var(--text-primary);
  font-size: 16px;
  font-weight: 500;
  border-left: 3px solid transparent;
  transition: all 0.2s ease;
}

.mobile-nav-link:hover {
  background: var(--bg-secondary);
}

.mobile-nav-link.active {
  color: var(--primary);
  background: var(--primary-light);
  border-left-color: var(--primary);
}

.mobile-lang-switcher {
  padding: 20px;
  border-top: 1px solid var(--border);
}

.lang-label {
  font-size: 12px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--text-muted);
  margin-bottom: 12px;
  display: block;
}

.lang-buttons {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 8px;
}

.mobile-lang-btn {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 10px 12px;
  border-radius: 10px;
  border: 1px solid var(--border);
  background: white;
  font-size: 14px;
  cursor: pointer;
  transition: all 0.2s ease;
}

.mobile-lang-btn:hover {
  background: var(--bg-secondary);
  border-color: var(--border-dark);
}

.mobile-lang-btn.active {
  background: var(--primary-light);
  border-color: var(--primary);
  color: var(--primary);
}

.mobile-auth-buttons {
  padding: 20px;
  border-top: 1px solid var(--border);
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.btn-full {
  width: 100%;
}

/* Responsive - Show hamburger on tablets and mobile */
@media (max-width: 992px) {
  .header-actions {
    gap: 12px;
  }
}

@media (max-width: 768px) {
  .hamburger-btn {
    display: flex;
  }
  .header-content {
    height: 64px;
  }
  .logo-text {
    font-size: 18px;
  }
}
</style>
