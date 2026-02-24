# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概述

**项目名称**: ChinaMedCare
**定位**: 外国人来华就医一站式服务平台
**技术栈**: Vue.js 3 (前端) + Python FastAPI (后端)

## 常用命令

### 前端开发
```bash
cd frontend
npm install          # 安装依赖
npm run dev          # 启动开发服务器 (端口 3000)
npm run build        # 构建生产版本
```

### 后端开发
```bash
cd backend
pip install -r requirements.txt    # 安装依赖
uvicorn app.main:app --reload      # 启动开发服务器 (端口 8000)
```

API 文档: http://localhost:8000/docs

## 代码架构

### 前端结构
```
frontend/src/
├── components/       # 可复用组件 (Header.vue, Footer.vue, HospitalCard.vue)
├── views/           # 页面视图 (Home.vue, HospitalList.vue, Services.vue)
├── locales/         # 多语言文件 (en.json, zh.json, ru.json, ja.json, ko.json)
├── router/          # 路由配置
├── assets/styles/   # 全局样式
├── App.vue          # 根组件
└── main.js          # 入口文件
```

### 后端结构
```
backend/app/
├── api/             # API 路由 (hospitals.py, doctors.py, bookings.py)
├── models/          # 数据模型
├── services/        # 业务逻辑服务
└── main.py          # FastAPI 应用入口
```

## 多语言 (i18n)

支持 5 种语言: English (en), 中文 (zh), 俄语 (ru), 日语 (ja), 韩语 (ko)

添加新翻译时，需在 `frontend/src/locales/` 下的所有语言文件中同步添加键值。

## 现有组件

- `Header.vue` - 顶部导航栏，含语言切换
- `Footer.vue` - 页脚
- `HospitalCard.vue` - 医院卡片展示

## 环境变量

前端代理: `/api` 请求代理到 `http://localhost:8000` (配置在 `vite.config.js`)
