# HealthDesk Authentication Module

## Overview
Simple authentication system with no JWT tokens or session timeouts. User information is stored in memory (localStorage) on the frontend after successful login.

## Features

### Backend
- **User Registration** - Create users with roles (admin, doctor, staff)
- **Login** - Validate credentials and return user information
- **Password Hashing** - Secure password storage using bcrypt
- **Role-Based Access** - Three user roles: admin, doctor, staff

### Frontend  
- **Auth Context** - React context for managing user state
- **Lazy Loading** - Login module loaded on demand
- **Protected Routes** - Route guards based on authentication and roles
- **Role-Based Dashboards** - Different dashboards for each role
- **Persistent Login** - User data stored in localStorage

## API Endpoints

### POST /api/auth/register
Register a new user.

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "password123",
  "full_name": "John Doe",
  "role": "staff",  // admin, doctor, or staff
  "is_active": true
}
```

**Response:**
```json
{
  "id": "507f1f77bcf86cd799439011",
  "email": "user@example.com",
  "full_name": "John Doe",
  "role": "staff",
  "is_active": true,
  "created_at": "2026-01-14T10:30:00.000Z"
}
```

### POST /api/auth/login
Login with email and password.

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "password123"
}
```

**Response:**
```json
{
  "user": {
    "id": "507f1f77bcf86cd799439011",
    "email": "user@example.com",
    "full_name": "John Doe",
    "role": "staff",
    "is_active": true,
    "created_at": "2026-01-14T10:30:00.000Z"
  },
  "message": "Login successful"
}
```

### GET /api/auth/users/me?email={email}
Get current user information (for session validation).

## User Roles

### Admin
- Full system access
- User management
- View all enquiries
- Manage doctors
- System settings

**Routes:**
- `/admin/dashboard` - Admin dashboard

### Doctor
- View schedule
- Manage availability
- View appointments
- Access patient records
- Clinical guidelines

**Routes:**
- `/doctor/dashboard` - Doctor dashboard

### Staff
- View patient enquiries
- Book appointments
- Check doctor availability
- Manage appointments
- Send notifications

**Routes:**
- `/staff/dashboard` - Staff dashboard

## Frontend Usage

### Login
```jsx
import { useAuth } from './context/AuthContext';

function LoginComponent() {
  const { login } = useAuth();
  
  const handleLogin = async () => {
    const result = await login(email, password);
    if (result.success) {
      // User logged in, navigate to dashboard
    } else {
      // Show error: result.error
    }
  };
}
```

### Check Authentication
```jsx
const { user, isAuthenticated } = useAuth();

if (isAuthenticated) {
  // User is logged in
  console.log(user.role); // admin, doctor, or staff
}
```

### Logout
```jsx
const { logout } = useAuth();

logout(); // Clears user from state and localStorage
```

### Role-Based Access
```jsx
const { hasRole, hasAnyRole } = useAuth();

if (hasRole('admin')) {
  // Show admin features
}

if (hasAnyRole(['doctor', 'staff'])) {
  // Show features for doctors and staff
}
```

## Testing

### Create Test Users

You can use the API directly to create test users:

```bash
# Create Admin User
curl -X POST http://localhost:8000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "admin@healthdesk.com",
    "password": "admin123",
    "full_name": "Admin User",
    "role": "admin"
  }'

# Create Doctor User
curl -X POST http://localhost:8000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "doctor@healthdesk.com",
    "password": "doctor123",
    "full_name": "Dr. Smith",
    "role": "doctor"
  }'

# Create Staff User
curl -X POST http://localhost:8000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "staff@healthdesk.com",
    "password": "staff123",
    "full_name": "Staff Member",
    "role": "staff"
  }'
```

### Test Login

Visit `http://localhost:3000/login` and use:
- **Admin:** admin@healthdesk.com / admin123
- **Doctor:** doctor@healthdesk.com / doctor123
- **Staff:** staff@healthdesk.com / staff123

## Security Notes

- Passwords are hashed using bcrypt before storage
- Plain passwords are never stored in the database
- No JWT tokens or session management
- User data persists in localStorage (client-side only)
- For production, consider adding:
  - Token-based authentication
  - Session timeouts
  - HTTPS enforcement
  - Rate limiting
  - CSRF protection

## Frontend Routes

### Public Routes
- `/login` - Login page (redirects to dashboard if logged in)

### Protected Routes  
- `/dashboard` - General dashboard (any authenticated user)
- `/admin/dashboard` - Admin only
- `/doctor/dashboard` - Doctor only
- `/staff/dashboard` - Staff only
- `/unauthorized` - Access denied page

## Installation

### Backend Dependencies
```bash
cd Api-Service
.\venv\Scripts\Activate.ps1
pip install passlib bcrypt
```

### Frontend (already included in package.json)
```bash
cd Frontend
npm install
```

## Running the System

1. **Start Backend:**
```bash
cd Api-Service
.\venv\Scripts\Activate.ps1
python main.py
```
API running at: http://localhost:8000
API Docs: http://localhost:8000/docs

2. **Start Frontend:**
```bash
cd Frontend
npm run dev
```
App running at: http://localhost:3000

3. **Create test users** using the curl commands above or via API docs

4. **Login** at http://localhost:3000/login

## File Structure

### Backend
```
Api-Service/
├── app/
│   ├── api/routes/
│   │   └── auth.py              # Auth endpoints
│   ├── core/
│   │   ├── security.py          # Password hashing
│   │   └── config.py            # Configuration
│   └── models/
│       └── user.py              # User models
└── main.py                      # Updated with auth router
```

### Frontend
```
Frontend/
├── src/
│   ├── context/
│   │   └── AuthContext.jsx      # Auth state management
│   ├── features/auth/
│   │   ├── Login.jsx            # Login component (lazy loaded)
│   │   └── Login.css            # Login styles
│   ├── components/
│   │   └── ProtectedRoute.jsx   # Route guards
│   ├── pages/
│   │   ├── Dashboard.jsx        # General dashboard
│   │   ├── AdminDashboard.jsx   # Admin dashboard
│   │   ├── DoctorDashboard.jsx  # Doctor dashboard
│   │   ├── StaffDashboard.jsx   # Staff dashboard
│   │   └── Unauthorized.jsx     # Access denied page
│   └── App.jsx                  # Updated with routes
```
