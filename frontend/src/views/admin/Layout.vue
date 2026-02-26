<template>
  <div class="admin-layout">
    <el-container>
      <!-- Sidebar -->
      <el-aside width="240px" class="sidebar">
        <div class="logo">
          <h2>ChinaMedCare</h2>
          <p class="logo-subtitle">Admin MIS</p>
        </div>

        <el-menu
          :default-active="activeMenu"
          class="sidebar-menu"
          router
        >
          <el-menu-item index="/admin/hospitals">
            <el-icon><Hospital /></el-icon>
            <span>Hospital Management</span>
          </el-menu-item>
        </el-menu>
      </el-aside>

      <!-- Main Content -->
      <el-container class="main-container">
        <!-- Header -->
        <el-header class="header">
          <div class="header-left">
            <h3>{{ pageTitle }}</h3>
          </div>
          <div class="header-right">
            <el-dropdown @command="handleCommand">
              <span class="user-info">
                <el-icon><User /></el-icon>
                <span>Admin</span>
              </span>
              <template #dropdown>
                <el-dropdown-menu>
                  <el-dropdown-item command="logout">
                    <el-icon><SwitchButton /></el-icon>
                    Logout
                  </el-dropdown-item>
                </el-dropdown-menu>
              </template>
            </el-dropdown>
          </div>
        </el-header>

        <!-- Page Content -->
        <el-main class="main-content">
          <router-view />
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { ElMessageBox, ElMessage } from 'element-plus'
import { useAuthStore } from '@/stores/auth'

const router = useRouter()
const route = useRoute()
const authStore = useAuthStore()

const activeMenu = computed(() => route.path)

const pageTitle = computed(() => {
  if (route.path.includes('hospitals')) {
    return 'Hospital Management'
  }
  return 'Dashboard'
})

function handleCommand(command) {
  if (command === 'logout') {
    ElMessageBox.confirm('Are you sure you want to logout?', 'Confirm', {
      confirmButtonText: 'Yes',
      cancelButtonText: 'No',
      type: 'warning'
    }).then(() => {
      authStore.logout()
      ElMessage.success('Logged out successfully')
      router.push('/admin/login')
    }).catch(() => {})
  }
}
</script>

<style scoped>
.admin-layout {
  height: 100vh;
}

.sidebar {
  background: #001529;
  color: white;
  overflow-x: hidden;
}

.logo {
  padding: 24px 20px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.logo h2 {
  margin: 0;
  font-size: 20px;
  color: white;
}

.logo-subtitle {
  margin: 4px 0 0 0;
  font-size: 12px;
  color: rgba(255, 255, 255, 0.6);
}

.sidebar-menu {
  border: none;
  background: #001529;
}

.sidebar-menu:not(.el-menu--collapse) {
  width: 240px;
}

.main-container {
  background: #f0f2f5;
}

.header {
  background: white;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 24px;
  box-shadow: 0 1px 4px rgba(0, 0, 0, 0.08);
}

.header-left h3 {
  margin: 0;
  font-size: 18px;
  color: #333;
}

.header-right {
  display: flex;
  align-items: center;
}

.user-info {
  display: flex;
  align-items: center;
  gap: 8px;
  cursor: pointer;
  color: #666;
  font-size: 14px;
}

.user-info:hover {
  color: #409eff;
}

.main-content {
  padding: 24px;
  overflow-y: auto;
}
</style>
