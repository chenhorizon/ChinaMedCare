# ChinaMedCare

外国人来华就医一站式服务平台

## 项目简介

ChinaMedCare 是一个服务于外国人来华就医的平台，提供医院/医生查询、预约挂号、病历翻译、陪诊预订等服务。

## 技术栈

- **前端**: Vue.js 3 + Vite + Element Plus + Vue I18n
- **后端**: Python + FastAPI
- **语言支持**: 英语、中文、俄语、日语、韩语

## 项目结构

```
MedicalCare/
├── frontend/          # 前端Vue项目
│   ├── src/
│   │   ├── components/
│   │   ├── views/
│   │   ├── locales/     # 多语言文件
│   │   └── router/
│   │   └── main.js
│   │   └── App.vue
│   └── package.json
│   └── vite.config.js
│   └── index.html
├── backend/          # 后端Python项目
│   ├── app/
│   │   ├── api/
│   │   ├── models/
│   │   ├── services/
│   │   └── main.py
│   └── requirements.txt
└── README.md
```

---

## 在新电脑上运行项目

### 前置要求

确保你的电脑已安装：
- **Node.js** (v18 或更高)
- **npm** (随 Node.js 一起安装)
- **Python** (3.9 或更高)
- **Git**

---

### 步骤 1: 克隆仓库

```bash
git clone https://github.com/chenhorizon/ChinaMedCare.git
cd ChinaMedCare
```

---

### 步骤 2: 安装前端依赖

```bash
cd frontend
npm install
```

---

### 步骤 3: 安装后端依赖

```bash
cd ../backend
pip install -r requirements.txt
```

（推荐使用虚拟环境）
```bash
cd ../backend
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
pip install -r requirements.txt
```

---

### 步骤 4: 启动后端

在 `backend` 目录下：
```bash
uvicorn app.main:app --reload
```

后端将运行在: http://localhost:8000

API 文档: http://localhost:8000/docs

---

### 步骤 5: 启动前端

打开一个新的终端窗口，在 `frontend` 目录下：
```bash
cd frontend
npm run dev
```

前端将运行在: http://localhost:3000

---

## 日常开发

### 前端启动
```bash
cd frontend
npm run dev
```

前端访问地址: http://localhost:3000

### 后端启动
```bash
cd backend
uvicorn app.main:app --reload
```

后端API文档: http://localhost:8000/docs

---

## 功能模块

- 🏥 医院/医生展示与查询
- 📅 在线预约挂号
- 📄 病历翻译
- 🧑‍⚕️ 陪诊服务预订
- ✈️ 签证协助
- 💰 费用估算

## 多语言支持

- English
- 中文
- Русский
- 日本語
- 한국어

---

## Git 工作流

### 拉取最新代码
```bash
git pull origin main
```

### 提交更改
```bash
git add .
git commit -m "描述你的更改"
git push origin main
```

---

## 安全说明

- `.env` 文件已包含在 `.gitignore` 中，不会被提交
- 复制 `backend/.env.example` 为 `backend/.env` 并填入实际配置
- 永远不要将 API keys、密码等敏感信息提交到仓库
