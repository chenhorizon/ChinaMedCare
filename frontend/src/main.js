import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { createI18n } from 'vue-i18n'
import ElementPlus from 'element-plus'
import * as ElementPlusIconsVue from '@element-plus/icons-vue'
import 'element-plus/dist/index.css'
import App from './App.vue'
import router from './router'
import en from './locales/en.json'
import zh from './locales/zh.json'
import ru from './locales/ru.json'
import ja from './locales/ja.json'
import ko from './locales/ko.json'
import './assets/styles/main.css'

const messages = { en, zh, ru, ja, ko }

const i18n = createI18n({
  legacy: false,
  locale: 'en',
  fallbackLocale: 'en',
  messages
})

const app = createApp(App)
const pinia = createPinia()

// Register all Element Plus icons
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
  app.component(key, component)
}

app.use(pinia)
app.use(i18n)
app.use(router)
app.use(ElementPlus)
app.mount('#app')
