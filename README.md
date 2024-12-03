# Role-Based-Access-Control-RBAC-
# Backend Developer Assignment

## Description
This project implements Role-Based Access Control (RBAC) for managing users, login, logout, and admin access. It uses Django REST Framework and JWT for authentication.

## Features
- User Registration
- Login (with JWT tokens)
- Logout (JWT token blacklisting)
- Admin access (only accessible to admins)

## How to Run
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run migrations: `python manage.py migrate`
4. Start the development server: `python manage.py runserver`

## Endpoints
- `POST /api/accounts/register/` - Register a new user
- `POST /api/accounts/login/` - Login and receive JWT tokens
- `POST /api/accounts/logout/` - Logout (invalidate JWT token)
- `GET /api/accounts/admin-dashboard/` - Access admin dashboard (admin only)

## Dependencies
- Django 5.1.3
- djangorestframework
- djangorestframework_simplejwt
- etc.

## Notes
- Ensure that you set up the `SECRET_KEY` in the settings.py file correctly.
