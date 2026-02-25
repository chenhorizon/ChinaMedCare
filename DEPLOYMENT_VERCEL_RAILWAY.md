# Vercel + Railway 部署指南

本指南将帮助你将 ChinaMedCare 项目部署到 Vercel（前端）和 Railway（后端 + 数据库）。

## 目录
- [前置准备](#前置准备)
- [第一步：部署数据库（Railway）](#第一步部署数据库railway)
- [第二步：部署后端（Railway）](#第二步部署后端railway)
- [第三步：部署前端（Vercel）](#第三步部署前端vercel)
- [配置环境变量](#配置环境变量)
- [验证部署](#验证部署)

---

## 前置准备

你需要：
1. GitHub 账户（将代码推送到 GitHub）
2. Vercel 账户（https://vercel.com）
3. Railway 账户（https://railway.app）

### 推送代码到 GitHub

```bash
# 初始化 git（如果还没有）
git init

# 添加所有文件
git add .

# 提交
git commit -m "Initial commit for deployment"

# 添加远程仓库（先在 GitHub 创建仓库）
git remote add origin https://github.com/你的用户名/ChinaMedCare.git

# 推送
git push -u origin main
```

---

## 第一步：部署数据库（Railway）

1. 登录 [Railway](https://railway.app)
2. 点击 "New Project"
3. 选择 "Provision PostgreSQL"
4. 等待数据库创建完成
5. 点击数据库 → 点击 "Variables" 标签
6. 保存 `DATABASE_URL`，后面会用到

---

## 第二步：部署后端（Railway）

1. 在 Railway 项目中，点击 "Add Service"
2. 选择 "GitHub Repo"
3. 选择你的 ChinaMedCare 仓库
4. 配置部署：
   - **Root Directory**: `backend`
   - **Branch**: `main`
5. 点击 "Variables" 标签，添加以下环境变量：
   ```
   DATABASE_URL=postgresql://... (从数据库服务复制)
   API_KEY=你自定义的密钥
   JWT_SECRET=你自定义的密钥
   CORS_ORIGINS=https://你的-vercel-domain.vercel.app,http://localhost:3000,http://localhost
   ```
6. 点击 "Deploy" 等待部署完成
7. 部署成功后，点击 "Settings" → "Generate Domain" 为后端生成一个公网域名
8. 保存这个后端 URL（例如：`https://chinamedcare-backend.up.railway.app`）

---

## 第三步：部署前端（Vercel）

1. 登录 [Vercel](https://vercel.com)
2. 点击 "Add New Project"
3. 选择你的 ChinaMedCare 仓库
4. 配置项目：
   - **Framework Preset**: Vue
   - **Root Directory**: `frontend`  (重要！必须设置)
   - **Build Command**: (留空，使用默认或 `npm run build`)
   - **Output Directory**: (留空，使用默认或 `dist`)
5. 点击 "Environment Variables"，添加：
   ```
   VITE_API_URL=https://你的-railway-backend.up.railway.app
   ```
6. 点击 "Deploy" 等待部署完成
7. 部署成功后，你会得到一个 Vercel 域名（例如：`https://chinamedcare.vercel.app`）

**重要提示**：
- Root Directory 必须设置为 `frontend`
- Build Command 不需要加 `cd frontend`，因为 Root Directory 已经是 frontend 了
- 我们在 `frontend/` 目录下已经放置了 `vercel.json` 配置文件

---

## 第四步：更新 CORS 配置（重要！）

部署完前端后，你需要更新 Railway 后端的 CORS 配置：

1. 回到 Railway 后端服务
2. 点击 "Variables"
3. 更新 `CORS_ORIGINS`，添加你的 Vercel 域名：
   ```
   CORS_ORIGINS=https://chinamedcare.vercel.app,http://localhost:3000,http://localhost
   ```
4. 保存后，Railway 会自动重新部署

---

## 验证部署

### 测试后端
访问：`https://你的-railway-backend.up.railway.app/health`

应该看到：`{"status": "healthy"}`

### 测试医院列表 API
访问：`https://你的-railway-backend.up.railway.app/api/hospitals/`

### 测试前端
访问你的 Vercel 域名，应该能看到完整的网站。

---

## 本地开发

开发时，创建 `frontend/.env.local`：
```
VITE_API_URL=http://localhost:8000
```

然后使用 Docker Compose 启动本地环境：
```bash
docker-compose -f docker-compose.dev.yml up -d
```

---

## 故障排除

### 问题：Vercel 构建失败，提示 "cd: frontend: No such file or directory"

**错误信息**：
```
sh: line 1: cd: frontend: No such file or directory
```

**解决方案**：
1. 在 Vercel 项目设置中：
   - 确保 **Root Directory** 设置为 `frontend`
   - **Build Command** 留空或设置为 `npm run build`（不要加 `cd frontend`）
   - **Output Directory** 留空或设置为 `dist`
2. 重新部署

我们在 `frontend/` 目录下已经放置了 `vercel.json` 配置文件，Vercel 会自动使用它。

---

### 问题：Dockerfile 构建失败，提示找不到 requirements.txt

**错误信息**：
```
ERROR: failed to build: failed to solve: "/requirements.txt": not found
```

**解决方案**：
我们已经修复了这个问题！项目现在使用根目录的 `Dockerfile.backend`，它能正确地从 `backend/` 目录复制文件。

确保：
1. `railway.json` 中的 `dockerfilePath` 设置为 `"Dockerfile.backend"`
2. 根目录下有 `Dockerfile.backend` 文件
3. 重新触发部署

---

## 常见问题

**Q: 前端无法连接后端？**
A: 检查以下几点：
1. `VITE_API_URL` 环境变量是否正确设置
2. Railway 后端的 CORS_ORIGINS 是否包含了前端域名
3. 后端服务是否正常运行

**Q: 部署失败？**
A: 查看部署日志：
- Vercel: 项目首页 → Deployments → 选择部署记录
- Railway: 服务页面 → View Logs

**Q: 如何自定义域名？**
A:
- Vercel: Settings → Domains
- Railway: Settings → Custom Domains
