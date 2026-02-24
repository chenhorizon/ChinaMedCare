<template>
  <div class="hospital-list">
    <div class="container">
      <h1 class="page-title">{{ t('nav.hospitals') }}</h1>

      <div class="filters">
        <el-input v-model="searchQuery" :placeholder="t('common.search')" class="search-input" />
        <el-select v-model="selectedDept" placeholder="Department" clearable>
          <el-option label="All Departments" value="" />
          <el-option v-for="dept in departments" :key="dept" :label="dept" :value="dept" />
        </el-select>
        <el-select v-model="selectedCity" placeholder="City" clearable>
          <el-option label="All Cities" value="" />
          <el-option v-for="city in cities" :key="city" :label="city" :value="city" />
        </el-select>
      </div>

      <div class="hospital-grid">
        <HospitalCard v-for="hospital in filteredHospitals" :key="hospital.id" :hospital="hospital" />
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useI18n } from 'vue-i18n'
import HospitalCard from '@/components/HospitalCard.vue'

const { t } = useI18n()

const searchQuery = ref('')
const selectedDept = ref('')
const selectedCity = ref('')

const departments = ['Cardiology', 'Neurology', 'Oncology', 'Orthopedics', 'TCM', 'Dermatology', 'Reproductive']
const cities = ['Beijing', 'Shanghai', 'Guangzhou', 'Shenzhen', 'Chengdu']

const hospitals = ref([
  {
    id: 1,
    name: 'Peking Union Medical College Hospital',
    location: 'Beijing, China',
    rating: 4.9,
    image: 'https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?w=400',
    departments: ['Cardiology', 'Neurology', 'Oncology', 'Orthopedics'],
    languages: ['English', 'Chinese', 'Japanese']
  },
  {
    id: 2,
    name: 'Shanghai First People\'s Hospital',
    location: 'Shanghai, China',
    rating: 4.8,
    image: 'https://images.unsplash.com/photo-1586773860418-d37222d8fce3?w=400',
    departments: ['Cardiology', 'Orthopedics', 'TCM', 'Dermatology'],
    languages: ['English', 'Chinese', 'Korean']
  },
  {
    id: 3,
    name: 'Guangdong Provincial People\'s Hospital',
    location: 'Guangzhou, China',
    rating: 4.7,
    image: 'https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=400',
    departments: ['Oncology', 'Cardiology', 'Reproductive', 'Pediatrics'],
    languages: ['English', 'Chinese', 'Russian']
  }
])

const filteredHospitals = computed(() => {
  return hospitals.value.filter(h => {
    const matchesSearch = h.name.toLowerCase().includes(searchQuery.value.toLowerCase())
    const matchesDept = !selectedDept.value || h.departments.includes(selectedDept.value)
    const matchesCity = !selectedCity.value || h.location.includes(selectedCity.value)
    return matchesSearch && matchesDept && matchesCity
  })
})
</script>

<style scoped>
.hospital-list {
  padding: 40px 0;
}
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}
.page-title {
  font-size: 32px;
  margin-bottom: 32px;
  color: #333;
}
.filters {
  display: flex;
  gap: 16px;
  margin-bottom: 32px;
}
.search-input {
  flex: 1;
}
.hospital-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
}
</style>
