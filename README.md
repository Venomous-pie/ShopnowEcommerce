# ShopnowEcommerce – Company Development Guide

Welcome to the ShopnowEcommerce project. This document provides comprehensive instructions for setting up, running, and contributing to the project in a local development environment.

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Prerequisites](#prerequisites)
3. [Environment Setup](#environment-setup)
    - [Backend (Django)](#backend-django-setup)
    - [Frontend (Vue 3 + Vite)](#frontend-vue-3--vite-setup)
4. [Running the Application](#running-the-application)
5. [Environment Variables](#environment-variables)
6. [Production Build](#production-build)
7. [Troubleshooting](#troubleshooting)
8. [Project Structure](#project-structure)
9. [Contributing](#contributing)
10. [Contact](#contact)

---

## Project Overview
ShopnowEcommerce is a modern e-commerce platform featuring a Django REST backend and a Vue 3 frontend powered by Vite. The project is structured for scalability, maintainability, and ease of collaboration.

---

## Prerequisites
- **Python 3.10+**
- **Node.js 18+** and **npm**
- **pip** (Python package manager)
- (Recommended) **virtualenv** for Python
- **PowerShell** (for Windows users)

---

## Environment Setup

### Backend (Django) Setup
1. Open PowerShell and navigate to the backend directory:
   ```powershell
   cd backend
   ```
2. Create and activate a virtual environment:
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```
3. Install Python dependencies:
   ```powershell
   pip install -r ..\requirements.txt
   ```
4. Apply database migrations:
   ```powershell
   python manage.py migrate
   ```
5. (Optional) Create a superuser for admin access:
   ```powershell
   python manage.py createsuperuser
   ```

### Frontend (Vue 3 + Vite) Setup
1. In a new PowerShell window, navigate to the frontend directory:
   ```powershell
   cd frontend
   ```
2. Install Node.js dependencies:
   ```powershell
   npm install
   ```

---

## Running the Application

### Start the Django Backend
```powershell
cd backend
.\venv\Scripts\Activate.ps1
python manage.py runserver
```
The backend will be available at http://localhost:8000

### Start the Vue Frontend
```powershell
cd frontend
npm run dev
```
The frontend will be available at http://localhost:5173

---

## Environment Variables
- **Django:**
  - Configure sensitive settings (e.g., `SECRET_KEY`, database credentials) in `backend/.env` (use [python-dotenv](https://pypi.org/project/python-dotenv/) or similar if needed).
- **Vue:**
  - Place frontend environment variables in `frontend/.env` (see [Vite env docs](https://vitejs.dev/guide/env-and-mode.html)).

---

## Production Build
1. Build the frontend for production:
   ```powershell
   cd frontend
   npm run build
   ```
   The output will be in `frontend/dist/`.
2. Configure Django to serve static files from the frontend build:
   - Update `STATICFILES_DIRS` or `STATIC_ROOT` in `backend/settings.py`.
   - Collect static files:
     ```powershell
     cd backend
     python manage.py collectstatic
     ```

---

## Troubleshooting
- **CORS Errors:** Ensure `django-cors-headers` is installed and `CORS_ALLOWED_ORIGINS` includes your frontend URL.
- **API Proxy:** In `frontend/vite.config.js`, proxy `/api` to `http://localhost:8000` for local development.
- **Dependency Issues:**
  - For Python: Ensure the virtual environment is activated and dependencies are installed.
  - For Node: Delete `node_modules` and run `npm install` if issues persist.
- **Port Conflicts:** Make sure ports 8000 (backend) and 5173 (frontend) are available.

---

## Project Structure
```
ShopnowEcommerce/
├── backend/         # Django backend
│   ├── api/         # Django app (API)
│   └── backend/     # Django project settings
├── frontend/        # Vue 3 + Vite frontend
│   ├── src/
│   │   ├── App.vue         # Main Vue app entry
│   │   ├── main.js         # JS entry point
│   │   ├── style.css       # Global styles
│   │   ├── assets/         # Static assets
│   │   └── components/     # Vue components (e.g., HelloWorld.vue)
│   ├── public/
│   └── ...
├── requirements.txt # Python dependencies
└── README.md        # This guide
```

---

## Branching Strategy

This repository uses a branch-based workflow to support parallel development and maintain code quality. Below are the main branches and their purposes:

- **main**: The primary branch containing stable, production-ready code. All releases are tagged from this branch.
- **addfeature**: Used for developing new features. Each new feature should be developed in its own branch off of `main` or the latest stable branch, then merged via pull request.
- **bugfixes**: Dedicated to addressing and resolving bugs. Hotfixes and patches should be committed here and merged into `main` after review.
- **testing**: Used for integration and system testing. Experimental changes and QA processes are performed here before merging into `main`.
- **updates**: Used for general updates, refactoring, or improvements that do not fall under features, bugfixes, or testing. Merge into `main` after review.

> **Note:** Always create descriptive feature or bugfix branches for specific tasks (e.g., `feature/user-auth`, `bugfix/cart-total`).

---

## Contact
For questions, onboarding, or support, contact the project maintainer or your team lead.

---

Thank you for contributing to ShopnowEcommerce!
