# Docker 部署指南

## 快速开始

### 生产环境部署

```bash
# 1. 复制环境变量配置
cp .env.example .env
# 编辑 .env 文件，修改敏感信息

# 2. 构建并启动所有服务
docker-compose up -d --build

# 3. 查看服务状态
docker-compose ps

# 4. 查看日志
docker-compose logs -f
```

访问地址：
- 前端: http://localhost
- 后端 API: http://localhost:8000
- API 文档: http://localhost:8000/docs

---

### 开发环境部署（支持热重载）

```bash
# 1. 复制环境变量配置
cp .env.example .env

# 2. 使用开发环境配置启动
docker-compose -f docker-compose.dev.yml up -d --build

# 3. 查看日志
docker-compose -f docker-compose.dev.yml logs -f
```

开发环境访问：
- 前端: http://localhost:3000 (Vite 热重载)
- 后端 API: http://localhost:8000 (Uvicorn --reload)

---

## 常用命令

### 管理服务
```bash
# 启动服务
docker-compose up -d

# 停止服务
docker-compose stop

# 停止并删除容器
docker-compose down

# 停止并删除容器和数据卷（谨慎使用！）
docker-compose down -v

# 查看服务状态
docker-compose ps
```

### 查看日志
```bash
# 查看所有服务日志
docker-compose logs -f

# 查看特定服务日志
docker-compose logs -f backend
docker-compose logs -f frontend
docker-compose logs -f db
```

### 进入容器
```bash
# 进入后端容器
docker-compose exec backend bash

# 进入数据库容器
docker-compose exec db psql -U chinamedcare -d chinamedcare
```

---

## 服务说明

| 服务 | 容器名 | 端口 | 说明 |
|------|--------|------|------|
| frontend | chinamedcare-frontend | 80 | Nginx 托管的 Vue 前端 |
| backend | chinamedcare-backend | 8000 | FastAPI 后端服务 |
| db | chinamedcare-db | 5432 | PostgreSQL 数据库 |

---

## 环境变量

在 `.env` 文件中配置：

| 变量 | 说明 | 默认值 |
|------|------|--------|
| DB_USER | 数据库用户名 | chinamedcare |
| DB_PASSWORD | 数据库密码 | chinamedcare |
| DB_NAME | 数据库名 | chinamedcare |
| API_KEY | API 密钥 | - |
| JWT_SECRET | JWT 密钥 | - |
| CORS_ORIGINS | 允许的 CORS 源 | http://localhost:3000,http://localhost |

---

## 生产环境安全建议

1. **修改所有默认密码**（DB_PASSWORD、API_KEY、JWT_SECRET）
2. 使用强密码和随机密钥
3. 配置 HTTPS（使用 Let's Encrypt）
4. 限制数据库端口不对外暴露
5. 定期备份数据库数据
6. 使用防火墙限制访问 IP
