# 🚀 DeployMate

A DevOps-focused project built with **FastAPI**, **React**, **Terraform**, and **GitHub Actions**.  
DeployMate simulates a lightweight deployment dashboard for internal teams to track builds, versions, and cloud metrics.

---

## 📦 Features

- 🔧 **API Layer** with FastAPI for deployment logs, version info, and resource usage
- ⚙️ **GitHub Actions** pipeline simulating CI/CD logs
- ☁️ **Terraform** infrastructure for Azure (Resource Group + Storage Account)
- 📊 **React Dashboard** to visualize live data from API
- 🔐 CORS-configured for React ↔ FastAPI communication

---

## 🧪 API Endpoints

| Method | Endpoint        | Description                     |
|--------|------------------|---------------------------------|
| GET    | `/logs`          | Returns simulated deploy logs  |
| GET    | `/version`       | Fetches GitHub repo metadata   |
| GET    | `/resources`     | Returns fake CPU, RAM, storage |
| GET    | `/`              | Serves React frontend          |

---

## 📁 Tech Stack

- **Frontend:** React
- **Backend:** FastAPI (Python)
- **CI/CD:** GitHub Actions
- **IaC:** Terraform (Azure)
- **Hosting:** Local (or Render/Netlify optional)

---

## 🚀 Run Locally

### Backend (FastAPI)

```bash
cd app/
uvicorn main:app --reload
```
### Frontend (React)

```bash
cd deploymate-ui/
npm install
npm start
```