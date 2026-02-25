# 管理后台 API 测试指南

## 数据库说明

现在数据存储在 **SQLite/PostgreSQL 数据库**中（不再是内存存储）！

- 默认使用 SQLite（`./chinamedcare.db`）
- 可以通过 `DATABASE_URL` 环境变量配置 PostgreSQL
- 服务器重启后数据不会丢失

---

## 快速开始

### 1. 启动后端服务

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# 初始化数据库（可选，会自动运行）
python -m app.db.init_db

# 启动服务
uvicorn app.main:app --reload
```

### 2. 访问 API 文档

打开浏览器访问：http://localhost:8000/docs

---

## API 端点列表

### 认证端点

#### POST /api/admin/login
管理员登录

**请求体**：
```json
{
  "username": "admin",
  "password": "admin123"
}
```

**响应**：
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

---

### 医院管理端点

所有医院管理端点都需要在请求头中添加 Bearer Token：
```
Authorization: Bearer <access_token>
```

#### GET /api/admin/hospitals
获取医院列表（分页）

**查询参数**：
- `page`: 页码（默认 1）
- `page_size`: 每页数量（默认 10，最大 100）
- `search`: 按名称搜索（可选）
- `department`: 按科室筛选（可选）
- `city`: 按城市筛选（可选）

**响应**：
```json
{
  "items": [...],
  "total": 3,
  "page": 1,
  "page_size": 10,
  "total_pages": 1
}
```

#### GET /api/admin/hospitals/{id}
获取单个医院

#### POST /api/admin/hospitals
创建新医院

**请求体**：
```json
{
  "name": "New Hospital",
  "location": "Beijing, China",
  "rating": 4.5,
  "image": "https://example.com/image.jpg",
  "departments": ["Cardiology", "Neurology"],
  "languages": ["English", "Chinese"]
}
```

#### PUT /api/admin/hospitals/{id}
更新医院

**请求体**（只包含要更新的字段）：
```json
{
  "name": "Updated Hospital Name",
  "rating": 4.8
}
```

#### DELETE /api/admin/hospitals/{id}
删除医院（返回 204 No Content）

---

## 数据库配置

### 使用 SQLite（默认）
无需配置，自动使用 `./chinamedcare.db`

### 使用 PostgreSQL
设置环境变量：
```bash
export DATABASE_URL=postgresql://user:password@localhost:5432/chinamedcare
```

### 使用 Docker Compose
```bash
docker-compose -f docker-compose.dev.yml up -d
```
会自动使用 PostgreSQL 容器。

---

## 使用 curl 测试

### 1. 登录获取 Token
```bash
curl -X POST http://localhost:8000/api/admin/login \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "admin123"}'
```

### 2. 使用 Token 访问医院列表
```bash
# 替换 <your_token> 为实际的 token
curl -X GET "http://localhost:8000/api/admin/hospitals?page=1&page_size=10" \
  -H "Authorization: Bearer <your_token>"
```

### 3. 创建新医院
```bash
curl -X POST http://localhost:8000/api/admin/hospitals \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <your_token>" \
  -d '{
    "name": "Test Hospital",
    "location": "Shenzhen, China",
    "rating": 4.3,
    "image": "https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?w=400",
    "departments": ["Cardiology", "Pediatrics"],
    "languages": ["English", "Chinese"]
  }'
```

### 4. 更新医院
```bash
curl -X PUT http://localhost:8000/api/admin/hospitals/4 \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <your_token>" \
  -d '{"rating": 4.6}'
```

### 5. 删除医院
```bash
curl -X DELETE http://localhost:8000/api/admin/hospitals/4 \
  -H "Authorization: Bearer <your_token>"
```

---

## 默认账户

| 用户名 | 密码 |
|--------|------|
| admin | admin123 |

---

## 使用 Swagger UI 测试

1. 访问 http://localhost:8000/docs
2. 点击 `/api/admin/login` 端点
3. 点击 "Try it out"
4. 输入用户名和密码，点击 "Execute"
5. 复制返回的 `access_token`
6. 点击页面右上角的 "Authorize" 按钮
7. 输入 `Bearer <your_token>`（注意 Bearer 和 token 之间有空格）
8. 现在可以测试其他需要认证的端点了

---

## 数据库文件

- SQLite: `backend/chinamedcare.db`
- 可以使用 DB Browser for SQLite 查看和编辑
