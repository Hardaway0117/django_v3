# 📝 Django Task API - V3

這是一個使用 **Django REST Framework** 打造的任務管理系統 API，支援 **JWT 認證登入**、**Swagger UI 文件說明**，並整合 **PostgreSQL 資料庫**

---

## 🚀 專案功能

- ✅ 使用者登入（JWT 驗證）
- ✅ 任務清單 API（CRUD）
- ✅ Swagger 文件自動生成（/swagger/）
- ✅ 使用者權限驗證（登入才能使用 API）
- ✅ PostgreSQL 資料庫整合
- ✅ Admin 後台可管理任務與帳號

---
打開 /api/token/ 取得 取得 access、refresh (token) (refresh 可保留作後續取得access)

點 Swagger 右上角「Authorize」 (http://127.0.0.1:8000/swagger/)
input access token to login
---

Import -
| Django       | Python Web 框架
| Django REST Framework | 架構化 API 接口

| Simple JWT   | JSON Web Token 認證登入
| drf-yasg     | 自動生成 Swagger 文件
| PostgreSQL   | 資料庫系統

- `/api/`：API 主入口
- `/api/tasks/`：任務 CRUD（需 JWT 驗證）
- `/api/token/`：登入（取得 JWT）
- `/swagger/`：API 文件說明（可登入測試）
- `/admin/`：管理員後台




```bash
git clone https://github.com/Hardaway0117/django_v3.git
cd django_v3
python -m venv venv
venv\Scripts\activate 
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

By Hardaway0117
