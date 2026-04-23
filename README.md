# 📝 Task Manager REST API

A production-ready Task Management backend built using **Django REST Framework** with **JWT authentication**, enabling secure and user-specific task operations.

---

## 🚀 Live API

🔗 https://task-manager-j13m.onrender.com/swagger/

---

## ⚙️ Tech Stack

* **Backend:** Django, Django REST Framework
* **Authentication:** JWT (SimpleJWT)
* **Database:** PostgreSQL
* **Deployment:** Render + Gunicorn
* **API Documentation:** Swagger (drf-yasg)

---

## 🔐 Features

* User registration and login using JWT authentication
* Secure API endpoints with Bearer token authorization
* Full CRUD operations for task management
* User-specific data isolation
* Filtering tasks by completion status
* Search functionality using query parameters
* Pagination for handling large datasets
* Ordering support (e.g., latest tasks first)
* Deployed with production-ready configuration

---

## 📌 API Endpoints

### 🔑 Authentication

| Method | Endpoint              | Description                        |
| ------ | --------------------- | ---------------------------------- |
| POST   | `/api/register/`      | Register a new user                |
| POST   | `/api/token/`         | Login (get access & refresh token) |
| POST   | `/api/token/refresh/` | Refresh access token               |

---

### 📋 Tasks

| Method | Endpoint           | Description       |
| ------ | ------------------ | ----------------- |
| GET    | `/api/tasks/`      | Get all tasks     |
| POST   | `/api/tasks/`      | Create a new task |
| GET    | `/api/tasks/{id}/` | Retrieve task     |
| PUT    | `/api/tasks/{id}/` | Update task       |
| PATCH  | `/api/tasks/{id}/` | Partial update    |
| DELETE | `/api/tasks/{id}/` | Delete task       |

---

## 🔐 Authentication Usage

All protected endpoints require JWT token in headers:

Authorization: Bearer YOUR_ACCESS_TOKEN

---

## 🔍 Query Parameters

### Filter by completion:

`/api/tasks/?completed=true`

### Search by title:

`/api/tasks/?title=study`

### Order results:

`/api/tasks/?ordering=-created_at`

---

## 🧪 Example Request

### Create Task

```json
{
  "title": "Complete backend project",
  "completed": false
}
```

---

## 🛠️ Local Setup

```bash
git clone https://github.com/rohantiwari9573/task-manager.git
cd task-manager
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

---

## 📦 Deployment

Deployed on **Render** using:

* Gunicorn (WSGI server)
* PostgreSQL database
* Environment-based configuration

---

## 📈 Future Improvements

* Add task priority and due dates
* Add unit and integration tests
* Dockerize the project
* Add caching (Redis)

---

## 👨‍💻 Author

**Rohan Tiwari**
📧 [rohantiwari166@gmail.com](mailto:rohantiwari166@gmail.com)
🔗 https://github.com/rohantiwari9573
