# 部署检查清单

## 部署前准备

- [ ] 代码已推送到 GitHub
- [ ] 已注册 Vercel 账户 (https://vercel.com)
- [ ] 已注册 Railway 账户 (https://railway.app)

## 部署步骤

### Railway - 数据库
- [ ] 创建 Railway 新项目
- [ ] 添加 PostgreSQL 数据库
- [ ] 复制 DATABASE_URL

### Railway - 后端
- [ ] 在同一项目中添加 GitHub 仓库服务
- [ ] 配置 Root Directory 为 `backend`
- [ ] 添加环境变量：
  - [ ] DATABASE_URL
  - [ ] API_KEY
  - [ ] JWT_SECRET
  - [ ] CORS_ORIGINS
- [ ] 部署后端服务
- [ ] 生成并复制后端公网域名

### Vercel - 前端
- [ ] 导入 GitHub 仓库到 Vercel
- [ ] 配置 Root Directory 为 `frontend`
- [ ] 添加环境变量：
  - [ ] VITE_API_URL = Railway 后端域名
- [ ] 部署前端
- [ ] 复制 Vercel 前端域名

### 完成配置
- [ ] 更新 Railway 后端的 CORS_ORIGINS，添加 Vercel 域名
- [ ] 等待后端自动重新部署

## 验证

- [ ] 访问后端 /health 端点，确认正常
- [ ] 访问后端 /api/hospitals/ 端点，确认正常
- [ ] 访问前端，确认页面加载正常
- [ ] 测试前端是否能正常调用后端 API

## 本地开发

- [ ] 创建 frontend/.env.local 文件
- [ ] 设置 VITE_API_URL=http://localhost:8000
- [ ] 运行 docker-compose -f docker-compose.dev.yml up -d
