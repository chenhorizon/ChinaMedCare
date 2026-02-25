# 医院管理后台方案

## 概述

本方案为 ChinaMedCare 项目添加医院管理后台功能，支持医院数据的增删改查（CRUD）。

---

## 技术架构

### 整体架构图

```
┌─────────────────────────────────────────────────────────┐
│                     前端 (Vue.js 3)                      │
├──────────────────────┬──────────────────────────────────┤
│  公开页面            │     管理后台                      │
│  - HospitalList      │     - /admin/login               │
│  - HospitalDetail    │     - /admin/dashboard           │
│  - Home, etc.        │     - /admin/hospitals (CRUD)   │
└──────────────────────┴──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────┐
│              后端 (FastAPI)                              │
├─────────────────────────────────────────────────────────┤
│  - Auth API (登录/JWT)                                   │
│  - Hospital CRUD API                                     │
│  - 数据库 (PostgreSQL)                                   │
└─────────────────────────────────────────────────────────┘
```

---

## 功能模块

### 1. 认证模块

**功能**：
- 管理员登录
- JWT Token 认证
- Token 刷新
- 退出登录

**API 端点**：
```
POST /api/admin/login          # 管理员登录
POST /api/admin/refresh        # 刷新 Token
POST /api/admin/logout         # 退出登录
```

### 2. 医院管理模块

**功能**：
- 医院列表（分页、搜索、筛选）
- 新增医院
- 编辑医院
- 删除医院
- 查看医院详情

**API 端点**：
```
GET    /api/admin/hospitals          # 获取医院列表（分页）
GET    /api/admin/hospitals/{id}     # 获取单个医院
POST   /api/admin/hospitals          # 创建医院
PUT    /api/admin/hospitals/{id}     # 更新医院
DELETE /api/admin/hospitals/{id}     # 删除医院
```

---

## 后端实现方案

### 目录结构

```
backend/app/
├── api/
│   ├── admin/
│   │   ├── __init__.py
│   │   ├── auth.py           # 认证 API
│   │   └── hospitals.py      # 医院管理 CRUD API
│   ├── hospitals.py          # 公开医院 API（保持不变）
│   ├── doctors.py
│   └── bookings.py
├── core/
│   ├── __init__.py
│   ├── config.py             # 配置（JWT密钥等）
│   ├── security.py           # 密码哈希、JWT 工具
│   └── dependencies.py       # FastAPI 依赖（获取当前用户）
├── models/
│   ├── __init__.py
│   ├── hospital.py           # 医院 Pydantic 模型
│   └── admin.py              # 管理员 Pydantic 模型
├── services/
│   ├── __init__.py
│   ├── hospital_service.py   # 医院业务逻辑
│   └── auth_service.py       # 认证业务逻辑
└── db/
    ├── __init__.py
    └── mock_db.py            # 模拟数据库（后期可替换为 SQLAlchemy）
```

### 数据模型

#### 医院模型 (Pydantic)

```python
from pydantic import BaseModel
from typing import List, Optional

class HospitalBase(BaseModel):
    name: str
    location: str
    rating: float
    image: str
    departments: List[str]
    languages: List[str]

class HospitalCreate(HospitalBase):
    pass

class HospitalUpdate(HospitalBase):
    name: Optional[str] = None
    location: Optional[str] = None
    rating: Optional[float] = None
    image: Optional[str] = None
    departments: Optional[List[str]] = None
    languages: Optional[List[str]] = None

class Hospital(HospitalBase):
    id: int

    class Config:
        from_attributes = True
```

#### 分页响应

```python
class PaginatedResponse(BaseModel):
    items: List[Hospital]
    total: int
    page: int
    page_size: int
    total_pages: int
```

---

## 前端实现方案

### 目录结构

```
frontend/src/
├── views/
│   ├── admin/
│   │   ├── Login.vue           # 登录页
│   │   ├── Dashboard.vue       # 管理后台首页
│   │   └── HospitalList.vue    # 医院管理列表
├── components/
│   └── admin/
│       ├── HospitalForm.vue    # 医院表单（新增/编辑）
│       └── HospitalTable.vue   # 医院表格
├── router/
│   └── index.js                # 添加管理后台路由
├── api/
│   └── admin.js                # 管理后台 API
├── stores/
│   └── auth.js                 # 认证状态管理（Pinia）
└── guards/
    └── auth.js                 # 路由守卫
```

### 页面设计

#### 1. 登录页 (/admin/login)

```
┌─────────────────────────────┐
│  ChinaMedCare 管理后台       │
│                             │
│  ┌─────────────────────┐   │
│  │ 用户名/邮箱         │   │
│  └─────────────────────┘   │
│  ┌─────────────────────┐   │
│  │ 密码                │   │
│  └─────────────────────┘   │
│  ┌─────────────────────┐   │
│  │   登 录             │   │
│  └─────────────────────┘   │
│                             │
└─────────────────────────────┘
```

#### 2. 医院管理页 (/admin/hospitals)

```
┌─────────────────────────────────────────────────────────┐
│  ←  Dashboard  │ 医院管理                   [+ 新增医院]  │
├─────────────────────────────────────────────────────────┤
│  搜索: [___________________]  [筛选] [重置]             │
│                                                           │
│  ┌───┬──────────────────┬──────────┬───────┬────────┐  │
│  │ID │ 医院名称         │ 位置     │ 评分  │ 操作   │  │
│  ├───┼──────────────────┼──────────┼───────┼────────┤  │
│  │ 1 │ 北京协和医院     │ 北京     │ 4.9   │[编辑][删除]│ │
│  │ 2 │ 上海第一人民医院 │ 上海     │ 4.8   │[编辑][删除]│ │
│  │ 3 │ 广东省人民医院   │ 广州     │ 4.7   │[编辑][删除]│ │
│  └───┴──────────────────┴──────────┴───────┴────────┘  │
│                                                           │
│  上一页  1 2 3 ... 10  下一页                           │
└─────────────────────────────────────────────────────────┘
```

#### 3. 医院表单弹窗

```
┌─────────────────────────────────────┐
│  新增医院                     [×]    │
├─────────────────────────────────────┤
│  医院名称: [_________________]      │
│  位置:     [_________________]      │
│  评分:     [4.9]                    │
│  图片URL:  [_________________]      │
│                                     │
│  科室:                              │
│  [x] 心内科  [x] 神经科  [ ] 肿瘤科  │
│  [x] 骨科    [ ] 中医科  [ ] 皮肤科  │
│                                     │
│  语言:                              │
│  [x] 英语  [x] 中文  [ ] 日语      │
│  [ ] 韩语  [ ] 俄语                 │
│                                     │
│  [取消]              [保存]         │
└─────────────────────────────────────┘
```

---

## 路由配置

```javascript
// frontend/src/router/index.js
const routes = [
  // ... 现有路由
  {
    path: '/admin',
    component: () => import('@/views/admin/Dashboard.vue'),
    meta: { requiresAuth: true },
    children: [
      { path: '', redirect: '/admin/hospitals' },
      { path: 'hospitals', component: () => import('@/views/admin/HospitalList.vue') },
    ]
  },
  {
    path: '/admin/login',
    component: () => import('@/views/admin/Login.vue')
  }
]
```

---

## 实施步骤

### 第一阶段：后端 API
1. 创建数据模型 (Pydantic)
2. 实现医院 CRUD API（先用 mock 数据）
3. 实现简单认证（JWT）
4. 测试 API 端点

### 第二阶段：前端管理界面
1. 创建登录页面
2. 创建医院管理列表页
3. 创建医院表单组件
4. 添加路由和认证守卫
5. 集成 API

### 第三阶段：完善与优化
1. 多语言支持（管理后台界面翻译）
2. 确认对话框（删除前确认）
3. 加载状态和错误处理
4. 表单验证

---

## 安全考虑

1. **JWT 认证**：管理后台所有 API 需要 Token
2. **密码哈希**：使用 bcrypt 存储管理员密码
3. **CORS 配置**：限制管理后台 API 的来源
4. **输入验证**：使用 Pydantic 验证所有输入
5. **操作日志**：记录所有 CRUD 操作（可选）

---

## 默认管理员账户

```
用户名: admin
密码: admin123
```
（生产环境必须修改！）

---

## 后续扩展

- 医生管理
- 预约管理
- 用户管理
- 数据统计仪表盘
- 图片上传功能
- 导出 CSV/Excel
