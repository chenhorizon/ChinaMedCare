<template>
  <div class="hospital-list">
    <div class="container">
      <h1 class="page-title">{{ t('nav.hospitals') }}</h1>

      <div class="filters">
        <el-select v-model="selectedDept" placeholder="Department" clearable @change="loadHospitals">
          <el-option label="All Departments" value="" />
          <el-option v-for="dept in departments" :key="dept" :label="dept" :value="dept" />
        </el-select>
        <el-select v-model="selectedCity" placeholder="City" clearable @change="loadHospitals">
          <el-option label="All Cities" value="" />
          <el-option v-for="city in cities" :key="city" :label="city" :value="city" />
        </el-select>
      </div>

      <div class="hospital-grid" v-loading="loading">
        <HospitalCard v-for="hospital in hospitals" :key="hospital.id" :hospital="hospital" />
      </div>

      <el-empty v-if="!loading && hospitals.length === 0" description="No hospitals found" />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useI18n } from 'vue-i18n'
import HospitalCard from '@/components/HospitalCard.vue'
import { hospitalApi } from '@/api/index'

const { t } = useI18n()

const loading = ref(false)
const hospitals = ref([])
const selectedDept = ref('')
const selectedCity = ref('')

const departments = ['Cardiology', 'Neurology', 'Oncology', 'Orthopedics', 'TCM', 'Dermatology', 'Reproductive']
const cities = ['Beijing', 'Shanghai', 'Guangzhou', 'Shenzhen', 'Chengdu']

async function loadHospitals() {
  loading.value = true
  try {
    const params = {}
    if (selectedDept.value) params.department = selectedDept.value
    if (selectedCity.value) params.city = selectedCity.value

    const response = await hospitalApi.getAll(params)
    hospitals.value = response.data || []
  } catch (error) {
    console.error('Failed to load hospitals:', error)
    hospitals.value = []
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  loadHospitals()
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
.hospital-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
}

/* Responsive Styles */
@media (max-width: 992px) {
  .hospital-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 768px) {
  .filters {
    flex-direction: column;
  }

  .hospital-grid {
    grid-template-columns: 1fr;
  }

  .page-title {
    font-size: 28px;
  }

  .hospital-list {
    padding: 24px 0;
  }
}

@media (max-width: 576px) {
  .page-title {
    font-size: 24px;
  }
}
</style>
