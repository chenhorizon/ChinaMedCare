<template>
  <div class="hospital-list">
    <!-- Toolbar -->
    <el-card class="toolbar-card">
      <div class="toolbar">
        <div class="search-section">
          <el-input
            v-model="searchQuery"
            placeholder="Search hospitals..."
            clearable
            style="width: 300px"
            @keyup.enter="loadHospitals"
          >
            <template #prefix>
              <el-icon><Search /></el-icon>
            </template>
          </el-input>
          <el-button @click="loadHospitals">
            <el-icon><Search /></el-icon>
            Search
          </el-button>
          <el-button @click="resetFilters">
            <el-icon><Refresh /></el-icon>
            Reset
          </el-button>
        </div>
        <el-button type="primary" @click="openCreateDialog">
          <el-icon><Plus /></el-icon>
          Add Hospital
        </el-button>
      </div>
    </el-card>

    <!-- Hospital Table -->
    <el-card class="table-card">
      <el-table
        :data="hospitals"
        v-loading="loading"
        stripe
        style="width: 100%"
      >
        <el-table-column prop="id" label="ID" width="80" />
        <el-table-column prop="name" label="Hospital Name" min-width="200" />
        <el-table-column prop="location" label="Location" min-width="180" />
        <el-table-column prop="rating" label="Rating" width="100">
          <template #default="{ row }">
            <el-tag type="success">{{ row.rating }}</el-tag>
          </template>
        </el-table-column>
        <el-table-column prop="departments" label="Departments" min-width="200">
          <template #default="{ row }">
            <el-tag v-for="dept in row.departments.slice(0, 3)" :key="dept" size="small" style="margin-right: 4px; margin-bottom: 4px">
              {{ dept }}
            </el-tag>
            <span v-if="row.departments.length > 3">+{{ row.departments.length - 3 }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Languages" width="150">
          <template #default="{ row }">
            <el-tag v-for="lang in row.languages" :key="lang" size="small" type="info" style="margin-right: 4px; margin-bottom: 4px">
              {{ lang }}
            </el-tag>
          </template>
        </el-table-column>
        <el-table-column label="Actions" width="200" fixed="right">
          <template #default="{ row }">
            <el-button type="primary" size="small" link @click="openEditDialog(row)">
              <el-icon><Edit /></el-icon>
              Edit
            </el-button>
            <el-button type="danger" size="small" link @click="confirmDelete(row)">
              <el-icon><Delete /></el-icon>
              Delete
            </el-button>
          </template>
        </el-table-column>
      </el-table>

      <!-- Pagination -->
      <div class="pagination">
        <el-pagination
          v-model:current-page="currentPage"
          v-model:page-size="pageSize"
          :page-sizes="[10, 20, 50, 100]"
          :total="total"
          layout="total, sizes, prev, pager, next, jumper"
          @size-change="loadHospitals"
          @current-change="loadHospitals"
        />
      </div>
    </el-card>

    <!-- Create/Edit Dialog -->
    <el-dialog
      v-model="dialogVisible"
      :title="isEditing ? 'Edit Hospital' : 'Add Hospital'"
      width="600px"
      destroy-on-close
    >
      <el-form
        ref="formRef"
        :model="form"
        :rules="rules"
        label-width="120px"
      >
        <el-form-item label="Hospital Name" prop="name">
          <el-input v-model="form.name" placeholder="Enter hospital name" />
        </el-form-item>
        <el-form-item label="Location" prop="location">
          <el-input v-model="form.location" placeholder="City, Country" />
        </el-form-item>
        <el-form-item label="Rating" prop="rating">
          <el-input-number
            v-model="form.rating"
            :min="0"
            :max="5"
            :step="0.1"
            style="width: 100%"
          />
        </el-form-item>
        <el-form-item label="Image URL" prop="image">
          <el-input v-model="form.image" placeholder="https://..." />
        </el-form-item>
        <el-form-item label="Departments" prop="departments">
          <el-select
            v-model="form.departments"
            multiple
            filterable
            allow-create
            placeholder="Select or create departments"
            style="width: 100%"
          >
            <el-option
              v-for="dept in departmentOptions"
              :key="dept"
              :label="dept"
              :value="dept"
            />
          </el-select>
        </el-form-item>
        <el-form-item label="Languages" prop="languages">
          <el-select
            v-model="form.languages"
            multiple
            filterable
            allow-create
            placeholder="Select or create languages"
            style="width: 100%"
          >
            <el-option
              v-for="lang in languageOptions"
              :key="lang"
              :label="lang"
              :value="lang"
            />
          </el-select>
        </el-form-item>
      </el-form>
      <template #footer>
        <el-button @click="dialogVisible = false">Cancel</el-button>
        <el-button type="primary" :loading="saving" @click="saveHospital">
          Save
        </el-button>
      </template>
    </el-dialog>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted } from 'vue'
import { ElMessage, ElMessageBox } from 'element-plus'
import { Search, Refresh, Plus, Edit, Delete } from '@element-plus/icons-vue'
import { hospitalAdminApi } from '@/api/admin'

const loading = ref(false)
const saving = ref(false)
const hospitals = ref([])
const total = ref(0)
const currentPage = ref(1)
const pageSize = ref(10)
const searchQuery = ref('')

const dialogVisible = ref(false)
const isEditing = ref(false)
const formRef = ref(null)

const departmentOptions = [
  'Cardiology', 'Neurology', 'Oncology', 'Orthopedics',
  'TCM', 'Dermatology', 'Reproductive', 'Pediatrics'
]

const languageOptions = [
  'English', 'Chinese', 'Japanese', 'Korean', 'Russian'
]

const form = reactive({
  id: null,
  name: '',
  location: '',
  rating: 4.5,
  image: '',
  departments: [],
  languages: []
})

const rules = {
  name: [{ required: true, message: 'Please enter hospital name', trigger: 'blur' }],
  location: [{ required: true, message: 'Please enter location', trigger: 'blur' }],
  rating: [{ required: true, message: 'Please enter rating', trigger: 'blur' }],
  image: [{ required: true, message: 'Please enter image URL', trigger: 'blur' }]
}

async function loadHospitals() {
  loading.value = true
  try {
    const params = {
      page: currentPage.value,
      page_size: pageSize.value
    }
    if (searchQuery.value) {
      params.search = searchQuery.value
    }

    const response = await hospitalAdminApi.getAll(params)
    hospitals.value = response.data.items
    total.value = response.data.total
  } catch (error) {
    ElMessage.error('Failed to load hospitals')
    console.error(error)
  } finally {
    loading.value = false
  }
}

function resetFilters() {
  searchQuery.value = ''
  currentPage.value = 1
  loadHospitals()
}

function openCreateDialog() {
  isEditing.value = false
  Object.assign(form, {
    id: null,
    name: '',
    location: '',
    rating: 4.5,
    image: 'https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?w=400',
    departments: [],
    languages: []
  })
  dialogVisible.value = true
}

function openEditDialog(hospital) {
  isEditing.value = true
  Object.assign(form, { ...hospital })
  dialogVisible.value = true
}

async function saveHospital() {
  if (!formRef.value) return

  await formRef.value.validate(async (valid) => {
    if (!valid) return

    saving.value = true
    try {
      if (isEditing.value) {
        await hospitalAdminApi.update(form.id, form)
        ElMessage.success('Hospital updated successfully')
      } else {
        await hospitalAdminApi.create(form)
        ElMessage.success('Hospital created successfully')
      }
      dialogVisible.value = false
      loadHospitals()
    } catch (error) {
      ElMessage.error(isEditing.value ? 'Failed to update hospital' : 'Failed to create hospital')
      console.error(error)
    } finally {
      saving.value = false
    }
  })
}

function confirmDelete(hospital) {
  ElMessageBox.confirm(
    `Are you sure you want to delete "${hospital.name}"?`,
    'Confirm Delete',
    {
      confirmButtonText: 'Delete',
      cancelButtonText: 'Cancel',
      type: 'warning'
    }
  ).then(async () => {
    try {
      await hospitalAdminApi.delete(hospital.id)
      ElMessage.success('Hospital deleted successfully')
      loadHospitals()
    } catch (error) {
      ElMessage.error('Failed to delete hospital')
      console.error(error)
    }
  }).catch(() => {})
}

onMounted(() => {
  loadHospitals()
})
</script>

<style scoped>
.hospital-list {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.toolbar-card,
.table-card {
  margin-bottom: 0;
}

.toolbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 16px;
}

.search-section {
  display: flex;
  align-items: center;
  gap: 12px;
}

.pagination {
  display: flex;
  justify-content: flex-end;
  margin-top: 20px;
}
</style>
