# HealthDesk API Service

Backend API service for the HealthDesk healthcare management system, built with FastAPI and MongoDB Atlas.

## Features

- Patient enquiry management
- FastAPI with async support
- MongoDB Atlas integration
- CORS enabled for frontend communication
- Pydantic models for data validation

## Tech Stack

- **Framework**: FastAPI
- **Database**: MongoDB Atlas (Motor driver for async operations)
- **Language**: Python 3.8+
- **Validation**: Pydantic

## Project Structure

```
Api-Service/
├── app/
│   ├── api/
│   │   └── routes/
│   │       ├── health.py          # Health check endpoint
│   │       └── enquiries.py       # Enquiry management endpoints
│   ├── core/
│   │   ├── config.py              # App configuration
│   │   └── database.py            # MongoDB connection
│   └── models/
│       └── enquiry.py             # Pydantic models
├── main.py                        # Application entry point
├── requirements.txt               # Python dependencies
└── .env.example                   # Environment variables template
```

## Setup Instructions

### 1. Prerequisites

- Python 3.8 or higher
- MongoDB Atlas account (free tier works fine)
- pip or pipenv

### 2. Create Virtual Environment

```bash
# Navigate to Api-Service directory
cd Api-Service

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

```bash
# Copy the example env file
cp .env.example .env

# Edit .env and add your MongoDB Atlas connection string
# Get your connection string from MongoDB Atlas dashboard
```

**MongoDB Atlas Setup:**
1. Go to [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
2. Create a free cluster
3. Create a database user
4. Whitelist your IP address (or use 0.0.0.0/0 for development)
5. Get your connection string and update `.env` file

### 5. Run the Application

```bash
# Make sure virtual environment is activated
python main.py
```

The API will be available at: `http://localhost:8000`

API Documentation (Swagger UI): `http://localhost:8000/docs`

Alternative Documentation (ReDoc): `http://localhost:8000/redoc`

## API Endpoints

### Health Check
- `GET /api/health` - Check API health status
- `GET /api/` - Root endpoint

### Enquiries
- `POST /api/enquiries/` - Create new enquiry
- `GET /api/enquiries/` - Get all enquiries
- `GET /api/enquiries/{id}` - Get specific enquiry

## Example API Request

```bash
# Create an enquiry
curl -X POST "http://localhost:8000/api/enquiries/" \
  -H "Content-Type: application/json" \
  -d '{
    "patient_name": "John Doe",
    "patient_email": "john@example.com",
    "patient_phone": "1234567890",
    "subject": "Appointment Request",
    "message": "I would like to book an appointment"
  }'
```

## Development

To enable hot-reload during development, the app is configured to run with `reload=True` in [main.py](main.py).

## Next Steps

- Add authentication & authorization
- Implement appointment booking system
- Add doctor availability management
- Integrate RAG for Clinical Guidelines
- Add Vector search capabilities
- Implement MCP (Model Context Protocol)

## Troubleshooting

**MongoDB Connection Issues:**
- Verify your connection string in `.env`
- Check if your IP is whitelisted in MongoDB Atlas
- Ensure database user credentials are correct

**Port Already in Use:**
- Change the port in [main.py](main.py) (default is 8000)
