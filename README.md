# HealthDesk - Healthcare Management System

A comprehensive healthcare management system that enables patients to send enquiries to staff, who can then book appointments based on doctor availability. The system is designed to be extended with RAG (Retrieval-Augmented Generation), Vector Search, and MCP (Model Context Protocol) for Clinical Guidelines & Patient Education.

## Project Overview

This project consists of two main parts:

1. **Frontend** - React-based user interface
2. **Api-Service** - Python FastAPI backend with MongoDB Atlas

## Architecture

```
HealthDesk/
├── Frontend/              # React + Vite application
│   ├── src/
│   ├── package.json
│   └── README.md
│
└── Api-Service/           # FastAPI + MongoDB application
    ├── app/
    ├── main.py
    ├── requirements.txt
    └── README.md
```

## Quick Start

### Prerequisites

- **Node.js** 16+ and npm (for Frontend)
- **Python** 3.8+ (for Backend)
- **MongoDB Atlas** account (free tier works)

### 1. Setup Backend (Api-Service)

```bash
# Navigate to Api-Service
cd Api-Service

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env and add your MongoDB Atlas connection string

# Run the server
python main.py
```

Backend will be running at: `http://localhost:8000`
API Docs: `http://localhost:8000/docs`

### 2. Setup Frontend

```bash
# Navigate to Frontend (in a new terminal)
cd Frontend

# Install dependencies
npm install

# Run development server
npm run dev
```

Frontend will be running at: `http://localhost:3000`

## Features

### Current Features (v0.1.0)

- ✅ Patient enquiry submission
- ✅ Enquiry management API
- ✅ MongoDB Atlas integration
- ✅ CORS-enabled API
- ✅ Modern React UI
- ✅ RESTful API endpoints

### Planned Features

- 🔜 User authentication & authorization
- 🔜 Doctor availability management
- 🔜 Appointment booking system
- 🔜 Staff dashboard
- 🔜 Patient dashboard
- 🔜 Clinical Guidelines Assistant (RAG)
- 🔜 Vector Search for medical information
- 🔜 MCP integration for AI capabilities
- 🔜 Patient education resources

## Technology Stack

### Frontend
- React 18
- Vite
- React Router
- Axios
- CSS3

### Backend
- FastAPI
- MongoDB Atlas (Motor async driver)
- Pydantic
- Uvicorn
- Python 3.8+

## API Endpoints

### Health
- `GET /api/` - Root endpoint
- `GET /api/health` - Health check

### Enquiries
- `POST /api/enquiries/` - Create new enquiry
- `GET /api/enquiries/` - List all enquiries
- `GET /api/enquiries/{id}` - Get specific enquiry

## Project Structure

See individual README files for detailed structure:
- [Frontend README](Frontend/README.md)
- [Backend README](Api-Service/README.md)

## Development Workflow

1. Start the backend server first
2. Start the frontend development server
3. Frontend will proxy API requests to backend automatically
4. Make changes and see them reflected immediately with hot-reload

## MongoDB Atlas Setup

1. Create account at [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
2. Create a new cluster (free M0 tier)
3. Create database user with password
4. Whitelist your IP (or 0.0.0.0/0 for development)
5. Get connection string from "Connect" > "Connect your application"
6. Update `.env` in Api-Service with connection string

## Contributing

This is a learning project focused on implementing modern web technologies including:
- RESTful API design
- Async Python with FastAPI
- React best practices
- RAG (Retrieval-Augmented Generation)
- Vector databases and search
- Model Context Protocol (MCP)

## Next Steps

1. ✅ Setup base project structure
2. Run both frontend and backend
3. Test the connection between them
4. Implement enquiry form in frontend
5. Add appointment booking feature
6. Integrate doctor availability
7. Add authentication
8. Implement RAG for clinical guidelines
9. Add vector search capabilities
10. Integrate MCP for AI features

## License

This is a learning project. Feel free to use and modify as needed.

## Support

For issues or questions:
1. Check the individual README files in Frontend/ and Api-Service/
2. Review the API documentation at `http://localhost:8000/docs`
3. Check MongoDB Atlas connection and configuration

---

**Happy Coding! 🚀**
