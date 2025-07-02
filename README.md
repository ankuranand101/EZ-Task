# EZ-Task
# 📁 Smart File Sharing 

A Django REST API for secure file sharing between two user roles: **OPS** and **CLIENT**.  
Built as part of the EZ Backend Intern Assessment.

---

## 🔧 Tech Stack

- Python 3.x
- Django
- Django REST Framework
- Djoser (authentication & user management)
- SQLite (for simplicity)
- Token Authentication (via Djoser)

---

## 👥 User Roles

| Role   | Permissions                            |
|--------|----------------------------------------|
| OPS    | Upload files                           |
| CLIENT | Download files via encrypted URL only  |

---

## 🚀 Features

- ✅ User registration with role (OPS/CLIENT)
- ✅ Account activation via token (Djoser)
- ✅ Login with token authentication
- ✅ File upload for OPS users
- ✅ Secure, signed download links for CLIENT users
- ✅ File access restricted to authenticated users

---

## 📦 API Endpoints (Core)

### 🔐 Authentication

- `POST /auth/users/` → Register user
- `POST /auth/users/activation/` → Activate account
- `POST /auth/token/login/` → Login and get token
- `GET  /auth/users/me/` → Get current user info

### 📤 File Upload (OPS only)

- `POST /upload/` → Upload a file  
  `Header: Authorization: Token <token>`

### 🔑 Generate Secure Link (CLIENT only)

- `GET /generate-download/<file_id>/`  
  `Header: Authorization: Token <token>`

### 📥 Download File (CLIENT only)

- `GET /download/<signed_id>/`  
  `Header: Authorization: Token <token>`

---

## 📂 Setup Instructions

1. Create virtual env:
   python -m venv env
   env\Scripts\activate
   
3. Install dependencies:
   pip install -r requirements.txt

3. Apply migrations:
   python manage.py migrate

4. Run server:
   python manage.py runserver
   
### Sample OPS and CLIENT
# OPS User
{
  "username": "ops1",
  "password": "Ops@123456",
  "email": "ops@example.com",
  "role": "OPS"
}

# CLIENT User
{
  "username": "client1",
  "password": "Client@123456",
  "email": "client@example.com",
  "role": "CLIENT"
}
